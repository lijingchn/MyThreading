#!/usr/bin/env python
# encoding: utf-8

import threading
import time

#def context(tjoin):
#    print "In threadContext."
#    tjoin.start()
#
#    # 将阻塞tContext直到threadjoin终止
#    tjoin.join()
#
#    # tjoin终止后继续执行
#    print "Out threadContext."
#
#def join():
#    print "threadjoin in ..."
#    time.sleep(1)
#    print "threadjoin out ..."
#
## tjoin和tContext分别为两个不同的线程
#print "------------------------------------"
#tjoin = threading.Thread(target = join)
#tContext = threading.Thread(target = context, args=(tjoin,))
#tContext.start()
#tContext.join()
#print "------------------------------------"

def thread_1():
    print "thread 1. "
    temp_1 = 1
    result["temp_1"] = temp_1
#    return temp_1

def thread_2():
    print "thread 2. "
    temp_2 = 2
    result["temp_2"] = temp_2
#    return temp_2

def main():
    global result
    result = {}
    print threading.current_thread().name
    print "------------------------------------"
    t1 = threading.Thread(target = thread_1)
    t2 = threading.Thread(target = thread_2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print "------------------------------------"
    print result
    print threading.current_thread().name

if __name__ == "__main__":
    main()




