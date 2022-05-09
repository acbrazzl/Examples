#! /usr/bin/python3
import argparse

class Node:

    def __init__(self, letter):
        self.letter = letter
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def printList(self):
        tmp = self.head
        while(tmp):
            print (tmp.letter,end = "")
            tmp = tmp.next
    
    def append(self, letter):
        n = Node(letter)
        if self.head is None:
            self.head = n
            return
        last = self.head
        #walk list until end is found, O(n)
        while (last.next):
            last = last.next
        #stitch new node in!
        last.next = n



def main(args):
    if(args.string is not None): print(args.string)
    else:
        print("Doot Doot!")
    
    print("Now using pre-populated Linked List:")
    llist = LinkedList()
    llist.head = Node('D')
    second = Node('o')
    third = Node('o')
    fourth = Node('t')
    fifth = Node('!')
    llist.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth

    llist.printList()
    print("") #newLine hack
    
    if(args.string is not None): 
        print("Now printing provided text with linked list: ")
        llist_second = LinkedList()
        for i,s in enumerate(args.string):
            llist_second.append(args.string[i])
        llist_second.printList()
        print("") #newLine hack

if __name__ == "__main__":
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('-s','--string',type=str,help="String to print")
    args = my_parser.parse_args()
    main(args)