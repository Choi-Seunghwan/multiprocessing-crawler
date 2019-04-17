from time import sleep
TIME_OUT = 5 #sec

class Frontier:
    def __init__(self, config):
        self.visited = []
        self.seedURL = config.seedURL

    def check_url(self, url):
        if url in self.visited:
            return False
        
        if not url.find(self.seedURL):
            return False

        return True
    

    def do_work(self, url_waiting_queue, url_result_queue ):
            try:
                while True:
                    url = url_result_queue.get(TIME_OUT)
                
                    if self.check_url(url):
                        self.visited.append(url)
                        url_waiting_queue.put(url)
                    sleep(2)
                    print("waitingQ Size: ", url_waiting_queue.qsize())
                    print("resultQ Size: ", url_result_queue.qsize())
            except Exception as e:
                print('Frontier exception :', e)
    