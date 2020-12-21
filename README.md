# Chef_and_dish_ingredient
A python problem to solve a chef's problem regarding the dishes he wishes to prepare

Problem Statement


Chef's ingredients:-

1.The chef receives exactly 1 ingredient per day from the market.The
ingredients never repeat.

2. Every ingredient belongs to 1 of the 3 categories namely FIBER,FAT & CARB.

3.Every ingredient has a unique ingredient id.

4.The ingredient id always starts with the category name (ex:FIBERBroccoli,FATCheese,CARBRice)

Chef's Dishes

1. All of the chef's dishes have a constant number of ingredients=4

2. All the ingredients used will be fully used in a Dish. The chef doesn' use some part/quntity of an ingredient.

3.Chef can either prepare dish X or dish Y on a given day
dish X - has minimum 2 FAT ingredients and no CARB ingredient
dish Y has atleast 1 CARB ingredient and atleast 1 FIBER ingredient. It has no FAT ingredient


Chef's Cooking style:-

1. If the chef has multiple options of ingredients for the dish,then he takes the oldest possible ones to cook
in the order of their arrival.

2.After the chef prepares a dish,the ingredients used can Not be reused as they have been already used.

3.The chef prepares a maximum of 1 dish per day.

4.if the Chef does not have enough ingredients to cook the dish with above mentioned rules,then he does not
cook on that day.

Given the input array of ingredient id that the chef receives every day (i.e. array index is the day number)
write a program to print when does the chef cook a dish and when he does not.


Input:-

Line 1: The total number of days for the scope of the problem(1<=input<=20)

Line 2: The space separated ingredient ids.(6<=length(ingredientid)<=20)

Output:- Print the dish(X or Y) if the chef cooks on that day
and print "-" if the chef doesn't cook anything on that day.Print the output as  single string.

Example input 1:

9
FATOil FIBERSpinach CARBRice FATCheese FIBERBeans FATOlive CARBPotato FIBERBroccoli FIBERBanana
Example output 2:
----X---Y

Example input 2:
13
CARBBeetroot FIBERCarrot FATOlive CARBCorn CARBPotato FIBERBroccoli FATEgg FIBERBeans FATCheese CARBRice FIBERSpinach FATOil FIBERBanana
Example output 2:
----Y--X-----
