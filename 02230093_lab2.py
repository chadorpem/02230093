# Task 1 
# Node class
class Node:
    def __init__(self, data):
        self.data = data      # store element
        self.next = None      # reference to next node


# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None      # first node
        self.tail = None      # last node (optional but used here)
        self.size = 0         # number of elements

    # Method to display list info
    def display_info(self):
        print("Created new LinkedList")
        print("Current size:", self.size)
        print("Head:", self.head)


# Main program
if __name__ == "__main__":
    # Create LinkedList object
    my_list = LinkedList()

    # Display initial state
    my_list.display_info()
    # Task 2
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    # Append
    def append(self, element):
        new_node = Node(element)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self._size += 1
        print(f"Appended {element} to the list")

    # Get
    def get(self, index):
        if index < 0 or index >= self._size:
            print("Index out of range")
            return

        current = self.head
        for _ in range(index):
            current = current.next

        print(f"Element at index {index}: {current.data}")

    # Set
    def set(self, index, element):
        if index < 0 or index >= self._size:
            print("Index out of range")
            return

        current = self.head
        for _ in range(index):
            current = current.next

        current.data = element
        print(f"Set element at index {index} to {element}")

    # Size
    def size(self):
        print(f"Current size: {self._size}")

    # Prepend
    def prepend(self, element):
        new_node = Node(element)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self._size += 1
        print(f"Prepend {element} to the list")

    # Print list
    def print_list(self):
        current = self.head
        result = []

        while current:
            result.append(str(current.data))
            current = current.next

        print("Print Linked list:[", " ".join(result), "]", sep="")


# Main program (Example Output)
if __name__ == "__main__":
    my_list = LinkedList()

    my_list.append(5)
    my_list.get(0)
    my_list.set(0, 10)
    my_list.get(0)
    my_list.size()
    my_list.prepend(10)
    my_list.append(5)
    my_list.print_list()