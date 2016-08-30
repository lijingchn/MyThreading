#!/usr/bin/env python
# encoding: utf-8

import redis

class Task(object):
    def __init__(self):
        self.rcon = redis.StrictRedis(host='localhost', db=8)
        self.ps = self.rcon.pubsub()
        self.ps.subscribe('task:pubsub:channel')

    def listen_task(self):
        for i in self.ps.listen():
            if i['type'] == 'message':
                print "Task get", i['data']

if __name__ == '__main__':
    print 'listen task channel'
    Task().listen_task()
