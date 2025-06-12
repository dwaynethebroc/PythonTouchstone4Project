import json

def load_inventory():
    try:
        with open("inventory.json") as json_file:
            json_data = json.load(json_file)
            return json_data
    except FileNotFoundError:
        print("Inventory file not found.")
        return {}
    
def save_inventory(inventory):
    with open("inventory.json", "w") as file:
        modified_json = json.dump(inventory, file, indent=4)
        return modified_json
    
def view_inventory(inventory):
    print('Current inventory:')
    for key, value in inventory.items():
        print(f'    {key}:')
        print(f"    Name: {value['name']}")
        print(f"    Price: {value['price']:.2f}")
        print(f"    Quantity: {value['quantity']}")
        print(f"    Type: {value['type']}")
        print('')

def add_item(inventory):
    new_item_name = input('what is the item you would like to add to the inventory?: ')

    for key, value in inventory.items():
        if new_item_name == value['name']:
            print('Item already exists in inventory')
            return inventory
        
    price = input("What is the price of the item: ")
    quantity = input("What is the quantity of the item: ")
    type = input("Is it a food or drink: ")

    index = 0
    if type == "food":
        count_food = 0
        for key, value in inventory.items():
            if value['type'] == 'food':
                count_food += 1
        index = f"A{count_food}"
    elif type == "drink":
        count_drink = 0
        for key, value in inventory.items():
            if value['type'] == 'drink':
                count_drink += 1
        index = f"A{count_drink}"

    



def display_menu():
    print("1. View Inventory")
    print("2. Add New Item")
    print("3. Update Item")
    print("4. Remove Item")
    print("5. Exit")
    choice = input("Enter a choice (1-5): ")
    return choice


inventory = load_inventory()
print(inventory)

view_inventory(inventory)

# choice = display_menu()
# print(choice)