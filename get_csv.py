from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# avoid the pop-upwindow
options = Options()
options.add_argument("--disable-notifications")
 
chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
chrome.get("http://isophonics.net/content/reference-annotations-zweieck")

soup = BeautifulSoup(chrome.page_source, 'html.parser')

txt_files = ""
for ol in soup.findAll('ol'):
    for li in ol:
        for ul in li.findAll('ul'):
            if ul.find('li'):
                a = list(ul.find_all('a', {'href': True}, text='csv'))
                try:
                    txt_files += 'http://isophonics.net' + a[2]['href'] + '\n'
                    print(a[2])
                except:
                    print('except', a)

chrome.quit()

with open("Output.txt", "w") as text_file:
    text_file.write(txt_files)