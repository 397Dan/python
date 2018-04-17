#!usr/bin/python
#coding=utf-8

'''
	步骤：
	1.导入Tkinter模块；
	2.创建一个顶层窗口，容纳整个GUI应用；
	3.在顶层窗口对象上（或者其中）构建所有的GUI组件（及其功能）；
	4.通过底层的应用代码将这些GUI组件链接；
	5.进入主事件循环
'''

import Tkinter

def resize(ev = None):
	label.config(font='Helvetica -%d bold'%scale.get())

top = Tkinter.Tk()
top.geometry() # 设置顶层窗口的大小(不能用)
label = Tkinter.Label(top,text = "Hello World",font = 'Helvetica -12 bold')
label.pack()

scale = Tkinter.Scale(top, from_=10,to = 40,orient=Tkinter.HORIZONTAL,command = resize)
scale.set(12)
scale.pack(fill = Tkinter.X,expand = 1)

quit = Tkinter.Button(top,text="Hello World2",command = top.quit,bg='red',fg='white') # top.quit 执行退出
quit.pack(fill = Tkinter.X,expand = 1)

Tkinter.mainloop()