import Queue

'''
# Using Array to form a QUEUE
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")           # Terry arrives
>>> queue.append("Graham")          # Graham arrives
>>> queue.popleft()                 # The first to arrive now leaves
'Eric'
>>> queue.popleft()                 # The second to arrive now leaves
'John'
>>> queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
'''

# QUEUE
q = Queue.Queue()
for i in range(5):
    q.put(i)
while not q.empty():
    print q.get()

# STACK
q = Queue.LifoQueue()
for i in range(5):
    q.put(i)
while not q.empty():
    print q.get()
