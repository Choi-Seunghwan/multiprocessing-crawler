import requests
from bs4 import BeautifulSoup
from time import sleep


TIME_OUT = 5 #sec

class Agent:
    def __init__(self, config, id):
        self.id = id
        self.seedURL = config.seedURL

    def get_html(self, url):
        
        _html = ''
        try:
            res = requests.get(url, timeout=5)
            if res.status_code == 200:
                _html = res.text
        except Exception as e:
            print('[' + self.id + ']Agent requests exception : ', e )
            
        return _html
        

    def do_work(self, url_waiting_queue, url_result_queue):
        try:
            url = ''
            while True:
                url = url_waiting_queue.get(timeout=TIME_OUT)
                soup = BeautifulSoup( self.get_html(url), 'lxml')
                
                for a in soup.find_all('a', href=True):
                    url_result_queue.put( a['href'])
                    
                # sleep(2)

        except Exception as e:
            print('Agent Exception :', e.__doc__, "URL : ", url)
        
        print("Agend END : ", self.id)
    