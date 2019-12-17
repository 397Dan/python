#!usr/bin/python
#coding=utf-8

'''两个循环并发执行，短的先结束，因此总的运行时间跟最慢的线程有关，并不是每个线程之和'''

import thread
from time import  sleep,ctime

def loop0():
	print 'start loop 0 at:',ctime()
	sleep(4)
	print 'loop 0 done at:',ctime()

def loop1():
	print 'start loop 1 at:',ctime()
	sleep(2)
	print 'loop1 done at:',ctime()

def main():
	print 'start at:',ctime()
	thread.start_new_thread(loop0,())
	thread.start_new_thread(loop1,())
	sleep(6)           #若把6改成2 loop0和loop1不会Done，注释掉本行，会直接all Done at
	print 'all DONE at:',ctime()

# if __name__ == '__main__':
# 	main()

'''
	1.start_new_thread(function,args,kwargs=None): 新生成一个线程，使用给定的args和可选的kwargs执行function
	必须包含前两个参数，及时执行的函数没有参数 也要传入空元组
	2.main即主线程
'''

'''上述利用线程同步（及推测最慢线程完成时间）管理线程并不是良好的方式，所以引入锁来进行线程同步，修改后代码如下：'''

loops = [14,5]

def loop(nloop,nsec,lock):
	print 'start loop',nloop,'at:',ctime()
	sleep(nsec)
	print 'loop',nloop,'done at:',ctime()
	lock.release()

def main2():
	print 'starting at:',ctime()
	locks = []
	nloops = range(len(loops))
	for i in nloops:
		lock = thread.allocate_lock()  #创建锁列表得到锁对象
		lock.acquire()  # 通过acquire得到每个锁，得到锁的效果相当于把锁锁上
		locks.append(lock)  #把锁上的锁添加到锁的列表中

	for i in nloops:  # 派生线程
		thread.start_new_thread(loop,(i,loops[i],locks[i]))
		# 转loop中的lock.release() 每个线程执行完，都会释放锁对象
	for i in nloops:  # 暂停主进程等待，所有锁被释放后才会进行
		while locks[i].locked():
			print locks[i].locked(), '----', i # 只要有一个锁没被释放 while一直循环，这个锁被释放以后，其他锁可能早已被释放
			pass  # 什么也不做 占位
		print 'all DONE at:',ctime()

if __name__ == '__main__':
	main()

'''
	1.为什么不在上锁的循环中启动进程？：1.以便所有马同时冲出围栏；
								2.获取锁需要时间，如果执行太快，可能出现获取锁之前线程就执行结束了
'''