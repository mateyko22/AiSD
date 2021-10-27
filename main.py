from typing import Any


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        tekst = ""
        pom = self.head
        while pom is not None:
            tekst += str(pom.data)
            pom = pom.next
            if pom is not None:
                tekst += " -> "
        return tekst

    def __len__(self):
        if self.head is None:
            return 0
        pom = self.head
        licznik = 0
        while pom is not None:
            pom = pom.next
            licznik += 1
        return licznik

    def push(self, value: Any) -> None:
        nowa_w = Node(value)
        nowa_w.next = self.head
        self.head = nowa_w

    def append(self, value: Any) -> None:
        nowa_w = Node(value)
        if self.head is None:
            self.head = nowa_w
            return
        pom = self.head
        while pom.next:
            pom = pom.next
        pom.next = nowa_w

    def node(self, at: int) -> None:
        wuwu = self.head
        for i in range(at):
            wuwu = wuwu.next
        return wuwu

    def insert(self, value: Any, after: Node) -> None:
        nowa_w = Node(value)
        nowa_w.next = after.next
        after.next = nowa_w

    def pop(self) -> Any:
        pom = self.head
        self.head = pom.next
        return pom.data

    def remove_last(self) -> Any:
        pom = self.head
        while pom.next.next is not None:
            pom = pom.next
        pom2 = pom.next.data
        pom.next = None
        return pom2

    def remove(self, after: Node) -> Any:
        if after.next is None:
            print("Wskazany wezel nie znajduje sie w liscie.")
            return
        else:
            temp = after.next
            after.next = after.next.next
            temp = None


list_ = LinkedList()

assert list_.head == None

list_.push(1)
list_.push(0)

assert str(list_) == '0 -> 1'

list_.append(9)
list_.append(10)

assert str(list_) == '0 -> 1 -> 9 -> 10'


middle_node = list_.node(at=1)

list_.insert(5, after=middle_node)

assert str(list_) == '0 -> 1 -> 5 -> 9 -> 10'


first_element = list_.node(at=0)
returned_first_element = list_.pop()

assert first_element.data == returned_first_element

last_element = list_.node(at=3)
returned_last_element = list_.remove_last()

assert last_element.data == returned_last_element
assert str(list_) == '1 -> 5 -> 9'

second_node = list_.node(at=1)
list_.remove(second_node)

assert str(list_) == '1 -> 5'

print(list_)
print(len(list_))


class Stack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    def __len__(self):
        return self.size

    def __str__(self):
        tekst = ""
        pom = self.head.next
        while pom is not None:
            tekst += str(pom.data)
            pom = pom.next
            if pom is not None:
                tekst += " \n"
        return tekst

    def push(self, element: Any) -> None:
        nowa_w = Node(element)
        nowa_w.next = self.head.next
        self.head.next = nowa_w
        self.size += 1

    def pop(self) -> Any:
        usun = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return usun.data


stack = Stack()
assert len(stack) == 0

stack.push(3)
stack.push(10)
stack.push(1)
assert len(stack) == 3

top_value = stack.pop()
assert top_value == 1
assert len(stack) == 2

print(stack)
print("liczba elementow stosu: ", len(stack))


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        tekst = ""
        pom = self.head
        while pom is not None:
            tekst += str(pom.data)
            pom = pom.next
            if pom is not None:
                tekst += ", "
        return tekst

    def __len__(self):
        return self.size

    def peek(self) -> Any:
        return self.head.data

    def enqueue(self, element: Any) -> None:
        pom = Node(element)
        if self.tail is None:
            self.head = pom
            self.tail = self.head
        else:
            self.tail.next = pom
            self.tail = self.tail.next
        self.size += 1

    def dequeue(self) -> None:
        pom = self.head
        self.head = self.head.next
        self.size -= 1
        return pom.data


queue = Queue()
assert len(queue) == 0

queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')
assert str(queue) == 'klient1, klient2, klient3'

client_first = queue.dequeue()

assert client_first == 'klient1'
assert str(queue) == 'klient2, klient3'
assert len(queue) == 2

