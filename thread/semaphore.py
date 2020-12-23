from multiprocessing import Process, Semaphore, Lock, Queue
import time
from random import random

'''
生产者放入队列中数据，然后消费者将数据取出来。
'''

buffer = Queue(10)
empty = Semaphore(3)
full = Semaphore(0)
lock = Lock()

class Consumer(Process):

    def run(self):
        global buffer, empty, full, lock
        while True:
            full.acquire()
            lock.acquire()
            print 'Consumer get', buffer.get()
            time.sleep(1)
            lock.release()
            empty.release()


class Producer(Process):
    def run(self):
        global buffer, empty, full, lock
        while True:
            empty.acquire()
            lock.acquire()
            num = random()
            print 'Producer put ', num
            buffer.put(num)
            time.sleep(1)
            lock.release()
            full.release()


if __name__ == '__main__':
    p = Producer()
    c = Consumer()
    p.daemon = c.daemon = True
    p.start()
    c.start()
    p.join()
    c.join()
    print 'Ended!'