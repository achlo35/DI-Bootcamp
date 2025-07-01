import json

class MenuManager:
    def __init__(self):
        with open('restaurant_menu.json', 'r') as file:
            self.menu = json.load(file)

    def add_item(self, name, price):
        for item in self.menu['items']:
            if item['name'].lower() == name.lower():
                return False
        self.menu['items'].append({'name': name, 'price': price})
        return True
        
    def remove_items(self, name):
        for i,item in enumerate(self.menu['items']):
            if item['name'].lower() == name.lower():
                del self.menu['items'][i]
                return True
        return False
        
    def save_to_file(self):
        with open('restaurant_menu.json', 'w') as file:
            json.dump(self.menu, file, indent=4)
        print("Menu saved successfully.")
    