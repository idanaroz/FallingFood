import time
import turtle

wn = turtle.Screen()


class Order:
    def __init__(self, amount_of_pancakes, order_number):
        self.amount_of_pancakes = amount_of_pancakes
        self.order_number = order_number
        self.creation_time = time.time()
        self.constant_y_change = 100  # how much the orders are spaced out by
        self.order_complete = True
        self.turtle = None
        self.customer_rating = 5  # rating out of 5, 2 main factors: amount of time, amount of pancakes,
        # add later: different feelings for each customer

        wn.ontimer(self.decrease_rating, 5000)

    def decrease_rating(self):
        self.customer_rating -= 1
