Scrapy并发参数优化
==================
settings.py
CONCURRENT_REQUESTS = 32
DOWNLOAD_DELAY = 3
CONCURRENT_REQUESTS_PERDOMAIN =16
CONCURRENT_REQUESTS_PER_IP = 16
Twisted 异步I/O框架
def response(*args, **kwargs)  
             keyword args 接收key-value形式参数（字典）


			 
多进程
==================
多并发 多进程 逻辑
  单任务—>同步—>多任务—>异步
  进程间父子关系
  产生新进程 os.fork()  (linux,mac)
             mutiporcessing.Process()
			 
  res = os.fork()  res = 0 则为子进程，非0父进程
  mutiprocessing.Process(group=name, target=None,name=None,args=()，kwargs={})
  target函数 name给进程去别名 group分组，用得少
  target=f() 函数执行，执行的结果给target
  target=f  f函数这个对象传递
  ```python
	from multiprocessing import Process  
	def f(name):
		print(f'hello {name}')
		  
	if __name__=='__main__':
		p=Process(target=f, args=('john',))
		#args传的是元组
		p.start() #产生子进程
		p.join()  #父进程等待子进程结束后才结束
  ```
  
  
  
进程间通信 队列
==================
变量赋值是在每个进程的堆栈中，跨进程到另一个进程中，堆栈不传递
主要共享方式：队列、管道、共享内存  
多进程争抢资源：锁机制

队列
------
```python
from multiprocessing import Queue
#队列进程安全，多人读、写
q=Queue()  实例化
q.put([])  q.get()
````
管道(队列实现底层是pipe)
----------------------
```python
from multiprocessing import Pipe
    parent_conn,child_conn = Pipe()
	pipe.rece()
	pipe.send()
#多人读写，pipe数据会损坏
```
共享内存
-------------
from multiprocessing import Value,Array
Value,Array 将数据存储在共享内存映射中

for _ in range(5)  _只是重复次数，该变量并不想用

资源抢占 锁机制
==================
进程由操作系统进行调度
```python
from multiprocessing as mp
l=mp.Lock() #定义进程锁
v=mp.Value() #定义共享内存
l.acquire()  #锁住 
l.release()  #释放
```
多进程 进程池
==================
from mutiporcessing.pool import Pool
p=Pool(4)
控制并行数量，进程数等于逻辑cpu数量

for i in range(10):
    p.apply_async(run, args(i,))#异步运行
	p.apply()#同步方式
	
join之前必须要有close或terminate，父进程需要等子进程结束，拿到子进程结果

with描述符
with Pool(processes=4) as pool:
    result = pool.apply_async(f,(10,))
	
迭代器 next(it)
pool.map(f,range(10))  #列表
it = pool.imap(f,range(10)) #迭代器

多线程
==================
C++ JAVA中高级应用，Python中多进程多线程配合使用

进程 线程区别
-----------
进程概念比较重，有自己结构存在，资源开销重
多线程跑在一个进程中，同步数据方便

阻塞 非阻塞 同步 异步
-----------------
阻塞 非阻塞 调用方看的结果  发起方发起后还能否处理别的问题 拨电话 requests 
同步 异步  被调用方看的结果  接电话或回短信
异步非阻塞 排错调试难

为什么有进程、线程、协程
-------------
Python运行时多线程只能在一个物理核心上运行，多线程方便通信，多进程占用cpu
线程、进程的调度由系统决定
协程 切换更轻量级，由用户把控

并发concurrent
----------
Two Queue One Machine

并行parallel
-----------
Two Queue Two Machine

```python
import threading
#函数方式
t1=threading.Thread(target=run, args=('thread 1',))

t1.start()

#面向对象方式
class MyThread(threading.Thread):
    def __init__(self,n):
	    super().__init__()  #父类init引入,super 当前MyThread父类
		self.n = n
	def run(self):
	    print('current task:', self.n)
		
t1 = MyThread('task1')
t1.start()
t2.start()
t1.join()
t2.join()
#调试用
thread1.is_alive()
thread1.getName()
```

线程锁
==================
Lock Rlock(嵌套锁)

condition条件锁
threading.Condition()
conn.acquire()
conn.wait_for(condition)
conn.release()

semaphore 信号量 信号锁
semaphore = threading.BounderdSemaphore(5)

event 事件锁
定义一个flag，set设为True，clear设为False
event = threading.Event()
event.clear()  #红灯
event.set()    #绿灯

timer 指定几秒后运行
t=threading.Timer(1,run)
t.start()

多线程 队列
==================
```python
import queue
q=queue.Queue(5)  #队列大小
q.put(111)
q.get()
q.task_done()     #提示q.join()是否停止阻塞

q.qsize()
q.empty()
q.full()
#队列是线程安全的
#可实现生产者、消费者
```
优先级队列
```python
q=queue.PriorityQueue()
q.put((1,'work'))
q.put((-1,'life'))
#数字越小优先级越高
#同优先级，先进先出
```
后进先出队列（类似堆栈）
q = queue.LifoQueue()

双向队列
使用较少，Python哲学是简

t.setDaemon(True)  #关掉终端依然可以运行
t.start()

线程池
==================
from multiprocessing.dummy import Pool as ThreadPool  #一般的线程池
from concurrent.futures import ThreadPoolExecutor     #并行任务的高级封装 python3.2后支持

seed=['a','b','c','d']
executor.submit(fun,seed)   #['a','b','c','d']
executor2.map(fun,seed)     #映射传递4次 a b c d

GIL锁与多线程性能瓶颈
==================
Python解释器CPython，多线程是伪并发，不是真正意义多线程
Global Interpertor Lock全局解释锁
每个进程只有1个GIL锁，拿GIL锁使用CPU
CPU密集型 单线程与多线程相差不大
I/O密集型（爬虫） 密集切换，多线程适用
