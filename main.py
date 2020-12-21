import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

number_of_days = int(input())

class FatEmpty(Exception):
    pass

fats = []
carbs = []
fibers=[]
first_dish = ''
first_fiber = 0
ingredient_counter=1

for ingredient in input().split():
    #first split ingredients into respective categories with ingredient_counter representing the timestamp
    if ingredient.startswith("FAT"):
        ingredient_counter=ingredient_counter+1
        fats.append(ingredient_counter)
    elif ingredient.startswith("CARB"):
        ingredient_counter=ingredient_counter+1
        carbs.append(ingredient_counter)
    elif ingredient.startswith("FIBER"):
        ingredient_counter=ingredient_counter+1
        fibers.append(ingredient_counter)

    #check lengths
    if first_dish == "":
        if len(fats)+len(fibers) >= 4 and len(fats) >= 2:
            fats.pop(0)
            fats.pop(0)
            for i in range(2): 
                try:
                    if fats[0] < fibers[0]:
                        fats.pop(0)
                    else:
                        fibers.pop(0)
                except:#list index out of range
                    if fats:
                        fats.pop(0)
                    else:
                        fibers.pop(0)
            first_dish = 'X'
            print('X', end='')
        elif len(carbs) >= 1 and len(fibers) >= 1 and (len(fibers)+len(carbs) >= 4):
            carbs.pop(0)
            fibers.pop(0)
            #pop the necessary ingredients
            #decide on third and fourth ingredients
            for i in range(2):
                try: 
                    if carbs[0] < fibers[0]:
                        carbs.pop(0)
                    else:
                        fibers.pop(0)
                except:
                    if carbs:
                        carbs.pop(0)
                    else:
                        fibers.pop(0)
            first_dish = 'Y'
            print('Y', end='')
        else:
            print('-', end='')
    elif first_dish == 'X':
        if len(carbs) >= 1 and len(fibers) >= 1 and (len(fibers)+len(carbs) >= 4):
            carbs.pop(0)
            fibers.pop(0)
            #pop the necessary ingredients
            #decide on third and fourth ingredients
            for i in range(2): 
                try:
                    if carbs[0] < fibers[0]:
                        carbs.pop(0)
                    else:
                        fibers.pop(0)
                except:
                    if carbs:
                        carbs.pop(0)
                    else:
                        fibers.pop(0)
            first_dish = 'Y'
            print('Y', end='')
        else:
            print("-", end='')
    elif first_dish == 'Y':
        if len(fats) >= 2 and (len(fats)+ len(fibers) >= 4):
            fats.pop(0)
            fats.pop(0)
            for i in range(2): 
                try:
                    if fats[0] < fibers[0]:
                        fats.pop(0)
                    else:
                        fibers.pop(0)
                except:
                    if fats:
                        fats.pop(0)
                    else:
                        fibers.pop(0)
            first_dish = 'X'
            print('X', end='')
        else:
            print("-", end='')
    else:
        print('-', end='')


#9
#FATOil FIBERSpinach CARBRice FATCheese FIBERBeans FATOlive CARBPotato FIBERBroccoli FIBERBanana
#----X---Y

#13
#CARBBeetroot FIBERCarrot FATOlive CARBCorn CARBPotato FIBERBroccoli FATEgg FIBERBeans FATCheese CARBRice FIBERSpinach FATOil FIBERBanana
#----Y--X-----


