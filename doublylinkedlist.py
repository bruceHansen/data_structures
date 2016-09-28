#!/usr/bin/env python3

class DoublyLinkedList():

	'''
	A linked list implementation that holds arbitrary objects.
	'''
	
	'''Creates a linked list.'''
	def __init__(self):
		self.head = Node(None)
		self.tail = Node(None)
		self.head.next = self.tail
		self.size = 0

		#DOUBLE

	def add(self, item):

		my_node = Node(item)

			#ensure you won't go below bounds of list
		if self.size == 0:
			self.tail = my_node   
			self.head.next = self.tail 

		else:
			temp_tail = self.tail  
			self.tail.next = my_node 
			self.tail = my_node 
			self.tail.prev = temp_tail 
   
		self.size += 1   

		#DOUBLE

	def set(self, index, item):
		index = int(index)
		my_check = self._check_bounds(index)
		if my_check:
			return my_check 

		if self.size == 0:
			my_node = Node(item)
			self.tail = my_node
			self.head.next = self.tail  
				#add size if no size to list
			self.size += 1

		else:

			new_node = Node(item)
			temp = self.head.next
		
				#get item before index position in order to set new next pointer to index
			for items in range(index - 1):
				
				temp = temp.next

			#with set, you need to replace the item, with insert, you don't replace, just add into list
				# get node after the index node 
			node_after = temp.next.next
				#set new pointer in item under new position
			temp.next = new_node 
				#set new node to point to next item in the list
			new_node.next = node_after  
				#set previous pointers
			node_after.prev = new_node
			new_node.prev = temp 

		#DOUBLE

	def insert(self, index, item):
		index = int(index)
		
		my_check = self._check_bounds(index)
		if my_check:
			return my_check 

		if self.size == 0:
			my_node = Node(item)
			self.tail = my_node
			self.head.next = self.tail 

		else:
			new_node = Node(item)

			temp = self.head
				#get item before set position in order to set new pointer 
			for items in range(index):	
				temp = temp.next

			#with set, you need to replace the item, with insert, you don't replace, just add into list

				#set pointer var for item to be put in the list
			new_pointer_temp = temp.next  
				#set new node to point to node it replaced
			new_node.next = new_pointer_temp  
				#set new pointer in item one below new position
			temp.next = new_node
				#set previous 
			new_node.prev = temp
			new_pointer_temp.prev = new_node

		self.size += 1

		#DOUBLE

	def get(self, index):

		index = int(index)

		my_check = self._check_bounds(index)
		if my_check:
			return my_check 

		temp = self.head.next  
		for items in range(index):
			temp = temp.next

		if temp.value == None:
			return IndexError

		return temp.value

		#DOUBLE
	def delete(self, index):
		index = int(index)

		my_check = self._check_bounds(index)
		if my_check:
			return my_check

		temp = self.head 
		for item in range(index):
			temp = temp.next

			#set variable for space above item to be deleted
		new_pointer_temp = temp.next.next
		
		self.size -= 1

			#point to space above item to be deleted
		if new_pointer_temp != None:
			new_pointer_temp.prev = temp
			temp.next = new_pointer_temp
		else:
			self.tail = temp
			self.head.next = self.tail

	def swap(self, index1, index2):

		index1 = int(index1)
		index2 = int(index2)

		my_check1 = self._check_bounds(index1)
		my_check2 = self._check_bounds(index2)

		if my_check1:
			return my_check1

		if my_check2:
			return my_check2
		
		temp1 = self.head.next 
		for item in range(index1):
			temp1 = temp1.next 

		temp2 = self.head.next
		for item in range(index2):
			temp2 = temp2.next 

		ind1_value = temp1.value  	
		temp1.value = temp2.value 
		temp2.value = ind1_value 


	def debug_print(self):
		f_temp = self.head  
		r_temp = self.tail 
		my_f_list_items = []
		my_r_list_items = []

		for length in range(self.size):
				#read list front to back, must read in value of f_temp first
			f_temp = f_temp.next 
			my_f_list_items.append(f_temp.value)
			
			my_r_list_items.append(r_temp.value)
			r_temp = r_temp.prev

		forward_string = ', '.join(map(str, my_f_list_items))
		reverse_string = ', '.join(map(str, my_r_list_items))

		my_return = '{} >>> {} >>> {}'.format(self.size, forward_string, reverse_string)
		return my_return 

	def debug_reverse(self):
		my_list = []

		my_length = self.size

		if self.size > 2:
			my_length = 3
		
		temp = self.tail 
		for length in range(my_length):
				#read list front to back, must append value then increment
			my_list.append(temp.value)
			temp = temp.prev


		string = ', '.join(map(str, my_list))

		return string 

	def _check_bounds(self, index):

		if self.size == 0 and index == 0:
			return 

		if index > self.size - 1 or index < 0:
			return IndexError("Error: {} is not within the bounds of the current list".format(index))


######################################################
###   A node in the linked list
		
class Node(object):
	'''A node on the linked list'''
	
	def __init__(self, value):
		self.value = value
		self.prev = None
		self.next = None
		
	def __str__(self):
		return '<Node: {}>'.format(self.value)
