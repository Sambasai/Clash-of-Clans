# from src.prnt import *
from src.start import *
from src.inp import *
from src.infra import *
# from src.townhall import *
# from src.Hut import *
# from src.defenses import *
# from src.wall import *
from src.troops import *
from src.spell import *
# from src.bking import *
import os
# from os import system, name

from time import sleep


def clear():
    _ = os.system('clear')


# for i in range(len(objects)):
#     objects[i].show()

# bking_model[0][0] = "K"
# King = bKing(200, 10, 30, 1, 1, bking_model, 20, False)
# troops.append(King)
# Queen = aQueen(150, 10, 30, 1, 1, aqueen_model, 15, False)
# troops.append(Queen)
# for i in range(len(objects)):
#     objects[i].show()
objects = []
walls = []
defenses = []
troops = []
# bking[0].showtroop()

t = 0
dir = ""
rageflag = 0.1
gameflag = 0
level = 1
heroflag = 0
f = 0
axeX = 0
axeY = 0

while True:
    _inp = Input()
    ip = _inp.get_parsed_input(rageflag)
    if(f == 0):
        print(r"     _____ _           _              __   _____ _    ")
        print(r"    /  __ \ |         | |            / _| /  __ \ |   ")
        print(r"    | /  \/ | __ _ ___| |__     ___ | |_  | /  \/ | __ _ _ __  ___")
        print(r"    | |   | |/ _` / __| '_ \   / _ \|  _| | |   | |/ _` | '_ \/ __|")
        print(r"    | \__/\ | (_| \__ \ | | | | (_) | |   | \__/\ | (_| | | | \__ \ ")
        print(r"    \ ____/_|\__,_|___/_| |_|  \___/|_|    \____/_|\__,_|_| |_|___/")

        print()
        if(level == 1):
            # grid = [[" " for i in range(173)] for j in range(44)]
            os.system('aplay -q ./snd/sounds/open.wav')
            objects = []
            walls = []
            defenses = []
            troops = []
            bcount = 0
            acount = 0
            lcount = 0

            defenses.append(cannon(100, 18, 90, 3, 2, cannon_model, 5, 5, True))
            defenses.append(cannon(100, 28, 60, 3, 2, cannon_model, 5, 5, True))
            defenses.append(wizard(100, 25, 70, 3, 3, wizard_model, 5, 5, True))
            defenses.append(wizard(100, 21, 92, 3, 3, wizard_model, 5, 5, True))

            objects.append(hut(100, 18, 70, 3, 3, hut_model, True));
            objects.append(hut(100, 21, 73, 3, 3, hut_model, True));
            objects.append(hut(100, 20, 100, 3, 3, hut_model, True));
            objects.append(hut(100, 22, 60, 3, 3, hut_model, True));
            objects.append(hut(100, 26, 90, 3, 3, hut_model, True));
            objects.append(hut(100, 30, 75, 3, 3, hut_model, True));

            walls.append(wall(100, 22, 79, 1, 1, wall_model, True))
            walls.append(wall(100, 22, 80, 1, 1, wall_model, True))
            walls.append(wall(100, 22, 81, 1, 1, wall_model, True))
            walls.append(wall(100, 22, 82, 1, 1, wall_model, True))
            walls.append(wall(100, 22, 83, 1, 1, wall_model, True))
            walls.append(wall(100, 22, 84, 1, 1, wall_model, True))
            walls.append(wall(100, 26, 79, 1, 1, wall_model, True))
            walls.append(wall(100, 26, 80, 1, 1, wall_model, True))
            walls.append(wall(100, 26, 81, 1, 1, wall_model, True))
            walls.append(wall(100, 26, 82, 1, 1, wall_model, True))
            walls.append(wall(100, 26, 83, 1, 1, wall_model, True))
            walls.append(wall(100, 26, 84, 1, 1, wall_model, True))
            walls.append(wall(100, 23, 79, 1, 1, wall_model, True))
            walls.append(wall(100, 24, 79, 1, 1, wall_model, True))
            walls.append(wall(100, 25, 79, 1, 1, wall_model, True))
            walls.append(wall(100, 23, 84, 1, 1, wall_model, True))
            walls.append(wall(100, 24, 84, 1, 1, wall_model, True))
            walls.append(wall(100, 25, 84, 1, 1, wall_model, True))

            objects.append(townHall(100, 23, 80, 4, 3, townHall_model, True));

            King = bKing(200, 10, 30, 1, 1, bking_model, 20, False)
            troops.append(King)
            Queen = aQueen(150, 10, 30, 1, 1, aqueen_model, 15, False)
            troops.append(Queen)

        elif(level == 2):
            # grid = [[" " for i in range(173)] for j in range(44)]
            for i in range(44):
                for j in range(173):
                    # print(grid[i][j], end="")
                    grid[i][j] = " "
                print("")
            # grid = []
            objects = []
            walls = []
            defenses = []
            troops=[]
            bcount = 0
            acount = 0
            lcount = 0

            defenses.append(cannon(100, 18, 90, 3, 2, cannon_model, 5, 5, True))
            defenses.append(cannon(100, 28, 60, 3, 2, cannon_model, 5, 5, True))
            defenses.append(cannon(100, 26, 90, 3, 2, cannon_model, 5, 5, True))
            defenses.append(wizard(100, 25, 70, 3, 3, wizard_model, 5, 5, True))
            defenses.append(wizard(100, 21, 92, 3, 3, wizard_model, 5, 5, True))
            defenses.append(wizard(100, 28, 83, 3, 3, wizard_model, 5, 5, True))

            objects.append(hut(100, 18, 70, 3, 3, hut_model, True));
            objects.append(hut(100, 21, 73, 3, 3, hut_model, True));
            objects.append(hut(100, 20, 100, 3, 3, hut_model, True));
            objects.append(hut(100, 22, 60, 3, 3, hut_model, True));
            objects.append(hut(100, 27, 95, 3, 3, hut_model, True));
            objects.append(hut(100, 30, 75, 3, 3, hut_model, True));

            walls.append(wall(100, 22, 79, 1, 1, wall_model, True))
            walls.append(wall(100, 22, 80, 1, 1, wall_model, True))
            walls.append(wall(100, 22, 81, 1, 1, wall_model, True))
            walls.append(wall(100, 22, 82, 1, 1, wall_model, True))
            walls.append(wall(100, 22, 83, 1, 1, wall_model, True))
            walls.append(wall(100, 22, 84, 1, 1, wall_model, True))
            walls.append(wall(100, 26, 79, 1, 1, wall_model, True))
            walls.append(wall(100, 26, 80, 1, 1, wall_model, True))
            walls.append(wall(100, 26, 81, 1, 1, wall_model, True))
            walls.append(wall(100, 26, 82, 1, 1, wall_model, True))
            walls.append(wall(100, 26, 83, 1, 1, wall_model, True))
            walls.append(wall(100, 26, 84, 1, 1, wall_model, True))
            walls.append(wall(100, 23, 79, 1, 1, wall_model, True))
            walls.append(wall(100, 24, 79, 1, 1, wall_model, True))
            walls.append(wall(100, 25, 79, 1, 1, wall_model, True))
            walls.append(wall(100, 23, 84, 1, 1, wall_model, True))
            walls.append(wall(100, 24, 84, 1, 1, wall_model, True))
            walls.append(wall(100, 25, 84, 1, 1, wall_model, True))

            objects.append(townHall(100, 23, 80, 4, 3, townHall_model, True));

            King = bKing(200, 10, 30, 1, 1, bking_model, 20, False)
            troops.append(King)
            Queen = aQueen(150, 10, 30, 1, 1, aqueen_model, 15, False)
            troops.append(Queen)

            for i in range(44):
                for j in range(173):
                    print(grid[i][j], end="")
                print("")

        elif(level == 3):
            # grid = [[" " for i in range(173)] for j in range(44)]

            for i in range(44):
                for j in range(173):
                    # print(grid[i][j], end="")
                    grid[i][j] = " "
                print("")

            objects = []
            walls = []
            defenses = []
            troops=[]
            bcount = 0
            acount = 0
            lcount = 0

            defenses.append(cannon(100, 18, 90, 3, 2, cannon_model, 5, 5, True))
            defenses.append(cannon(100, 28, 60, 3, 2, cannon_model, 5, 5, True))
            defenses.append(cannon(100, 26, 90, 3, 2, cannon_model, 5, 5, True))
            defenses.append(cannon(100, 18, 60, 3, 2, cannon_model, 5, 5, True))
            defenses.append(wizard(100, 25, 70, 3, 3, wizard_model, 5, 5, True))
            defenses.append(wizard(100, 21, 92, 3, 3, wizard_model, 5, 5, True))
            defenses.append(wizard(100, 28, 83, 3, 3, wizard_model, 5, 5, True))
            defenses.append(wizard(100, 18, 80, 3, 3, wizard_model, 5, 5, True))

            objects.append(hut(100, 18, 70, 3, 3, hut_model, True));
            objects.append(hut(100, 21, 73, 3, 3, hut_model, True));
            objects.append(hut(100, 20, 100, 3, 3, hut_model, True));
            objects.append(hut(100, 22, 60, 3, 3, hut_model, True));
            objects.append(hut(100, 27, 95, 3, 3, hut_model, True));
            objects.append(hut(100, 30, 75, 3, 3, hut_model, True));

            walls.append(wall(100, 22, 79, 1, 1, wall_model, True))
            walls.append(wall(100, 22, 80, 1, 1, wall_model, True))
            walls.append(wall(100, 22, 81, 1, 1, wall_model, True))
            walls.append(wall(100, 22, 82, 1, 1, wall_model, True))
            walls.append(wall(100, 22, 83, 1, 1, wall_model, True))
            walls.append(wall(100, 22, 84, 1, 1, wall_model, True))
            walls.append(wall(100, 26, 79, 1, 1, wall_model, True))
            walls.append(wall(100, 26, 80, 1, 1, wall_model, True))
            walls.append(wall(100, 26, 81, 1, 1, wall_model, True))
            walls.append(wall(100, 26, 82, 1, 1, wall_model, True))
            walls.append(wall(100, 26, 83, 1, 1, wall_model, True))
            walls.append(wall(100, 26, 84, 1, 1, wall_model, True))
            walls.append(wall(100, 23, 79, 1, 1, wall_model, True))
            walls.append(wall(100, 24, 79, 1, 1, wall_model, True))
            walls.append(wall(100, 25, 79, 1, 1, wall_model, True))
            walls.append(wall(100, 23, 84, 1, 1, wall_model, True))
            walls.append(wall(100, 24, 84, 1, 1, wall_model, True))
            walls.append(wall(100, 25, 84, 1, 1, wall_model, True))

            objects.append(townHall(100, 23, 80, 4, 3, townHall_model, True));

            King = bKing(200, 10, 30, 1, 1, bking_model, 20, False)
            troops.append(King)
            Queen = aQueen(150, 10, 30, 1, 1, aqueen_model, 15, False)
            troops.append(Queen)


        # os.system('aplay -q ./snd/sounds/open.wav')
        # print("Click on P to play!")
        print("Enter 1 for King and 2 for queen: ")
        # print("Enter level you want to play: ")
        f = 2
    elif(f == 2 and (ip == "queen" or ip == "king")):
        f = 1
        if(ip == "king"):
            heroflag = 1
            King.alive = True
        else:
            heroflag = 2
            Queen.alive = True
    elif(f == 1):
        clear()
        # for i in range(len(objects)):
        #     objects[i].show()
        # bking[0].show()
        t = t + rageflag
        # print(t)
        for i in range(173):
            grid[0][i] = " "
        for i in range(len(objects)):
            if(objects[i].health <= 0):
                objects[i].clear()
                objects[i].alive = False
        for i in range(len(objects)):
            if(objects[i].alive):
                objects[i].show()
        for i in range(len(defenses)):
            if(defenses[i].health <= 0):
                defenses[i].clear()
                defenses[i].alive = False
        for i in range(len(defenses)):
            if(defenses[i].alive):
                defenses[i].show()
        for i in range(len(walls)):
            if(walls[i].health <= 0):
                walls[i].clear()
                walls[i].alive = False
        for i in range(len(walls)):
            if(walls[i].alive):
                walls[i].show()
        for i in range(1, len(troops)):
            if(troops[i].health <= 0):
                troops[i].clear()
                troops[i].alive = False
        for i in range(1, len(troops)):
            if(troops[i].alive):
                troops[i].show()

        if(heroflag == 1):
            King.show()
            h = King.health
        elif(heroflag == 2):
            Queen.show()
            h = Queen.health
        grid[0][0] = "H"
        grid[0][1] = "e"
        grid[0][2] = "a"
        grid[0][3] = "l"
        grid[0][4] = "t"
        grid[0][5] = "h"
        grid[0][6] = " "
        grid[0][7] = "-"
        grid[0][8] = " "
        i = 9
        # self.pixel = Style.RESET_ALL
        while(h > 0):
            grid[0][i] = "+"
            i = i + 1
            h = h - 20
        if(King.health <= 0):
            King.alive = False
        if(Queen.health <= 0):
            Queen.alive = False
        if(ip == "up"):
            dir = "up"
            if(King.alive):
                King.moveup()
            elif(Queen.alive):
                Queen.moveup()
        elif(ip == "down"):
            dir = "down"
            if(King.alive):
                King.movedown()
            elif(Queen.alive):
                Queen.movedown()
        elif(ip == "left"):
            dir = "left"
            if(King.alive):
                King.moveleft()
            elif(Queen.alive):
                Queen.moveleft()
        elif(ip == "right"):
            dir = "right"
            if(King.alive):
                King.moveright()
            elif(Queen.alive):
                Queen.moveright()
        elif(ip == "space"):
            # flag = 0
            if(King.alive):
                for i in range(len(objects)):
                    # print(objects[i].posX)
                    if(objects[i].alive and (King.posX >= objects[i].posX and King.posX < objects[i].posX + objects[i].height)):
                        if(King.posY + 1 == objects[i].posY):
                            objects[i].health = objects[i].health - King.damage
                            break

                for i in range(len(defenses)):
                    if(defenses[i].alive and (King.posX >= defenses[i].posX and King.posX < defenses[i].posX + defenses[i].height)):
                        if(King.posY + 1 == defenses[i].posY):
                            defenses[i].health = defenses[i].health - King.damage
                            break

                for i in range(len(walls)):
                    if(walls[i].alive and (King.posX >= walls[i].posX and King.posX < walls[i].posX + walls[i].height)):
                        if(King.posY + 1 == walls[i].posY):
                            walls[i].health = walls[i].health - King.damage
                            break
            elif(Queen.alive):
                for i in range(len(objects)):
                    if(objects[i].alive):
                        if(dir == "down" and abs(objects[i].posX-Queen.posX-8) <= 2 and abs(objects[i].posY-Queen.posY) <= 2):
                            objects[i].health = objects[i].health - Queen.damage
                            break
                        elif(dir == "up" and abs(objects[i].posX-Queen.posX+8) <= 2 and abs(objects[i].posY-Queen.posY) <= 2):
                            objects[i].health = objects[i].health - Queen.damage
                            break
                        elif(dir == "right" and abs(objects[i].posX-Queen.posX) <= 2 and abs(objects[i].posY-Queen.posY-8) <= 2):
                            objects[i].health = objects[i].health - Queen.damage
                            break
                        elif(dir=="left" and abs(objects[i].posX-Queen.posX) <= 2 and abs(objects[i].posY-Queen.posY+8) <= 2):
                            objects[i].health = objects[i].health - Queen.damage
                            break
                for i in range(len(defenses)):
                    if(defenses[i].alive):
                        if(dir == "down" and abs(defenses[i].posX-Queen.posX-8) <= 2 and abs(defenses[i].posY-Queen.posY) <= 2):
                            defenses[i].health = defenses[i].health - Queen.damage
                            break
                        elif(dir == "up" and abs(defenses[i].posX-Queen.posX+8) <= 2 and abs(defenses[i].posY-Queen.posY) <= 2):
                            defenses[i].health = defenses[i].health - Queen.damage
                            break
                        elif(dir == "right" and abs(defenses[i].posX-Queen.posX) <= 2 and abs(defenses[i].posY-Queen.posY-8) <= 2):
                            defenses[i].health = defenses[i].health - Queen.damage
                            break
                        elif(dir=="left" and abs(defenses[i].posX-Queen.posX) <= 2 and abs(defenses[i].posY-Queen.posY+8) <= 2):
                            defenses[i].health = defenses[i].health - Queen.damage
                            break
                for i in range(len(walls)):
                    if(walls[i].alive):
                        if(dir == "down" and abs(walls[i].posX-Queen.posX-8) <= 2 and abs(walls[i].posY-Queen.posY) <= 2):
                            walls[i].health = walls[i].health - Queen.damage
                            break
                        elif(dir == "up" and abs(walls[i].posX-Queen.posX+8) <= 2 and abs(walls[i].posY-Queen.posY) <= 2):
                            walls[i].health = walls[i].health - Queen.damage
                            break
                        elif(dir == "right" and abs(walls[i].posX-Queen.posX) <= 2 and abs(walls[i].posY-Queen.posY-8) <= 2):
                            walls[i].health = walls[i].health - Queen.damage
                            break
                        elif(dir=="left" and abs(walls[i].posX-Queen.posX) <= 2 and abs(walls[i].posY-Queen.posY+8) <= 2):
                            walls[i].health = walls[i].health - Queen.damage
                            break
                            

        elif(ip == "axe"):
            if(King.alive):
                for i in range(len(objects)):
                    if(objects[i].alive and ((King.posX-objects[i].posX)**2 + (King.posY-objects[i].posY)**2) <= 25):
                        objects[i].health = objects[i].health - King.damage
                        break
                for i in range(len(defenses)):
                    if(defenses[i].alive and ((King.posX-defenses[i].posX)**2 + (King.posY-defenses[i].posY)**2) <= 25):
                        defenses[i].health = defenses[i].health - King.damage
                        break
                for i in range(len(walls)):
                    if(walls[i].alive and ((King.posX-walls[i].posX)**2 + (King.posY-walls[i].posY)**2) <= 25):
                        walls[i].health = walls[i].health - King.damage
                        break
            elif(Queen.alive and t > 1):
                t = 0
                # axeX = 0
                # axeY = 0
                if(dir == "down"):
                    axeX = Queen.posX + 16
                    axeY = Queen.posY
                elif(dir == "up"):
                    axeX = Queen.posX - 16
                    axeY = Queen.posY
                elif(dir == "right"):
                    axeX = Queen.posX
                    axeY = Queen.posY + 16
                elif(dir == "left"):
                    axeX = Queen.posX
                    axeY = Queen.posY - 16
                # print(axeX, axeY)

        if(abs(t-1) < 0.01):
            # print(axeX, axeY)
            for i in range(len(objects)):
                if(objects[i].alive and (abs(axeX-objects[i].posX)<=4 and abs(axeY-objects[i].posY)<=4)):
                    objects[i].health = objects[i].health - Queen.damage
                    # break
            for i in range(len(defenses)):
                if(defenses[i].alive and (abs(axeX-defenses[i].posX)<=4 and abs(axeY-defenses[i].posY)<=4)):
                    defenses[i].health = defenses[i].health - Queen.damage
                    # break
            for i in range(len(walls)):
                if(walls[i].alive and (abs(axeX-walls[i].posX)<=4 and abs(axeY-walls[i].posY)<=4)):
                    walls[i].health = walls[i].health - Queen.damage
                    # break

        if(ip == "spawn1" and bcount < 6):
            # os.system('clear')
            # os.system('aplay -q ./snd/sounds/barbarian.wav')
            troops.append(barb(30, 17, 45, 1, 1, barb_model, 10, True))
            bcount = bcount + 1
        elif(ip == "spawn2" and bcount < 6):
            # os.system('aplay -q ./snd/sounds/barbarian.wav')
            troops.append(barb(30, 11, 100, 1, 1, barb_model, 10, True))
            bcount = bcount + 1
        elif(ip == "spawn3" and bcount < 6):
            # os.system('aplay -q ./snd/sounds/barbarian.wav')
            troops.append(barb(30, 37, 90, 1, 1, barb_model, 10, True))
            bcount = bcount + 1
        elif(ip == "spawn4" and acount < 6):
            troops.append(arch(15, 41, 80, 1, 1, arch_model, 5, True))
            acount = acount + 1
        elif(ip == "spawn5" and acount < 6):
            troops.append(arch(15, 15, 60, 1, 1, arch_model, 5, True))
            acount = acount + 1
        elif(ip == "spawn6" and acount < 6):
            troops.append(arch(10, 20, 110, 1, 1, arch_model, 5, True))
            acount = acount + 1
        elif(ip == "spawn7" and lcount < 6):
            troops.append(loon(30, 16, 44, 1, 1, loon_model, 20, True))
            lcount = lcount + 1
        elif(ip == "spawn8" and lcount < 6):
            troops.append(loon(30, 14, 95, 1, 1, loon_model, 20, True))
            lcount = lcount + 1
        elif(ip == "spawn9" and lcount < 6):
            troops.append(loon(30, 38, 105, 1, 1, loon_model, 20, True))
            lcount = lcount + 1

        # attackflag = 0

        for i in range(2, len(troops)):
            loonflag = False
            mn = 1000
            tarx = troops[i].posX
            tary = troops[i].posY
            for j in range(len(defenses)):
                if((troops[i].alive and defenses[j].alive) and abs(troops[i].posX-defenses[j].posX) + abs(troops[i].posY-defenses[j].posY) < mn):
                    loonflag = True
                    mn = abs(troops[i].posX-defenses[j].posX) + abs(troops[i].posY-defenses[j].posY)
                    tarx = defenses[j].posX
                    tary = defenses[j].posY

            if((not loonflag and isinstance(troops[i],loon)) or (not isinstance(troops[i], loon))):
                for j in range(len(objects)):
                    if((troops[i].alive and objects[j].alive) and abs(troops[i].posX-objects[j].posX) + abs(troops[i].posY-objects[j].posY) < mn):
                        mn = abs(troops[i].posX-objects[j].posX) + abs(troops[i].posY-objects[j].posY)
                        tarx = objects[j].posX
                        tary = objects[j].posY


            if(isinstance(troops[i], barb)):
                if(tary < troops[i].posY):
                    troops[i].moveleft()
                if(tary > troops[i].posY):
                    troops[i].moveright()
                if(tarx < troops[i].posX):
                    troops[i].moveup()
                if(tarx > troops[i].posX):
                    troops[i].movedown()
                # attackflag = 1
                troops[i].isAttacking = True
            elif(isinstance(troops[i], loon)):
                if(tary < troops[i].posY):
                    troops[i].moveleft()
                if(tary > troops[i].posY):
                    troops[i].moveright()
                if(tarx < troops[i].posX):
                    troops[i].moveup()
                if(tarx > troops[i].posX):
                    troops[i].movedown()

                if(tary < troops[i].posY):
                    troops[i].moveleft()
                if(tary > troops[i].posY):
                    troops[i].moveright()
                if(tarx < troops[i].posX):
                    troops[i].moveup()
                if(tarx > troops[i].posX):
                    troops[i].movedown()

                if(troops[i].posX == tarx and troops[i].posY == tary):
                    # attackflag = 1
                    troops[i].isAttacking = True
            elif(isinstance(troops[i], arch) and abs(troops[i].posX-tarx) + abs(troops[i].posY-tary) > 5):
                if(tary < troops[i].posY):
                    troops[i].moveleft()
                elif(tary > troops[i].posY):
                    troops[i].moveright()
                elif(tarx < troops[i].posX):
                    troops[i].moveup()
                elif(tarx > troops[i].posX):
                    troops[i].movedown()

                if(tary < troops[i].posY):
                    troops[i].moveleft()
                elif(tary > troops[i].posY):
                    troops[i].moveright()
                elif(tarx < troops[i].posX):
                    troops[i].moveup()
                elif(tarx > troops[i].posX):
                    troops[i].movedown()

                if(abs(troops[i].posX-tarx) + abs(troops[i].posY-tary)<=5):
                    # attackflag = 1
                    troops[i].isAttacking = True

        for i in range(2, len(troops)):
            flag = 0
            if(isinstance(troops[i], barb) and troops[i].isAttacking):
                for j in range(len(objects)):
                    if((troops[i].alive and objects[j].alive) and (troops[i].posX >= objects[j].posX and troops[i].posX < objects[j].posX + objects[j].height)):
                        if(troops[i].posY + 1 == objects[j].posY or troops[i].posY == objects[j].posY + objects[j].width):
                            objects[j].health = objects[j].health - troops[i].damage
                            flag = 1
                            break
                    elif((troops[i].alive and objects[j].alive) and (troops[i].posY >= objects[j].posY and troops[i].posY < objects[j].posY + objects[j].width)):
                        if(troops[i].posX + 1 == objects[j].posX or troops[i].posX == objects[j].posX + objects[j].height):
                            objects[j].health = objects[j].health - troops[i].damage
                            flag = 1
                            break

                if flag == 1:
                    continue

                for j in range(len(defenses)):
                    if((troops[i].alive and defenses[j].alive) and (troops[i].posX >= defenses[j].posX and troops[i].posX < defenses[j].posX + defenses[j].height)):
                        if(troops[i].posY + 1 == defenses[j].posY or troops[i].posY == defenses[j].posY + defenses[j].width):
                            defenses[j].health = defenses[j].health - \
                                troops[i].damage
                            flag = 1
                            break
                    elif((troops[i].alive and defenses[j].alive) and (troops[i].posY >= defenses[j].posY and troops[i].posY < defenses[j].posY + defenses[j].width)):
                        if(troops[i].posX + 1 == defenses[j].posX or troops[i].posX == defenses[j].posX + defenses[j].height):
                            defenses[j].health = defenses[j].health - \
                                troops[i].damage
                            flag = 1
                            break

                if flag == 1:
                    continue

                # make sure u check this again !!!!!!
                for j in range(len(walls)):
                    if((troops[i].alive and walls[j].alive) and (troops[i].posX >= walls[j].posX and troops[i].posX < walls[j].posX + walls[j].height)):
                        if(troops[i].posY + 1 == walls[j].posY or troops[i].posY == walls[j].posY + walls[j].width):
                            walls[j].health = walls[j].health - troops[i].damage
                            flag = 1
                            break
                    elif(troops[i].alive and walls[j].alive and (troops[i].posY >= walls[j].posY and troops[i].posY < walls[j].posY + walls[j].width)):
                        if(troops[i].posX + 1 == walls[j].posX or troops[i].posX == walls[j].posX + walls[j].height):
                            walls[j].health = walls[j].health - troops[i].damage
                            flag = 1
                            break

                if flag == 1:
                    continue
            elif(isinstance(troops[i],arch) and troops[i].isAttacking):
                for j in range(len(objects)):
                    if((troops[i].alive and objects[j].alive) and (abs(troops[i].posX - objects[j].posX) + abs(troops[i].posY-objects[j].posY)) <= 5):
                        # if(troops[i].posY + 1 == objects[j].posY or troops[i].posY == objects[j].posY + objects[j].width):
                            objects[j].health = objects[j].health - troops[i].damage
                            flag = 1
                            break
                    
                if(flag==1):
                    continue

                for j in range(len(defenses)):
                    if((troops[i].alive and defenses[j].alive) and (abs(troops[i].posX - defenses[j].posX) + abs(troops[i].posY-defenses[j].posY)) <= 5):
                        # if(troops[i].posY + 1 == defenses[j].posY or troops[i].posY == defenses[j].posY + defenses[j].width):
                            defenses[j].health = defenses[j].health - troops[i].damage
                            flag = 1
                            break

                if(flag==1):
                    continue

                for j in range(len(walls)):
                    if((troops[i].alive and walls[j].alive) and (abs(troops[i].posX - walls[j].posX) + abs(troops[i].posY-walls[j].posY)) <= 2):
                        # if(troops[i].posY + 1 == walls[j].posY or troops[i].posY == walls[j].posY + walls[j].width):
                            walls[j].health = walls[j].health - troops[i].damage
                            flag = 1
                            break

                if(flag==1):
                    continue
            
            elif(isinstance(troops[i],loon) and troops[i].isAttacking):
                for j in range(len(defenses)):
                    if((troops[i].alive and defenses[j].alive) and (troops[i].posX == defenses[j].posX and troops[i].posY == defenses[j].posY)):
                        defenses[j].health = defenses[j].health - troops[i].damage
                        flag = 1
                        break

                if(flag==1):
                    continue

                for j in range(len(objects)):
                    if((troops[i].alive and objects[j].alive) and (troops[i].posX == objects[j].posX and troops[i].posY == objects[j].posY)):
                        objects[j].health = objects[j].health - troops[i].damage
                        flag = 1
                        break
                    



        if ip == "heal":
            healspell = Spell(1)
            healspell.deployheal(troops)
        elif ip == "rage":
            ragespell = Spell(2)
            rageflag = ragespell.deployrage(rageflag)

        for i in range(len(defenses)):
            for j in range(len(troops)):
                if(isinstance(defenses[i],cannon) and not isinstance(troops[j], loon) and (defenses[i].alive and troops[j].alive) and (defenses[i].posX-troops[j].posX)*(defenses[i].posX-troops[j].posX) + (defenses[i].posY-troops[j].posY)*(defenses[i].posY-troops[j].posY) <= defenses[i].rng*defenses[i].rng):
                    if rageflag == 0.05:
                        troops[j].health = troops[j].health - \
                            (defenses[i].damage/2)
                    else:
                        troops[j].health = troops[j].health - defenses[i].damage
                    defenses[i].changecolor()
                    break
                elif(isinstance(defenses[i],wizard) and (defenses[i].alive and troops[j].alive) and (defenses[i].posX-troops[j].posX)*(defenses[i].posX-troops[j].posX) + (defenses[i].posY-troops[j].posY)*(defenses[i].posY-troops[j].posY) <= defenses[i].rng*defenses[i].rng):
                    tarx = troops[j].posX
                    tary = troops[j].posY
                    for k in range(len(troops)):
                        if(abs(troops[k].posX-tarx) <= 1 and abs(troops[k].posY-tary) <= 1 and troops[k].alive):
                            troops[k].health = troops[k].health - defenses[i].damage
                            defenses[i].changecolor()
                            # print(troops[k].health)
                            # break
                    break

        cnt = 0
        for i in range(len(troops)):
            if troops[i].alive:
                cnt = cnt + 1
        if cnt == 0:
            gameflag = 1
            break

        cnt = 0
        for i in range(len(objects)):
            if objects[i].alive:
                cnt = cnt + 1

        for i in range(len(defenses)):
            if defenses[i].alive:
                cnt = cnt + 1

        if cnt == 0:
            t = 0
            dir = ""
            rageflag = 0.1
            heroflag = 0
            f = 0
            gameflag = 0
            if level == 1:
                level = 2
            elif level == 2:
                level = 3
            else:
                gameflag = 2
                break

        for i in range(44):
            for j in range(173):
                print(grid[i][j], end="")
            print("")

        if(ip == "quit"):
            quit()
    # t = t+1
    # if(t > 10):
    #     quit()
    # sleep(2)
    # # print("\033c")
    # clear()

if gameflag == 1:
    print("You lost!")
elif gameflag == 2:
    print("You won!")
