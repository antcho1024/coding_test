# class Node:
#     def __init__(self, data, next=None, prev = None):
#         self.data = data
#         self.next = next
#         self.prev = prev
#
# n,k = map(int, input().split())
#
# head = Node(1)
# curr = head
# for i in range(2, n+1):
#     new_node = Node(i)
#     new_node.prev=curr
#     curr.next=new_node
#     curr=curr.next
# curr.next=head
# head.prev=curr
#
# curr = head
# l = list()
# while curr.next!=curr:
#     for _ in range(1,k):
#         curr=curr.next
#     l.append(curr.data)
#     curr.prev.next = curr.next
#     curr.next.prev = curr.prev
#     curr=curr.next
# l.append(curr.data)
#
# print("<", end="")
# for i in range(len(l)-1):
#   print(l[i], end=", ")
# print(str(l[len(l)-1])+">")


### 디큐로 퓰기 (디큐 : 스택 + 큐)

from collections import deque

n, k = map(int, input().split())

# 1~n번 사람
people = deque()
for i in range(1, n+1): people.append(i)
result = []

while people:
  for _ in range(k-1):
    people.append(people.popleft())

  result.append(people.popleft())

print(str(result).replace('[', '<').replace(']', '>'))