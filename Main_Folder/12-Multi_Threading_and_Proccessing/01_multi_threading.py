### Multithreading 
## when to use Mutli threading 
### I/O bound tasks: Tasks that spend more time waiting for input/output operations (like file reading/writing, network requests)
### Concurrent execution: when you want to improve the throughput of you application by performing multiple operation concurrently



# Importing threading to run functions at the same time (parallel)
# Importing time to create delays and measure time
import threading
import time 

# This function prints numbers from 0 to 4, with a 2-second delay between each
def print_numbers():
    for i in range(5):
        time.sleep(2)  # wait for 2 seconds
        print(f"Number: {i}")  # print current number

# This function prints letters from 'a' to 'e', with a 2-second delay between each
def print_letters():
    for letter in 'abcde':
        time.sleep(2)  # wait for 2 seconds
        print(f"Letter: {letter}")  # print current letter

# Create two threads, one for numbers and one for letters
t1 = threading.Thread(target=print_numbers)  # Thread to run print_numbers()
t2 = threading.Thread(target=print_letters)  # Thread to run print_letters()

# Record the current time before starting the threads
t = time.time()    

# Start both threads (they will run at the same time)
t1.start()
t2.start()

# Wait for both threads to complete before moving to the next line
t1.join()
t2.join()

# Calculate how much time it took to finish both threads
finished_time = time.time() - t
print(finished_time)  # Print the total time taken

