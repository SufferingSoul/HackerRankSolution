import math
import os
import random
import re
import sys


class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node


def print_doubly_linked_list(node, sep):
    while node:
        print(str(node.data))

        node = node.next

        if node:
            print(sep)


def sortedInsert(head, data):
    current_node = head
    new_node = DoublyLinkedListNode(data)
    while current_node.next and current_node.data < data:
        current_node = current_node.next

    if current_node.data < data:
        current_node.next = new_node
        new_node.prev = current_node
    else:
        new_node.prev = current_node.prev
        if current_node.prev:
            current_node.prev.next = new_node
        else:
            head = new_node
        current_node.prev = new_node
        new_node.next = current_node
    return head


def reverse(head):
    current_node = head
    if current_node is None:
        return current_node
    while current_node.next:
        temp = current_node.next
        current_node.next = current_node.prev
        current_node.prev = temp
        current_node = current_node.prev
    current_node.next = current_node.prev
    current_node.prev = None
    return current_node


if __name__ == '__main__':
    inputStr = open("testCase/testCase.txt")

    t = int(inputStr.readline())

    for t_itr in range(t):
        llist_count = int(inputStr.readline())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(inputStr.readline())
            llist.insert_node(llist_item)

        llist1 = reverse(llist.head)

        print_doubly_linked_list(llist1, " ")
