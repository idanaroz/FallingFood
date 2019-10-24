class Game:
    def __init__(self):
        self.freeze = False
        self.game_over = False
        self.pancake_list = []
        self.standard_rating = 1  # this means the standard rating that the player needs to get to. 1-5
        self.chef_destination = 100
        #  Todo: orders,

    def unfreeze(self):
        game.freeze = False  # Todo(Idan): Fix this logic so no errors will NOT be seen
        diff = (self.chef_destination) - chef.xcor()
        for pancake in game.pancake_list:
            turtle = pancake.turtle
            if pancake.on_plate:
                turtle.setx(turtle.xcor() + diff)
        chef.setx(self.chef_destination)

    def freeze_game(self):
        game.freeze = True
        wn.ontimer(self.unfreeze, 4000)

    # def freeze(self):
    #     game.pancake_list
