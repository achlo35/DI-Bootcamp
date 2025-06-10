class MenuManager():
    def __init__(self, menu):
        self.menu = {
            'Soup' : {'price': 10, 'spice' : "B", 'gluten': False},
            'Hamburger' : {'price': 15, 'spice' : "A", 'gluten': True},
            'Salad': {'price': 18, 'spice' : "A", 'gluten': False},
            'French Fries' : {'price': 5, 'spice' : "C", 'gluten': False},
            'Beef bourguignon' : {'price': 25, 'spice' : "B", 'gluten': True}
        }

    def add_item(self, name, price, spice, gluten):
        if name in self.menu:
            print(f'{name} already exists in the menu.')
        else:
            self.menu[name] = {'price': price, 'spice': spice, 'gluten': gluten}
            print(f'{name} has been added to the menu.')

    def update_item(self, name, price, spice, gluten):
        if name in self.menu:
            self.menu[name] = {'price': price, 'spice': spice, 'gluten': gluten}
            print(f'{name} has been updated.')
        else:
            print(f'{name} does not exist in the menu.')

    def remove_item(self, name):
        if name in self.menu:
            del self.menu[name]
            print(f'{name} has been removed from the menu.')
            print(self.menu)
        else:
            print(f'{name} does not exist in the menu.')



# Test code for MenuManager

menu_manager = MenuManager(None)

# Show initial menu
print("Initial menu:", menu_manager.menu)

# Add a new item
menu_manager.add_item('Pizza', 20, 'A', True)

# Try to add an existing item
menu_manager.add_item('Soup', 12, 'C', False)

# Update an existing item
menu_manager.update_item('Salad', 19, 'B', True)

# Update a non-existing item
menu_manager.update_item('Ice Cream', 8, 'C', False)

# Remove an existing item
menu_manager.remove_item('Hamburger')

# Remove a non-existing item
menu_manager.remove_item('Ice Cream')

# Show final menu
print("Final menu:", menu_manager.menu)