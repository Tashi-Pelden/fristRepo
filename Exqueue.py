# # Initializing a queue
# queue = []

# # Adding elements to the queue
# queue.append('g')
# queue.append('f')
# queue.append('g')
# print(queue) # ['g', 'f', 'g'] 

# # Removing elements from the queue
# print(queue.pop(0))
# print(queue) # ['f', 'g']
# print(queue.pop(0))
# print(queue.pop(0)) 

# print("\nQueue after removing elements")
# print(queue)

# Uncommenting print(queue.pop(0))
# will raise and IndexError
# as the queue is now empty



#Implementing queue using collection.dequeue
# from collections import deque

# q = deque()

# # Adding elements to a queue
# q.append('g')
# q.append('f')
# q.append('g')
# print(q) # deque(['g', 'f', 'g'])  

# # Removing elements from a queue
# print(q.popleft())
# print(q) # deque(['f', 'g']) 
# print(q.popleft())
# print(q.popleft())

# print("\nQueue after removing elements")
# print(*q) # Empty queue 


#Implementing queue using queue
from queue import Queue

q = Queue(maxsize = 3)

# qsize() give the maxsize
# of the Queue
print(q.qsize())

# Adding of element to queue
q.put('g')
q.put('f')
q.put('g')
print(q.queue) # ['g', 'f', 'g'] 


# Return Boolean for Full
# Queue
print("\nFull: ", q.full())

# Removing element from queue
print(q.get())
print(q.queue) # ['f', 'g']
print(q.get())
print(q.get())

# Return Boolean for Empty
# Queue
print("\nEmpty: ", q.empty())

q.put(1)
print("\nEmpty: ", q.empty())
print("Full: ", q.full())

# This would result into Infinite
# Loop as the Queue is empty.
# print(q.get())
