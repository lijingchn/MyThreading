#!/usr/bin/env python
# encoding: utf-8

import threading
import datetime
from time import ctime, sleep

def music(song):
    for i in range(2):
        print "I am listening to <{song}>. --- {time}\n".format(song=song, time = datetime.datetime.now())
        sleep(1)

def movie(mv):
    for i in range(2):
        print "I am watching <{mv}>. --- {time}\n".format(mv=mv, time = datetime.datetime.now())
        sleep(5)

if __name__ == "__main__":
    print "============================================"
    threads = []
    t1 = threading.Thread(target=music, args=('小苹果',))
    threads.append(t1)
    t2 = threading.Thread(target=music, args=('权利的游戏',))
    threads.append(t2)
    for t in threads:
        t.start()
    t.join()
    print "all over. --- {time}".format(time = datetime.datetime.now())
    print "============================================"






























