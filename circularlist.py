


class CircularLinkedList(object):
    '''
    A circularly-linked list implementation that holds arbitrary objects.
    '''
   
    '''Creates a linked list.'''
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.size = 0

        #Circular

    def add(self, item):

        my_node = Node(item)
        if self.size == 0:
            self.tail = my_node
            self.head.next = self.tail 
            self.tail.next = self.tail 
        else: 
                #point tail to first node
            self.tail.next = my_node 
            self.tail = my_node 
            self.tail.next = self.head.next 

        self.size += 1     

        #Circular - nothing 
    def set(self, index, item):
        index = int(index)
        my_check = self._check_bounds(index)
        if my_check:
            return my_check

        temp = self.head.next
    
            #get item before set position in order to set new pointer 
        for items in range(index - 1):
            temp = temp.next

        new_pointer_temp = temp.next.next  

        new_node = Node(item)
            #set new pointer in item under new position
        old_pointer_temp = temp
        old_pointer_temp.next = new_node
            #set new node to old node pointer

        new_node.next = new_pointer_temp

        #Circular - nothing 
    def get(self, index):

        index = int(index)

        my_check = self._check_bounds(index)
        if my_check:
            return my_check 

        temp = self.head.next  
        for items in range(index):
            temp = temp.next

        return temp.value

        #Circular
    def insert(self, index, item):
        index = int(index)
        my_check = self._check_bounds(index)

        if index == 0 and self.size == 0:
            my_node = Node(item)
            self.tail = my_node
            self.head.next = self.tail 
            self.tail = my_node
            self.tail.next = self.tail 

        else:
            if my_check:
                return my_check

            temp = self.head.next
                #get item before set position in order to set new pointer 
            for items in range(index - 1):
                temp = temp.next

                #set pointer var for item to be pushed up in the list
            new_pointer_temp = temp.next  

            new_node = Node(item)
                #set new node to point to node it replaced
            new_node.next = new_pointer_temp  
                #set new pointer in item one below new position
            old_pointer_temp = temp
            old_pointer_temp.next = new_node
        
        self.size += 1

        #Circular - nothing 
    def delete(self, index):
        index = int(index)

        my_check = self._check_bounds(index)
        if my_check:
            return my_check

        temp = self.head.next 
        for item in range(index - 1):
            temp = temp.next

            #set variable for space above item to be deleted
        new_pointer_temp = temp.next.next
            #point to space above item to be deleted
        temp.next = new_pointer_temp 

        self.size -= 1

        #Circular - nothing 
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
        my_list_items = []

        temp = self.head 
        for items in range(self.size):
            temp = temp.next 
            my_list_items.append(temp.value)

        string = ', '.join(map(str, my_list_items))
        #fair game to pack the linked-list into a list??
        my_return = '{} >>> {}'.format(self.size, string)
        return my_return

    def _check_bounds(self, index):
        if index > self.size - 1 or index < 0:
            return IndexError("Error: {} is not within the bounds of the current list".format(index))


        #SPECIFIC TO A CIRCULARLY-LINKED LIST

    def debug_cycle(self, count):
        '''Prints a representation of the entire cycled list up to count items'''
            
            #Set variables

        my_list_items = []
            #cycle through for count number of times
        my_range = count * self.size 
        temp = self.head.next 
        for item in range(my_range):
            temp = temp.next 
            my_list_items.append(temp)
            
        return my_list_items 


        #string = ', '.join(map(str, my_list_items))
        #my_return = '{} >>> {}'.format(self.size, string)
        #return my_return
        
        
    def _get_node(self, index):
        '''Retrieves the Node object at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''  

        my_check = self._check_bounds(index)
        if my_check:
            return my_check

        temp = self.head.next 
        for item in range(self.size - 1):
            temp = temp.next

        return temp.value 


######################################################
###   A node in the linked list
        
class Node(object):
    '''A node on the linked list'''
    
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def __str__(self):
        return '<Node: {}>'.format(self.value)



######################################################
###   An iterator for the circular list

class CircularLinkedListIterator(object):
    
    def __init__(self, circular_list):
        '''Starts the iterator on the given circular list.'''

        self.list = circular_list  
        self.temp = self.list.head

    def has_next(self):
        '''Returns whether there is another value in the list.'''
        has_next = True 

        return has_next 

    def next(self):
        '''Returns the next value, and increments the iterator by one value.'''

        next = self.has_next()

        if next:
            self.temp = self.temp.next 

        return self.temp.value 

    
        
