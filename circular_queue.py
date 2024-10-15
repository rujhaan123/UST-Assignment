class CircularQueue:
    def __init__(self, max_size=5):
        # Initialize the queue with an empty dictionary, set the maximum size, 
        # and use two indices to track the start and end positions.
        self.queue = {}
        self.max_size = max_size
        self.start = 0  # Index of the oldest element
        self.end = 0    # Index of where the new element will be added
        self.size = 0   # Number of elements currently in the queue

    def enqueue(self, element):
        # If the queue is full, we move the start index to the next position
        if self.size == self.max_size:
            # When queue is full, the oldest element will be overwritten, so move start
            self.start = (self.start + 1) % self.max_size
        else:
            # If the queue is not full, increase the size
            self.size += 1

        # Add the new element at the current 'end' position
        self.queue[self.end] = element

        # Move the 'end' index forward, wrapping around using modulo operation
        self.end = (self.end + 1) % self.max_size

    def display(self):
        # Display the current elements in the queue from 'start' to 'end'
        print("Queue state:")
        index = self.start  # Start displaying from the oldest element
        for _ in range(self.size):  # Loop through the number of elements in the queue
            print(self.queue[index], end=" ")
            index = (index + 1) % self.max_size  # Move to the next element, wrap around if needed
        print("\n")  # Print a new line at the end