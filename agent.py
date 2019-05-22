import requests
from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver

TIME_OUT = 20 #sec

class Agent:
    def __init__(self, config, id):
        self.id = id
        self.seedURL = config.seedURL
        self.driver = None

    def get_html(self, url):
        
        _html = ''
        try:
            res = requests.get(url, timeout=5)
            if res.status_code == 200:
                _html = res.text
        except Exception as e:
            print('[' + self.id + ']Agent requests exception : ', e )
            
        return _html
        
    def get_html_with_selenium(self, url):
        _html = ''
        try:
            self.driver.get(url)
            _html = self.driver.page_source
        except Exception as e:
            print('[' + self.id + ']Agent selenium exception : ', e )
        
        return _html


    def do_work(self, url_waiting_queue, url_result_queue):
        
        try:
            url = ''
            # pickle 때문에 __init__ 이 아닌,  여기서 선언.
            self.driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
            self.driver.implicitly_wait(5)
            self.driver.get(self.seedURL)
        
            while True:
                url = url_waiting_queue.get(timeout=TIME_OUT)
                # soup = BeautifulSoup( self.get_html(url), 'lxml')
                soup = BeautifulSoup( self.get_html_with_selenium(url), 'lxml')

                for a in soup.find_all('a', href=True):
                    url_result_queue.put( a['href'])
                    

        except Exception as e:
            print('Agent Exception :', e.__doc__, "URL : ", url)
        
        self.driver.close()
        print("Agend END : ", self.id)
    