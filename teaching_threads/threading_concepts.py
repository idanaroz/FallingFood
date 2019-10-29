import threading
import time

# Constants #
SPENDING_SPEED = 3
ALL_CUSTOMERS = []  # Todo: make this one Atomic


# Customer class #
class Customer:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        self.start_time = time.time()

    @staticmethod
    def decrease_amount(speed):
        while True:
            time.sleep(speed)
            print("Thread name is:" + threading.current_thread().getName())
            for customer in ALL_CUSTOMERS:
                print("start time for customer is: " + str(customer.start_time))
                print("Time elapsed: " + str(customer.time_elapased()))
                customer.amount -= 1

    def time_elapased(self):
        return time.time() - self.start_time


# Creating customers #
idan = Customer("Idan", 50)
guy = Customer("Guy Nir", 100000)
ALL_CUSTOMERS.append(idan)
ALL_CUSTOMERS.append(guy)

# Creating thread for decrease amount #
t = threading.Thread(target=Customer.decrease_amount,
                     args=(SPENDING_SPEED,))
t.setName("decrease_amount-1")
t.setDaemon(True)

# Make the thread start working #
t.start()

# Run the game/ Logic#
while True:
    time.sleep(5)
    thread_name = threading.current_thread().getName()
    print("Thread name: " + thread_name)
    for c in ALL_CUSTOMERS:
        print(c.name + " has amount of: " + str(c.amount))

    # print ( "The thread name is: " + t.getName())
    # print ( "The thread name is: " + str( t.isDaemon()))
