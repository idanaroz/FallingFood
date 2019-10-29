import turtle

wn = turtle.Screen()


class Chef:
    def __init__(self, speed):
        self.turtle = turtle.Turtle()
        self.speed = speed


def init_chef():
    chef_img = r"/Users/gnir/PycharmProjects/FallingFood/Images/chef.gif"
    wn.addshape(chef_img)
    chef = Chef(20)
    chef.turtle.shape(chef_img)
    chef.turtle.resizemode("auto")
    chef.turtle.penup()
    chef.turtle.setposition(100, -325)
    return chef



class Game:
    def __init__(self):
        self.freeze = False
        self.game_over = False
        self.pancake_list = []
        self.standard_rating = 1  # this means the standard rating that the player needs to get to. 1-5
        self.chef_destination = 100
        self.chef = init_chef()


        #  Todo: orders,

    def unfreeze(self):
        self.freeze = False  # Todo(Idan): Fix this logic so no errors will NOT be seen
        diff = (self.chef_destination) - self.chef.turtle.xcor()
        for pancake in self.pancake_list:
            turtle = pancake.turtle
            if pancake.on_plate:
                turtle.setx(turtle.xcor() + diff)
        self.chef.turtle.setx(self.chef_destination)

    def freeze_game(self):
        self.freeze = True
        wn.ontimer(self.unfreeze, 4000)

    # def freeze(self):
    #     game.pancake_list
