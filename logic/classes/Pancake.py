class Pancake:

    def __init__(self, turtle, time_delay):
        self.turtle = turtle
        self.time_delay_counter = time_delay
        self.on_plate = False

    def get_time_delay_counter(self):
        return self.time_delay_counter

    def get_turtle(self):
        return turtle  # Todo(idan): fix to self.turtle

    def set_time_delay_counter(self, new_int_value):
        self.time_delay_counter = new_int_value
        return self
