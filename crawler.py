import multiprocessing as mp
from time import sleep
import os

from agent import Agent
from frontier import Frontier
from config import Config


class Crawler:
    
    def __init__(self):
        self.url_waiting_queue = mp.Queue()
        self.url_result_queue = mp.Queue()
        
        self.config = Config()
        self.frontier = Frontier(self.config)
        self.agents = []
        for id in range(self.config.agentCount):
            self.agents.append(Agent(id))

        #setting seed url on waiting queue
        self.url_waiting_queue.put(self.config.seedURL)


    def do_work(self):
        try:
            p_frontier = mp.Process(target=self.frontier.do_work, args= (
                self.url_waiting_queue,
                self.url_result_queue,
            ))

            p_agents = []
            for agent in self.agents:
                p_agents.append(mp.Process(target=agent.do_work, args=(
                    self.url_waiting_queue,
                    self.url_result_queue,
                )))

            #start crawling.
            p_frontier.start()
            for p_agent in p_agents:
                p_agent.start()

            #join processes
            p_frontier.join()
            for p_agent in p_agents:
                p_agent.join()

            print("--crawling complete--")

        except Exception as e:
            print('cralwer, exception : ', e)

if __name__ == "__main__":
    c = Crawler()
    c.do_work()

