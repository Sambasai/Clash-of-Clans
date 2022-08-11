from src.start import *


class Infrastructure:
    def __init__(self, health, posX, posY, width, height, model, alive):
        self.health = health
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height
        self.model = model
        self.alive = alive

    def show(self):
        if(self.health > 50):
            self.pixel = Fore.GREEN
        elif(self.health > 20):
            self.pixel = Fore.YELLOW
        else:
            self.pixel = Fore.RED

        for i in range(self.height):
            for j in range(self.width):
                # print(i)
                grid[self.posX + i][self.posY + j] = self.pixel + self.model[i][j]
        self.pixel = Style.RESET_ALL

    def clear(self):
        for i in range(self.height):
            for j in range(self.width):
                grid[self.posX + i][self.posY + j] = " "


class hut(Infrastructure):
    def __init__(self, health, posX, posY, width, height, model, alive):
        super().__init__(health, posX, posY, width, height, model, alive)


class townHall(Infrastructure):
    def __init__(self, health, posX, posY, width, height, model, alive):
        super().__init__(health, posX, posY, width, height, model, alive)


class cannon(Infrastructure):
    def __init__(self, health, posX, posY, width, height, model, rng, damage, alive):
        super().__init__(health, posX, posY, width, height, model, alive)
        self.rng = rng
        self.damage = damage

    def changecolor(self):
        self.pixel = Fore.BLUE
        for i in range(self.height-1):
            for j in range(self.width):
                # print(i)
                grid[self.posX + i][self.posY + j] = self.pixel + self.model[i][j]
        self.pixel = Style.RESET_ALL

class wizard(Infrastructure):
    def __init__(self, health, posX, posY, width, height, model, rng, damage, alive):
        super().__init__(health, posX, posY, width, height, model, alive)
        self.rng = rng
        self.damage = damage

    def changecolor(self):
        self.pixel = Fore.BLUE
        for i in range(self.height-1):
            for j in range(self.width):
                # print(i)
                grid[self.posX + i][self.posY + j] = self.pixel + self.model[i][j]
        self.pixel = Style.RESET_ALL


class wall(Infrastructure):
    def __init__(self, health, posX, posY, width, height, model, alive):
        super().__init__(health, posX, posY, width, height, model, alive)
