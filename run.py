from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# avoid the pop-upwindow
options = Options()
options.add_argument("--disable-notifications")
 
chrome = webdriver.Chrome('./chromedriver', chrome_options=options)

# get band's all albums
chrome.get("https://rocknation.su/mp3/band-61")
soup = BeautifulSoup(chrome.page_source, 'html.parser')
div = soup.find("div", {"id": "clips"})
albums = []
for album in div.find('ol').findAll('li'):
    albums.append('https://rocknation.su' + album.find('a')['href'])

# get all mp3
for album in albums:
    chrome.get(album)
    time.sleep(2) # wait 2 sec
    txt_files = ""
    soup = BeautifulSoup(chrome.page_source, 'html.parser')    
    for div in soup.findAll("div", {"class": "jp-playlist"}):
        for a in div.findAll('a'):
            if a.get('onclick') != None:
                txt_files += a.get('onclick')[11:-2] + '\n'
 c               print(a.get('onclick')[11:-2])
    
    # write to txt file
    album_name = soup.find("div", {"class": "brad"}).find('span').get_text()
    print(album_name)
    with open(album_name + ".txt", "w") as text_file:
        text_file.write(txt_files)


chrome.quit()

