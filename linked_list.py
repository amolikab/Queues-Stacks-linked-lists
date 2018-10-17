#implement linked list
# linked list
#add, insert, delete, next node, prev node, append, print

#for node
#get value, set value, get next

class Node:
	def __init__(self,value):
		self.data = value
		self.next = None

	def set_data(self,data):
		self.data = data
		
	def get_data(self):
		return self.data
		
	def get_next(self):
		return self.next
		
	def set_next(self, node):
		self.next = node

		
class linked_list:
	
	def __init__(self,node):
		self.head = node
		
	def print_list(self):
		node = self.head
		while (node != None):
			print(node.data)
			node = node.next
	
	def get_node(self,data):
		node = self.head
		while(node != None):
			if(node.data == data):
				return node
			else:
				node = node.next

	
	def add (self, data):
		new_node = Node(data)
		new_node.set_next(self.head)
		self.head = new_node
	
	def pop (self):
		node = self.head
		self.head = node.next
		
	def insert(self, data, position):
		new_node = Node(data)
		node = self.head
		for i in range(1,position -1):
			node = node.next
		temp = node.next
		node.next = new_node
		new_node.next = temp
		
	def delete(self,position):
		#traverse the list uptill position-1
		node = self.head
		
		for i in range(1,position-1):
			node = node.next
		x = node.next #node to be deleted
		y = x.next	#node after the deleted node
		node.next = y	
		

def isPresent(list, data, n):	#for dulplicate without dict
	#traverse list till new_node
	node = list.head
	for i in range(1,n):
		if (node.data == data):
			return True
		else:
			node = node.next
	return False
		
		
		
def Duplicate(list):	#with/without dict
	#d = dict()	
	#traverse the list	
	position = 1
	node1 = list.head
	while (node1 != None):
		#print("looking at node %d " % node1.data)
		if (isPresent(list,node1.data,position)): #if(node.data in d)
			print("Need to delete %d " % node1.data)
			list.delete(position)
		else:
			#d[node1.data] = True
			position = position + 1	
		node1 = node1.next

#delete element if only node to be deleted is provided
def delete_without_head_of_list(node):
	
	node1 = node
	node2 = node1.next
	
	node1.set_data(node2.data)
	
	node1.next = node2.next
	
		
node1 = Node(65)
list = linked_list(node1)
list.add(92)
list.add(22)
list.add(10)
list.add(32)
list.add(22)
list.add(3)
list.add(10)
list.print_list()
print("end list")
#Duplicate(list)
#print("list after delete")
#list.print_list()
node = list.get_node(3)

delete_without_head_of_list(node)
list.print_list()











