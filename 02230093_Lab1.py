class CustomList:

    def __init__(self):
        # Default capacity
        self.capacity = 10
        
        # Underlying array
        self.elements = [None] * self.capacity
        
        # Current size
        self.current_size = 0
        
        print("Created new CustomList with capacity:", self.capacity)
        print("Current size:", self.current_size)

    # Append element to the end
    def append(self, element):
        if self.current_size < self.capacity:
            self.elements[self.current_size] = element
            self.current_size += 1
            print(f"Appended {element} to the list")
        else:
            print("List is full")

    # Get element at index
    def get(self, index):
        if 0 <= index < self.current_size:
            print(f"Element at index {index}: {self.elements[index]}")
            return self.elements[index]
        else:
            print("Index out of range")

    # Set element at index
    def set(self, index, element):
        if 0 <= index < self.current_size:
            self.elements[index] = element
            print(f"Set element at index {index} to {element}")
        else:
            print("Index out of range")

    # Return current size
    def size(self):
        print("Current size:", self.current_size)
        return self.current_size


# Testing the CustomList
my_list = CustomList()

my_list.append(5)
my_list.get(0)
my_list.set(0, 10)
my_list.get(0)
my_list.size()