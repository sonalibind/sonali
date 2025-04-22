import threading
import time
import random

# Class to handle the Dining Philosophers problem
class DiningPhilosophers:
    def __init__(self, num_philosophers):
        self.num = num_philosophers
        # Each chopstick is represented as a Semaphore (1 means available)
        self.chopsticks = [threading.Semaphore(1) for _ in range(num_philosophers)]
        # Semaphore to limit the number of philosophers eating at the same time (N-1 to prevent deadlock)
        self.max_diners = threading.Semaphore(num_philosophers - 1)

    # Method to pick up chopsticks (left and right)
    def pick_up_chopsticks(self, philosopher):
        self.max_diners.acquire()  # Ensure at most (N-1) philosophers eat at once
        self.chopsticks[philosopher].acquire()  # Pick up left chopstick
        self.chopsticks[(philosopher + 1) % self.num].acquire()  # Pick up right chopstick
        print(f"Philosopher {philosopher} is eating.")

    # Method to put down chopsticks after eating
    def put_down_chopsticks(self, philosopher):
        self.chopsticks[philosopher].release()  # Release left chopstick
        self.chopsticks[(philosopher + 1) % self.num].release()  # Release right chopstick
        self.max_diners.release()  # Allow another philosopher to eat
        print(f"Philosopher {philosopher} has finished eating.")

# Function representing a philosopher's behavior
def philosopher_task(philosopher, table):
    while True:
        print(f"Philosopher {philosopher} is thinking.")
        time.sleep(random.uniform(0.5, 2))  # Simulate thinking time
        table.pick_up_chopsticks(philosopher)  # Try to eat
        time.sleep(random.uniform(0.5, 2))  # Simulate eating time
        table.put_down_chopsticks(philosopher)  # Done eating

# Main execution
if __name__ == "__main__":
    num_philosophers = 5  # Number of philosophers
    table = DiningPhilosophers(num_philosophers)  # Create the dining table
    philosophers = []

    # Create and start a thread for each philosopher
    for i in range(num_philosophers):
        t = threading.Thread(target=philosopher_task, args=(i, table))
        philosophers.append(t)
        t.start()

    # Wait for all threads to finish (will run infinitely in this case)
    for t in philosophers:
        t.join()




# ALGORITHM:
# ● Define the number of philosophers
# ● Declare one thread per philosopher
# ● Declare one semaphore (represent chopsticks) per philosopher
# ● When a philosopher is hungry
# ○ See if chopsticks on both sides are free
# ○ Acquire both chopsticks
# ○ eat
# ○ restore the chopsticks
# ● If chopsticks aren’t free wait till they are available



