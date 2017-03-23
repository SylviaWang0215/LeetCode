'''
class Fruit:
    def _init_(self, name, edible):
        self.upper = name.upper()
        self.edible = edible
    def display(self):
        print '*' * 50
        print 'Fruiut name (upper case): %s.' % self.upper
        if self.edible:
            print "It's edible."
        else:
            print "It's not edible"
    #def accounting():
        #print "How many %sS do you want?" % self.upper
        

a = raw_input('Enter a fruit name')
b = input('Is it edible? Enter "1" or "True" if edible; otherwise, "0" or False: ')
fruitObj = Fruit(a,b)
fruitObj.display()
'''

'''
Question 2

class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

# return the data of a node
    def getData(self):
        return self.data

# return the reference to next node (move)
    def getNext(self):
        return self.next

# assign a new data value to the current node
    def setData(self,newdata):
        self.data = newdata

# assign a new reference pointing to next node
    def setNext(self,newnext):
        self.next = newnext
'''

from Q2_NodeClass_Ayoola_Afolabi import Node


class LinkedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,element):
        temp = Node(element)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self,element):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == element:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self,element):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == element:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
            
#printing all the elements of the list 2(a).
    def printList(self):
        current = self.head
        while current != None:
            print(current.getData())
            current = current.getNext()

# 2b
    def findAll(self,element):
        current = self.head
        count = 0
        location = []
        index = 0
        while current != None:
            if current.getData() == element:
                count += 1
                location.append(index)
            index +=1    
            current = current.getNext()
        print "%s is found %s time(s) at position(s)"  %  (element, count, location)

# 2c
    def insert(self, position, element):
        previous = None
        new = Node(element)
        if position > self.size():
            print "Out of range"
        elif position == 0:
            new.setNext(self.head)
            self.head = new

        else:
            while position:
                position = position -1
                previous = self.head
                self.head = self.head.getNext()
                previous.setNext(new)
                new.setNext(self.head)

# 2d
    def getIndex(self,index):
        current = self.head
        for i in range(index):
            current = current.getNext()
        if current != None:
            return current.getData()
        else:
            print "out of range"

    def popAtIndex(self,index):
        self.remove(self.getIndex(index))

        
# 2e
    def appendLast(self,element):
        current = self.head
        if current:
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(Node(element))
        else:
            self.head = Node(element)
            
                       


myList = LinkedList()
myList.add(500)
myList.add(100)
myList.add(200)
myList.add(300)
myList.add(500)
myList.add(400)
myList.add(500)
myList.add(500)
myList.add(600)








