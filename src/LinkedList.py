class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

	def __str__(self):
		print(self.data)

class LinkedList:
	def __init__(self):
		self.head = None
		self.size = 0

	def append(self, node):
		if self.head is None:
			self.head = node
		cursor = self.head
		while cursor.next is not None:
			cursor = cursor.next
		cursor.next = node
		node.next = None
		self.size += 1

	def extend(self, li):
		if self.head is None:
			self.head = li.head
		cursor = self.head
		while cursor.next is not None:
			cursor = cursor.next
		cursor.next = li.head
		self.size += len(li)

	def __len__(self):
		return self.size

	def __str__(self):
		if self.size == 0:
			return '[]'
		cursor = self.head
		s = '['
		for i in range(self.size - 1):
			s += str(cursor.data) + ', '
			cursor = cursor.next	
		s += str(cursor.data)
		s += ']'
		return s

li = LinkedList()
li2 = LinkedList()
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(1)
li.append(n1)
li.append(n2)
li.append(n3)
li.append(n4)
li.append(n5)
n6 = Node(6)
n7 = Node(8)
li2.append(n6)
li2.append(n7)
print(li)
print(len(li))
li.extend(li2)
print(li)
print(len(li))