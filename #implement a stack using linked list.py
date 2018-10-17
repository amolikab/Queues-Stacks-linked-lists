

#implement a stack using linked list


class Node:
	def __init__ (self, data):
		self.data = data
		#self.min = data
		self.next = None
		
	def get_data(self):
		return self.data
		
	def set_data(self, data):
		self.data = data
		
	def set_next(self,node):
		self.next = node
		
	def get_next(self):
		return self.next
		
class Min_Node:		#for node of stack of min values
	def __init__ (self, data):
		self.data = data
		self.count = 1
		self.next = None
		
	def get_data(self):
		return self.data
		
	def set_data(self, data):
		self.data = data
	
	def inc_count(self):
		n = self.count 
		self.count = n+1
		
	def dec_count(self):
		n = self.count
		self.count = n-1
		
	def is_count_min(self):
		n = self.count
		if (n == 1):
			return True
		else:
			return False
	
	def set_next(self,node):
		self.next = node
		
	def get_next(self):
		return self.next
		
class min_linked_list:		#linked lsit to store all the min values

	def __init__(self, node):
		self.head = node
		
	def print_list(self):
		node = self.head
		while (node != None):
			print("%d    with count %d " % (node.data, node.count))
			node = node.next
				
	def push(self,data):
		new_node = Min_Node(data)
		head = self.head
		new_node.next = self.head
		self.head = new_node
		
	def pop(self):
		node = self.head
		self.head = node.next
		return node
		
	def min(self):
		print( " the min of the stack is %d " %self.head.data )
		
	
		
		
class linked_list:

	def __init__(self, node):
		self.head = node
		
	def print_list(self):
		node = self.head
		while (node != None):
			print(node.data)
			node = node.next
				
	def push(self,data,min_list):
		new_node = Node(data)
		min_head = min_list.head
		if (min_head.data < data ):
			min_head.inc_count()
		else:
			min_list.push(data)
		new_node.next = self.head
		self.head = new_node
		
	def pop(self, min_list):
		node = self.head
		self.head = node.next
		min_head = min_list.head
		if (min_head.is_count_min):
			min_list.pop()
		else:
			min_head.dec_count()
		return node
		
	
		
node1 = Node(20)
list = linked_list(node1)
min_node = Min_Node(node1.data)
min_list = min_linked_list(min_node)
list.push(3,min_list)
list.push(60,min_list)
list.push(10,min_list)
list.push(25,min_list)
list.push(7,min_list)
list.push(1,min_list)
list.print_list()
#list.pop()
#list.print_list()
#list.min()
min_list.print_list()
#list.pop()
min_list.min()

		
		
		
		
		
		
		
		
		
		
		
		
