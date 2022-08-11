# from click import style
from src.start import *
# from colorama import Fore,Back,style


class Troop:
    def __init__(self, health, posX, posY, width, height, model, damage, alive, maxhealth, isAttacking):
        self.health = health
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height
        self.model = model
        self.damage = damage
        self.alive = alive
        self.maxhealth = maxhealth
        self.isAttacking = isAttacking

    def show(self):
        if(self.health > 50*(self.maxhealth/100)):
            self.pixel = Fore.GREEN
        elif(self.health > 20*(self.maxhealth/100)):
            self.pixel = Fore.YELLOW
        else:
            self.pixel = Fore.RED
        # self.pixel=Fore.WHITE
        for i in range(self.height):
            for j in range(self.width):
                # print(i)
                # self.pixel=Fore.WHITE
                grid[self.posX + i][self.posY + j] = self.pixel + self.model[i][j]
        self.pixel = Style.RESET_ALL
        # grid[0][0] = "H"
        # grid[0][1] = "e"
        # grid[0][2] = "a"
        # grid[0][3] = "l"
        # grid[0][4] = "t"
        # grid[0][5] = "h"
        # grid[0][6] = " "
        # grid[0][7] = "-"
        # grid[0][8] = " "
        # h = self.health
        # i = 9
        # # self.pixel = Style.RESET_ALL
        # while(h>=0):
        #     grid[0][i] = "+"
        #     i = i + 1
        #     h = h - 20

    def clear(self):
        for i in range(self.height):
            for j in range(self.width):
                grid[self.posX + i][self.posY + j] = " "

    def moveup(self):
        if(self.health > 50*(self.maxhealth/100)):
            self.pixel = Fore.GREEN
        elif(self.health > 20*(self.maxhealth/100)):
            self.pixel = Fore.YELLOW
        else:
            self.pixel = Fore.RED
        
        if(grid[self.posX][self.posY]==self.pixel + "l"):
            for i in range(self.height):
                for j in range(self.width):
                    grid[self.posX + i - 1][self.posY + j] =  self.model[i][j] + self.pixel
                    grid[self.posX + i][self.posY + j] = " "
            self.posX=self.posX-1
        elif (self.posX!=1 and (grid[self.posX - 1][self.posY]==" " or grid[self.posX - 1][self.posY]== self.pixel + "b" or grid[self.posX - 1][self.posY]== self.pixel + "a" or grid[self.posX - 1][self.posY]==self.pixel + "l")):
            for i in range(self.height):
                for j in range(self.width):
                    grid[self.posX + i - 1][self.posY + j] =  self.model[i][j] + self.pixel
                    grid[self.posX + i][self.posY + j] = " "
            self.posX=self.posX-1

    def movedown(self):
        # print(grid[self.posX + 1][self.posY])
        # print(grid[self.posX + 1][self.posY]==" ")
        # print(grid[self.posX + 1][self.posY]=="b")
        if(self.health > 50*(self.maxhealth/100)):
            self.pixel = Fore.GREEN
        elif(self.health > 20*(self.maxhealth/100)):
            self.pixel = Fore.YELLOW
        else:
            self.pixel = Fore.RED
        
        if(grid[self.posX][self.posY]==self.pixel + "l"):
            for i in range(self.height):
                for j in range(self.width):
                    grid[self.posX + i + 1][self.posY + j] =  self.model[i][j] + self.pixel
                    grid[self.posX + i][self.posY + j] = " "
            self.posX=self.posX+1
        elif (self.posX != 43 and (grid[self.posX + 1][self.posY]==" " or grid[self.posX + 1][self.posY]== self.pixel + "b" or grid[self.posX + 1][self.posY]==self.pixel + "a" or grid[self.posX + 1][self.posY]==self.pixel + "l")):
            # print("here")  
            for i in range(self.height):
                for j in range(self.width):
                    grid[self.posX + i + 1][self.posY + j] =  self.model[i][j] + self.pixel
                    grid[self.posX + i][self.posY + j] = " "
            self.posX=self.posX+1
            # print(self.posX)

    def moveleft(self):
        if(self.health > 50*(self.maxhealth/100)):
            self.pixel = Fore.GREEN
        elif(self.health > 20*(self.maxhealth/100)):
            self.pixel = Fore.YELLOW
        else:
            self.pixel = Fore.RED
        
        if(grid[self.posX][self.posY]==self.pixel + "l"):
            for i in range(self.height):
                for j in range(self.width):
                    grid[self.posX + i][self.posY + j - 1] =  self.model[i][j] + self.pixel
                    grid[self.posX + i][self.posY + j] = " "
            self.posY=self.posY-1
        elif (self.posY!=0 and (grid[self.posX][self.posY - 1]==" " or grid[self.posX][self.posY - 1]== self.pixel + "b" or grid[self.posX][self.posY - 1]== self.pixel + "a" or grid[self.posX][self.posY - 1]==self.pixel + "l")):
            for i in range(self.height):
                for j in range(self.width):
                    grid[self.posX + i][self.posY + j - 1] =  self.model[i][j] + self.pixel
                    grid[self.posX + i][self.posY + j] = " "
            self.posY=self.posY-1

    def moveright(self):
        # print(grid[self.posX][self.posY+1]==" ")
        # print(grid[self.posX][self.posY+1])
        # print(grid[self.posX][self.posY+1]== Fore.WHITE + 'b')
        # print("b" in grid[self.posX][self.posY + 1])
        if(self.health > 50*(self.maxhealth/100)):
            self.pixel = Fore.GREEN
        elif(self.health > 20*(self.maxhealth/100)):
            self.pixel = Fore.YELLOW
        else:
            self.pixel = Fore.RED

        if(grid[self.posX][self.posY]==self.pixel + "l"):
            for i in range(self.height):
                for j in range(self.width):
                    grid[self.posX + i][self.posY + j + 1] =  self.model[i][j] + self.pixel
                    grid[self.posX + i][self.posY + j] = " "
            self.posY=self.posY+1
        elif (self.posY!=172 and (grid[self.posX][self.posY + 1]== self.pixel + "b" or grid[self.posX][self.posY + 1]==" " or grid[self.posX][self.posY + 1]==self.pixel + "a" or grid[self.posX][self.posY + 1]==self.pixel + "l")):
            for i in range(self.height):
                for j in range(self.width):
                    grid[self.posX + i][self.posY + j + 1] =  self.model[i][j] + self.pixel
                    grid[self.posX + i][self.posY + j] = " "
            self.posY=self.posY+1


class barb(Troop):
    def __init__(self, health, posX, posY, width, height, model, damage, alive, maxhealth=30, isAttacking=False):
        super().__init__(health, posX, posY, width, height, model, damage, alive, maxhealth, isAttacking)

class arch(Troop):
    def __init__(self, health, posX, posY, width, height, model, damage, alive, maxhealth=15, isAttacking=False):
        super().__init__(health, posX, posY, width, height, model, damage, alive, maxhealth, isAttacking)

class loon(Troop):
    def __init__(self, health, posX, posY, width, height, model, damage, alive, maxhealth=30, isAttacking=False):
        super().__init__(health, posX, posY, width, height, model, damage, alive, maxhealth, isAttacking)
        
    


class bKing(Troop):
    def __init__(self, health, posX, posY, width, height, model, damage, alive, maxhealth=200, isAttacking=False):
        super().__init__(health, posX, posY, width, height, model, damage, alive, maxhealth, isAttacking)
        # self.alive = alive

class aQueen(Troop):
    def __init__(self, health, posX, posY, width, height, model, damage, alive, maxhealth=150, isAttacking=False):
        super().__init__(health, posX, posY, width, height, model, damage, alive, maxhealth, isAttacking)
        # self.alive = alive

    # def moveup(self):
    #     if self.posX!=1 and grid[self.posX - 1][self.posY]==" ":
    #         for i in range(self.height):
    #             for j in range(self.width):
    #                 grid[self.posX + i - 1][self.posY + j] =  grid[self.posX + i][self.posY + j]
    #                 grid[self.posX + i][self.posY + j] = " "
    #         self.posX=self.posX-1

    # def movedown(self):
    #     if self.posX!=43 and grid[self.posX + 1][self.posY]==" ":
    #         for i in range(self.height):
    #             for j in range(self.width):
    #                 grid[self.posX + i + 1][self.posY + j] =  grid[self.posX + i][self.posY + j]
    #                 grid[self.posX + i][self.posY + j] = " "
    #         self.posX=self.posX+1

    # def moveleft(self):
    #     if self.posY!=0 and grid[self.posX][self.posY - 1]==" ":
    #         for i in range(self.height):
    #             for j in range(self.width):
    #                 grid[self.posX + i][self.posY + j - 1] =  grid[self.posX + i][self.posY + j]
    #                 grid[self.posX + i][self.posY + j] = " "
    #         self.posY=self.posY-1

    # def moveright(self):
    #     if self.posY!=172 and grid[self.posX][self.posY + 1]==" ":
    #         for i in range(self.height):
    #             for j in range(self.width):
    #                 grid[self.posX + i][self.posY + j + 1] =  grid[self.posX + i][self.posY + j]
    #                 grid[self.posX + i][self.posY + j] = " "
    #         self.posY=self.posY+1

    # def attack(self,building):
    #     if self.posX == building.posX - 1:
    #         building.health = building.health - self.damage

    # def getX(self):
    #     return self.posX
    # def getY(self):
    #     return self.posY
    

    