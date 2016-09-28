#!/usr/bin/env python3
from linked_list import LinkedList

class Queue(object):
    '''
    A linked list implementation of a queue.
    
    This contains a LinkedList internally.  It does not extend LinkedList.
    In other words, this class uses "Composition" rather than "Inheritance".
    '''
    
    def __init__(self):
        '''Constructor'''
        self.list = LinkedList()
    
    def debug_print(self):
        '''Prints a representation of the entire queue.'''

            #prepare list to add all items in queue
        my_items = self.list.debug_print()

        return my_items 

    def enqueue(self, item):
        '''Adds an item to the end of the queue'''

        self.list.add(item)
        
    def dequeue(self):
        '''
        Dequeues the first item from the list.  This involves the following:
            1. Get the first node in the list.
            2. Delete the node from the list.
            3. Return the value of the node.
        '''

        first_node = self.list.get(0)
        self.list.delete(0)

        return first_node 

    def size(self):
        '''Returns the number of items in the queue'''
        return self.list.size 

