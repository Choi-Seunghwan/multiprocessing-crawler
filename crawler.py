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
        self.frontier = Frontier()
        self.agents = []
        for id in range(self.config.agentCount):
            self.agents.append(Agent(id))


    def do_work(self):
        try:
            p_frontier = mp.Process(target=self.frontier.do_work, args= (
                self.url_waiting_queue,
                self.url_result_queue,
            ))
            
        except Exception as e:
            print('cralwer, exception : ', e)