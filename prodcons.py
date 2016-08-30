#!/usr/bin/python
# encoding:utf-8

import random
import time
import datetime
from Queue import Queue
from threading import Thread

queue = Queue(10)

class Producer(Thread):
    def run(self):

        elem = random.randrange(9)
        queue.put(elem)
        print "{}厨师{}做了{}碗饭，还剩{}碗饭没卖完～".format(datetime.datetime.now(),self.name,elem,queue.qsize())
        time.sleep(random.random())

class Consumer(Thread):
    def run(self):
        elem = queue.get()
        print "{}吃货{}吃了{}碗饭，还有{}碗饭可以吃(*^__^*)".format(datetime.datetime.now(),self.name,elem,queue.qsize())
        time.sleep(random.random())

def main():
    for i in range(2):
        p = Producer()
        p.start()
    for i in range(2):
        c = Consumer()
        c.start()

if __name__ == "__main__":
    main()

