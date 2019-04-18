import validators
import requests
from bs4 import BeautifulSoup
from time import sleep
import re
from urllib.parse import urlparse


def get_html(url):
    _html = ''
    res = requests.get(url)
    if res.status_code == 200:
        _html = res.text
    return _html

regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)


arr = ['https://namu.wiki/policy',]
seedURL = '/'


if re.match( regex, arr[0]) == True:
    print("choi")


url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', seedURL) 

print(url)