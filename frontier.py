from time import sleep
import validators

from multiprocessing.queues import Empty
import re
TIME_OUT = 5 #sec

class Frontier:
    def __init__(self, config):
        self.visited = []
        self.seedURL = config.seedURL

    def check_url(self, url):
        
        if url in self.visited:
            return False
        
        if not self.seedURL in url:
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
                    url_waiting_queue.put(url)
                    workCount += 1
                # sleep(2)
               
        except Exception as e:
            print('Frontier exception :', e.__doc__)
        
        print("wait Q size : ", url_waiting_queue.qsize() )
        print("result Q size : ", url_result_queue.qsize() )
        print("Frontier END : ")
    