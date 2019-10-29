import threading
import time

SPENDING_SPEED = 5
ALL_CUSTOMERS = []  # Todo: make this one Atomic


class Customer:
    def __init__(self, name, satisfaction):
        self.name = name
        self.satisfaction = satisfaction
        self.start_time = time.time()
        self.order_was_NOT_completed = True

    def time_elapased(self):
        return time.time() - self.start_time


def decrease_amount(speed):
    while True:
        time.sleep(speed)
        print("Thread name is:" + threading.current_thread().getName())
        for c in ALL_CUSTOMERS:
            if c.order_was_NOT_completed:
                c.satisfaction -= 1
                # print("start time for customer is: " + str(c.start_time))
                # print("Time elapsed: " + str(c.time_elapased()))


def complete_orders(customer_list: [Customer]) -> None:
    time.sleep(20)
    print("Thread name is:" + threading.current_thread().getName())
    for c in customer_list:
        c.order_was_NOT_completed = False


# Creating customers #
idan = Customer("Idan", 50)
guy = Customer("Guy Nir", 100000)
ALL_CUSTOMERS.append(idan)
ALL_CUSTOMERS.append(guy)

# Creating thread for decrease amount #
t1 = threading.Thread(target=decrease_amount,
                      args=(SPENDING_SPEED,))
t1.setName("decrease_amount-1")
t1.setDaemon(True)

t2 = threading.Thread(target=complete_orders,
                      args=(ALL_CUSTOMERS,))
t2.setName("Complete-orders")
t2.setDaemon(True)

# Make the thread start working #
t1.start()
t2.start()

# Run the game/ Logic#
while True:
    time.sleep(5)
    thread_name = threading.current_thread().getName()
    # print("Thread name: " + thread_name)
    sum_amount = 0

    for c in ALL_CUSTOMERS:
        print(c.name + " has satisfaction of: " + str(c.satisfaction))
        sum_amount += c.satisfaction

    ave = sum_amount / len(ALL_CUSTOMERS)
    print("ave satisfaction:" + str(ave))

# Todo check How to stop/kill the thread (decrease_amount-1)!
