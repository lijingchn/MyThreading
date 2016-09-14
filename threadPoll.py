#!/usr/bin/env python
# encoding: utf-8

import Queue, threading, sys
from threading import Thread
import time, urllib

# working thread
class Worker(Thread):
    worker_count = 0
    def __init__(self, workQueue, resultQueue, timeout = 0, **kwds):
        Thread.__init__(self, **kwds)
        self.id = Worker.worker_count
        Worker.worker_count += 1
        self.setDeamon(True)
        self.workQueue = workQueue
        self.resultQueue = resultQueue
        self.timeout = tiemout
        self.start()

    def run(self):
        """
        The get-some-work, do-some-work main loop of worker threads
        """
        while True:
            try:
                callable, args, kwds = self.workQueue.get(timeout=self.timeout)
                res = callable(*args, **kwds)
                print "worker[%2d]: %s" % (self.id, str(res))
                self.resultQueue.put(res)
            except Queue.Empty:
                break
            except:
                print 'worker[%2d]' % self.id, sys.exc_info()[:2]

class WorkerManange:
    def __init__(self, num_of_workers=10, timeout=1):
        self.workQueue = Queue.Queue()
        self.resultQueue = Queue.Queue()
        self.workers = []
        self.timeout = timeout
        self._recruitThreads(num_of_workers)
    def __recruitThreads(self, num_of_workers):
        for i in range(num_of_workers):
            worker = Worker(self.workQueue, self.resultQueue, self.timeout)
            self.workers.append(worker)

    def wait_for_complete(self):
        """
        Wait for each of them to terminate.
        """
        while len(self.workers):
            worker = self.workers.pop()
            worker.join()
            if worker











































