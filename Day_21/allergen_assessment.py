from collections import defaultdict

def update_allergens(allergenDB, allergen):
    for key in allergenDB:
        if key != allergen and len(allergenDB[key]) > 1:
            allergenDB[key].difference_update(allergenDB[allergen])
            if len(allergenDB[key]) == 1:
                update_allergens(allergenDB, key)

def match_food_items(foods):
    ingredientDB = defaultdict(int)
    allergenDB = {}

    for food in foods:
        ingredients, allergens = [items.split(" ") for items in food]
        for allergen in allergens:
            allergenDB[allergen] = set(ingredients) if allergen not in allergenDB else allergenDB[allergen].intersection(ingredients)
            if len(allergenDB[allergen]) == 1:
                update_allergens(allergenDB, allergen) 
        for ingredient in ingredients:
            ingredientDB[ingredient] += 1
    
    return allergenDB, ingredientDB


with open("Day_21/input.txt", "r") as fin:
    foods = [line.rstrip(")").replace(",", "").split(" (contains ") for line in fin.read().split("\n")]

# Day 21.1
allergenDB, ingredientDB = match_food_items(foods)
dangerous_ingredients = [next(iter(allergenDB[key])) for key in sorted(allergenDB.keys())]
print(sum([count for ingredient, count in ingredientDB.items() if ingredient not in dangerous_ingredients]))

# Day 21.2
print(",".join(dangerous_ingredients))
