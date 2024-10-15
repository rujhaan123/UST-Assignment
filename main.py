import threading
from circular_queue import CircularQueue
from frequency_words import word_frequency
from passcheck import validate_passwords

# Create a lock object
print_lock = threading.Lock()

# Function to handle Circular Queue operations
def run_circular_queue():
    # Read input from file
    with open('input_files/circular_queue_input.txt', 'r') as f:
        elements = list(map(int, f.read().split(',')))

    cq = CircularQueue()  # Create circular queue
    for element in elements:
        cq.enqueue(element)

    # Acquire the lock before printing
    with print_lock:
        cq.display()  # Display the final queue state

# Function to handle Word Frequency analysis
def run_word_frequency():
    # Read input from file
    with open('input_files/frequency_words_input.txt', 'r') as f:
        text = f.read()

    frequencies = word_frequency(text)  # Run word frequency algorithm

    # Acquire the lock before printing
    with print_lock:
        print("\nWord Frequency Analysis:")
        for word, count in frequencies.items():
            print(f"{word}: {count}")

# Function to handle Password Validation
def run_password_validation():
    # Read input from file
    with open('input_files/passcheck_input.txt', 'r') as f:
        input_passwords = f.read()

    valid_passwords = validate_passwords(input_passwords)  # Run password validation

    # Acquire the lock before printing
    with print_lock:
        print("\nValid passwords:", valid_passwords)

def main():
    # Creating threads for each algorithm
    circular_queue_thread = threading.Thread(target=run_circular_queue)
    word_frequency_thread = threading.Thread(target=run_word_frequency)
    password_validation_thread = threading.Thread(target=run_password_validation)

    # Start the threads
    circular_queue_thread.start()
    word_frequency_thread.start()
    password_validation_thread.start()

    # Wait for all threads to complete
    circular_queue_thread.join()
    word_frequency_thread.join()
    password_validation_thread.join()

    print("\nAll tasks completed.")

if __name__ == "__main__":
    main()
