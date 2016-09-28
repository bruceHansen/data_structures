#!/usr/bin/env python3
from circularlist import CircularLinkedList, CircularLinkedListIterator
from doublylinkedlist import DoublyLinkedList
from stack import Stack
from queue import Queue

import csv 


class Processor(object):
    
    def __init__(self):
        '''Creates the lists'''
        self.callahead = DoublyLinkedList()
        self.waiting = DoublyLinkedList()
        self.appetizers = Queue()
        self.buzzers = Stack()
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.songs = CircularLinkedList()
        self.songs.add('Song 1')
        self.songs.add('Song 2')
        self.songs.add('Song 3')
        self.songs_iter = CircularLinkedListIterator(self.songs)

    def run(self, f, w):
        '''Processes the given file stream.'''
        for line_i, line in enumerate(f):  
            w.writerow(['{}:{}'.format(line_i, line)])

            col_two = line.rstrip().split(',')[1]
            line = line.rstrip().split(',')[0]
            # split and handle the commands here 

            if line=='DEBUG':
                self.debug(w)

            if line=='SONG':
                w.writerow([self.songs_iter.next()])

            if line=='APPETIZER':
                appetizer = self.appetizers.dequeue()
                if type(appetizer) != IndexError:
                    w.writerow(['{} >>> {}'.format(appetizer, self.waiting.debug_reverse())])
                else:
                    w.writerow([appetizer])

            if line=="APPETIZER_READY":
                self.appetizers.enqueue(col_two)

            if line=="CALL":
                self.callahead.add(col_two)    

            if line=="ARRIVE":
                #Check if the party called ahead
                call_ahead = False

                for party in range(self.callahead.size ):
                    #print('this is the party range', party)
                    if(col_two)==self.callahead.get(party):
                        #print(col_two, 'adding to waiting from call')
                        call_ahead = True
                        break

                if call_ahead:
                        #move party ahead five spaces                       
                    five_spots_ahead = 5 
                    waiting_size = self.waiting.size 
                
                    if waiting_size >= 6:
                        insert_at = waiting_size - five_spots_ahead                
                    else:
                        insert_at = 0 

                    self.waiting.insert(insert_at, col_two)
                        #delete from the callahead list

                    self.callahead.delete(party)                   
                else:
                    self.waiting.add(col_two)
                print(line, line_i)
                my_buzzer = self.buzzers.pop()
                if my_buzzer == IndexError:
                    w.writerow([my_buzzer])

            if line=="SEAT": 
                my_row = self.waiting.get(0)
                if my_row == IndexError:
                    w.writerow(['There are no customers to seat'])
                else:
                    w.writerow([self.waiting.get(0)])

                print('my row', my_row)
                if my_row != IndexError:
                    print('my if not eror row', my_row)
                        #delete party from waiting list 
                    self.waiting.delete(0)
                    print(line, line_i)
                    self.buzzers.push('Buzzer')

            if line=="LEAVE":
                for cust in range(self.waiting.size):
                    if col_two==self.waiting.get(cust):
                        self.waiting.delete(cust)
                print(line, line_i)
                self.buzzers.push('Buzzer')

    def debug(self, w):
        w.writerow([self.callahead.debug_print()])
        w.writerow([self.waiting.debug_print()])
        w.writerow([self.appetizers.debug_print()])
        w.writerow([self.buzzers.debug_print()])
        w.writerow([self.songs.debug_print()])

#######################
###   Main loop

with open('data.csv', newline='') as f:
    processor = Processor()
    csvfile = open('my_output.txt', 'w', newline='')
    w = csv.writer(csvfile, delimiter=' ', quoting=csv.QUOTE_NONE, escapechar=' ')
    processor.run(f, w)



