class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
    def __str__(self) -> str:
        return str(self.data)
    
class LinkedList:
    def __init__(self) -> None:
        self.head : Node = None
        self.length = 0
    
    def insert_head(self, data):
            old = self.head
            self.head = Node(data)
            self.head.next = old
            self.length += 1
    
    def add(self, data):
        if self.head:
            nodo = self.head
            while nodo.next:
                nodo = nodo.next
            
            nodo.next = Node(data)
        else:
            self.head = Node(data)
        self.length += 1
