#priority queue
import heapq
class priority_queue:
       def __init__(self):
              self.elements=[]
       def push(self,item,priority):
              heapq.heappush(self.elements,(priority,item))
       def pop(self):
              return heapq.heappop(self.elements)[1]
       def is_empty(self):
              return len(self.elements)==0
#main
pq=priority_queue()
pq.push('Task 1',5)
pq.push('Task 2',3)
pq.push('Task 3',7)
while not pq.is_empty():
       task=pq.pop()
       print(task)
              
