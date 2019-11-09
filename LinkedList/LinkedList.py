# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 09:27:52 2019

@author: kpvp2
"""
class Node:
    def __init__(self, data=None, prev=None, next1=None):
        self.data = data
        self.prev = prev
        self.next1 = next1

class DoublyLinkedList:
    def __init__(self):
        self.start_node = None
        self.tail_node = None
        self.Count = 0
        '''
        Generates the doubly-linked list, and sets the
        first and last node to None as this is an empyt list
        '''

    def print_list(self):
        if self.start_node is None:
            print("The List is Empty")
        else:
            n = self.start_node
            while n is not None:
                print(n.data, " ")
                n = n.next1

    def print_reverse(self):
        if self.start_node is None:
            print("The List is Empty")
        else:
            n = self.tail_node
            while n is not None:
                print(n.data, " ")
                n = n.prev

    def addfirst(self, data):
        '''
        Adds a new node at the start of the Linked List
        '''
        nnode = Node(data, next1 = self.start_node)
        if self.start_node:
            self.start_node.prev = nnode
        self.start_node = nnode
        self.Count += 1
        if self.Count == 1:
            self.tail_node = self.start_node

    def append(self, data):
        '''
        Adds a new node at the end of the Linked List
        '''
        nnode = Node(data)
        if self.Count == 0:
            self.start_node = nnode
        else:
            self.tail_node.next1 = nnode
            nnode.prev = self.tail_node
        self.tail_node = nnode
        self.Count += 1

    def delfirst(self):
        '''
        Removes the first node in the Linked List
        '''
        if self.Count > 0:
            self.start_node = self.start_node.next1
            self.Count -= 1
            if self.Count == 0:
                self.tail_node = None

    def dellast(self):
        ''' 
        Removes the last node in the Linked List
        '''
        if self.Count > 0:
            if self.Count == 1:
                self.start_node = None
                self.tail_node = None
            else:
                self.tail_node = self.tail_node.prev
                self.tail_node.next1 = None
            self.Count -= 1
            if self.Count == 1:
                self.start_node = self.tail_node

    def find(self, key):
        ''' 
        Find an element in the Linked List (First Element)
        '''
        cnode = self.start_node
        while cnode != None:
            if cnode.data == key:
                print('{} is in the list'.format(key))
                return(cnode)
            cnode = cnode.next1
        if cnode == None:
            print("{} not found in the List".format(key))

    def remove(self, key):
        c = self.start_node
        while c != None:
            if c.data == key :
                if c.prev != None:
                    c.prev.next1 = c.next1
                else:
                    self.delfirst()
                return True
            c = c.next1
        return False

    def insert_after(self, x, data):
        c = self.start_node
        while c != None:
            if c.data == x :
                break;
            c = c.next1
        if c == None:
            print("{} not in the list".format(x))
        else:
            if c.next1 != None:
                n = Node(data, c, c.next1)
                c.next1 = n
            else:
                n = Node(data, c)
                n.next1 = None
                self.tail_node = n
                c.next1 = n
            self.Count += 1

    def insert_before(self, x, data):
        c = self.start_node
        while c != None:
            if c.data == x :
                break;
            c = c.next1
        if c == None:
            print("{} not in the list".format(x))
        else:
            if c.prev != None:
                n = Node(data, c.prev, c)
                c.prev.next1 = n
                c.prev = n
                self.Count += 1
            else:
                self.addfirst(data)

    def insertatindex(self, index, data):
        ''' Indexing Starts at 0'''
        if index == 0:
            self.addfirst(data)
        elif index == self.Count - 1:
            self.append(data)
        elif index >= self.Count:
            print("Index out of Bounds")
        else:
            c = self.start_node
            i = 0
            while i < index:
                c = c.next1
                i += 1
            n = Node(data, c.prev, c)
            c.prev.next1 = n
            c.prev = n
            self.Count +=1

    def removeatindex(self, index):
        ''' Indexing Starts at 0'''
        if index == 0:
            self.delfirst()
        elif index == self.Count-1:
            self.dellast()
        elif index >= self.Count:
            print("Index Out of Bounds")
        else:
            c = self.start_node
            i = 0
            while i < index:
                c = c.next1
                i += 1
            p = c.prev
            n = c.next1
            p.next1 = n
            n.prev = p
            self.Count -= 1
    
    def enumerate(self):
        c = self.start_node;
        while c != None:
            yield c
            c = c.next1
            
    def size(self):
        '''Returns the Size of the List'''
        return self.Count
