from menu_manager import MenuManager

def load_manager():
    return MenuManager()

def show_user_menu(manager):
    print('MENU')
    print('(a) Add an item')
    print('(d) Delete an item')
    print('(v)  View the menu')
    print('(x) Exit')

    user_choice = input('Please enter your choice(a,d,v or x): ').lower()
    if user_choice == 'a':
        manager.add_item()
    elif user_choice == 'd':
        manager.remove_items()
    elif user_choice == 'v':
        manager.view_menu()
    elif user_choice == 'x':
        manager.save_to_file()
        print("Exiting the menu editor. Goodbye!")
    else:
        print("Invalid choice. Please try again.")
        show_user_menu(manager)

def add_item_to_menu(manager):
    name = input("Enter the name of the item: ")
    try:
        price = float(input("Enter the price of the item: "))
        if manager.add_item(name, price):
            print(f"Item '{name}' added successfully.")
        else:
            print(f"Item '{name}' already exists in the menu.")
    except ValueError:
        print("Invalid price. Please enter a valid number.")

def remove_item_from_menu(manager):
    name = input("Enter the name of the item to remove: ")
    if manager.remove_items(name):
        print(f"Item '{name}' removed successfully.")
    else:
        print(f"Item '{name}' not found in the menu.")

def show_restaurant_menu(manager):
    print("Current Menu:")
    for item in manager.menu['items']:
        print(f"{item['name']}: ${item['price']:.2f}")
    if not manager.menu['items']:
        print("The menu is currently empty.")

if __name__ == "__main__":
    manager = load_manager()
    show_user_menu(manager)


