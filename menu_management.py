def add_item(menu, item):
    if item not in menu:
        menu.append(item)
    else:
        print(f"{item} is already in the menu.")
def remove_item(menu, item):
    if item in menu:
        menu.remove(item)
    else:
        print(f"{item} does not exist in the menu.")
def check_item(menu, item):
    if item in menu:
        return f'"{item} is available"'
    else:
        return f'"{item} is not available"'
initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]
add = "Tacos"
add_item(initial_menu, add)
remove = "Salad"
remove_item(initial_menu, remove)
check= "Pizza"
available_item= check_item(initial_menu, check)
print(f"Updated menu: {initial_menu}")
print(f"Availability: {available_item}")