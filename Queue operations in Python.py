from collections import deque
queue=deque([1,2,3,4])
print("original",queue)
queue.append(30)
print(queue)
print(queue.popleft())
print(queue.popleft())
print(queue)
