from time import sleep
import validators

from multiprocessing.queues import Empty
import re
TIME_OUT = 30 #sec

class Frontier:
    def __init__(self, config):
        self.visited = []
        self.seedURL = config.seedURL

    def check_url(self, url):
        s1 = 'http://'
        s2 = 'https://'
        
        if url in self.visited:
            return False
        
        if s1 in url or s2 in url:
            return False

        if validators.url(url) == False:
            return False

        return True
    

    def do_work(self, url_waiting_queue, url_result_queue ):
        workCount = 0
        try:
            while True:
                url = url_result_queue.get(timeout=TIME_OUT)
               
                if self.check_url(url):
                    self.visited.append(url)
                    putUrl = self.seedURL + url
                    url_waiting_queue.put(putUrl)
                    workCount += 1
               
        except Exception as e:
            print('Frontier exception :', e.__doc__)
        print("workCount : ", workCount )
        print("wait Q size : ", url_waiting_queue.qsize() )
        print("result Q size : ", url_result_queue.qsize() )
        print("Frontier END : ")
    