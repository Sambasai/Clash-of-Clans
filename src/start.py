# from infra import *

from colorama import Fore, Back, Style

grid = [[" " for i in range(173)] for j in range(44)]

hut_model = [["c" for i in range(3)] for j in range(3)]

townHall_model = [["c" for i in range(4)] for j in range(3)]

cannon_model = [["c" for i in range(3)] for j in range(2)]

wizard_model = [["c" for i in range(3)] for j in range(3)]

wall_model = [["c" for i in range(1)] for j in range(1)]

bking_model = [["K" for i in range(1)] for j in range(1)]

aqueen_model = [["Q" for i in range(1)] for j in range(1)]

barb_model = [["b" for i in range(1)] for j in range(1)]

arch_model = [["a" for i in range(1)] for j in range(1)]

loon_model = [["l" for i in range(1)] for j in range(1)]

wall_model[0][0] = "+"

townHall_model[0][0] = " "
townHall_model[0][1] = "|"
townHall_model[0][2] = "|"
townHall_model[0][3] = " "
townHall_model[1][0] = "/"
townHall_model[1][1] = " "
townHall_model[1][2] = " "
townHall_model[1][3] = "\\"
townHall_model[2][0] = "|"
townHall_model[2][1] = "_"
townHall_model[2][2] = "_"
townHall_model[2][3] = "|"

hut_model[0][0] = " "
hut_model[0][1] = "_"
hut_model[0][2] = " "
hut_model[1][0] = "/"
hut_model[1][1] = " "
hut_model[1][2] = "\\"
hut_model[2][0] = "|"
hut_model[2][1] = "_"
hut_model[2][2] = "|"

cannon_model[0][0] = " "
cannon_model[0][1] = "_"
cannon_model[0][2] = " "
cannon_model[1][0] = "/"
cannon_model[1][1] = "o"
cannon_model[1][2] = "\\"

wizard_model[0][0] = " "
wizard_model[0][1] = "_"
wizard_model[0][2] = " "
wizard_model[1][0] = "|"
wizard_model[1][1] = "W"
wizard_model[1][2] = "|"
wizard_model[2][0] = "|"
wizard_model[2][1] = "_"
wizard_model[2][2] = "|"

# objects = []
# walls = []
# # cannons = []
# defenses = []
# troops=[]
# # bking=[]
