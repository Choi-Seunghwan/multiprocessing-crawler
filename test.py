import validators
import requests
from bs4 import BeautifulSoup
from time import sleep
import re
from urllib.parse import urlparse
from selenium import webdriver 

seedURL = 'https://edition.cnn.com'

def test1_checkURL(url):
    s1 = 'http://'
    s2 = 'https://'

    if s1 in url or s2 in url:
        return False
    
    if validators.url(url) == False:
        return False

    return True
        

def test1():
    
    driver = webdriver.Chrome('./chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get(seedURL)
    _html = driver.page_source
    driver.close()

    soup = BeautifulSoup(_html, 'lxml')
    for a in soup.find_all('a', href=True):
        
        if test1_checkURL(a['href']):
            print(seedURL + a['href'])


if __name__ == "__main__":
    test1()