class Node:
    def __init__(self, data: str):
        if not isinstance(data, str) or len(data) != 1:
            raise ValueError("Data must be a single character")
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0
    
    def length(self) -> int:
        return self._size
    
    def append(self, element: str) -> None:
        if not isinstance(element, str) or len(element) != 1:
            raise ValueError("Element must be a single character")
        
        new_node = Node(element)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
        self._size += 1
    
    def insert(self, element: str, index: int) -> None:
        if not isinstance(element, str) or len(element) != 1:
            raise ValueError("Element must be a single character")
        
        if index < 0 or index > self._size:
            raise IndexError(f"Index {index} out of range [0, {self._size}]")
        
        if index == self._size:
            self.append(element)
            return
        
        new_node = Node(element)
        
        if index == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            if self.tail is None:
                self.tail = new_node
        else:
            current = self._get_node_at_index(index)
            prev_node = current.prev
            
            new_node.prev = prev_node
            new_node.next = current
            prev_node.next = new_node
            current.prev = new_node
        
        self._size += 1
    
    def delete(self, index: int) -> str:
        if index < 0 or index >= self._size:
            raise IndexError(f"Index {index} out of range [0, {self._size-1}]")
        
        node_to_delete = self._get_node_at_index(index)
        data = node_to_delete.data
        
        if node_to_delete.prev:
            node_to_delete.prev.next = node_to_delete.next
        else:
            self.head = node_to_delete.next
        
        if node_to_delete.next:
            node_to_delete.next.prev = node_to_delete.prev
        else:
            self.tail = node_to_delete.prev
        
        self._size -= 1
        return data
    
    def deleteAll(self, element: str) -> None:
        if not isinstance(element, str) or len(element) != 1:
            raise ValueError("Element must be a single character")
        
        current = self.head
        while current:
            next_node = current.next
            if current.data == element:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                
                self._size -= 1
            current = next_node
    
    def get(self, index: int) -> str:
        if index < 0 or index >= self._size:
            raise IndexError(f"Index {index} out of range [0, {self._size-1}]")
        return self._get_node_at_index(index).data
    
    def clone(self):
        new_list = DoublyLinkedList()
        current = self.head
        while current:
            new_list.append(current.data)
            current = current.next
        return new_list
    
    def reverse(self) -> None:
        current = self.head
        while current:
            current.prev, current.next = current.next, current.prev
            current = current.prev
        
        self.head, self.tail = self.tail, self.head
    
    def findFirst(self, element: str) -> int:
        if not isinstance(element, str) or len(element) != 1:
            raise ValueError("Element must be a single character")
        
        current = self.head
        index = 0
        while current:
            if current.data == element:
                return index
            current = current.next
            index += 1
        return -1
    
    def findLast(self, element: str) -> int:
        if not isinstance(element, str) or len(element) != 1:
            raise ValueError("Element must be a single character")
        
        current = self.tail
        index = self._size - 1
        while current:
            if current.data == element:
                return index
            current = current.prev
            index -= 1
        return -1
    
    def clear(self) -> None:
        self.head = None
        self.tail = None
        self._size = 0
    
    def extend(self, elements) -> None:
        if not isinstance(elements, DoublyLinkedList):
            raise TypeError("Elements must be a DoublyLinkedList instance")
        
        current = elements.head
        while current:
            self.append(current.data)
            current = current.next
    
    def _get_node_at_index(self, index: int) -> Node:
        if index < 0 or index >= self._size:
            raise IndexError(f"Index {index} out of range [0, {self._size-1}]")
        
        if index < self._size // 2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self._size - 1 - index):
                current = current.prev
        
        return current
    
    def to_list(self) -> list:
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
    
    def __str__(self) -> str:
        return str(self.to_list())