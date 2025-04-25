
bread = 5
cheese = 8
butter = 6
tea = 10
coffee = 12
milk = 16
water = 17

# Store itesm and quantities in lists
items = ["bread", "cheese", "butter", "tea", "coffee", "milk", "water"]
quantities = [bread, cheese, butter, tea, coffee, milk, water]

# total inventory
total_inventory = sum(quantities)
print(f"The total inventory is {total_inventory}")

# highest inventory
highest_inventory = max(quantities)
print(f"The highest inventory is {highest_inventory}")

# lowest inventory
lowest_inventory = min(quantities)
print(f"The lowest inventory is {lowest_inventory}")

#index of highest and lowest quantities
highest_index = quantities.index(highest_inventory)
lowest_index = quantities.index(lowest_inventory)

# item with highest inventory
print("The item with the highest inventory is", items[highest_index])


# item with lowest inventory
print("The item with the lowest inventory is", items[lowest_index])