def calculate_recipe_costs(ingredient_prices, recipe):
    
    total_ingredient_cost = {}
    for name in recipe.keys():
        # total_ingredient_cost[name] = recipe[name]
        if name in ingredient_prices:
            cost = recipe[name] * ingredient_prices[name]
            total_ingredient_cost[name] = cost
        else:
            print(name + " is not in prices, cannot be added to total")

    

    return sum(total_ingredient_cost.values())
    








# Test your function with these:
prices = {
    "chicken": 5.99,
    "rice": 2.50,
    "beans": 1.75,
    "cheese": 4.25,
    "tortilla": 3.00
}

burrito_bowl = {"rice": 2, "beans": 1, "chicken": 1, "cheese": 1}
# Should return: 14.49

quesadilla = {"tortilla": 2, "cheese": 2}
# Should return: 10.50

# Test with missing ingredient:
mystery_recipe = {"rice": 1, "tofu": 1, "beans": 1}
# Should print message about tofu and return cost without it

print(calculate_recipe_costs(prices, burrito_bowl))
print(calculate_recipe_costs(prices, mystery_recipe))