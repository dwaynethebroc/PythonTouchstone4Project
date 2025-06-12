import json

# Loads the inventory data from 'inventory.json'.
# If the file doesn't exist, it returns an empty dictionary.
def load_inventory():
    try:
        with open("inventory.json") as json_file:
            json_data = json.load(json_file)
            return json_data
    except FileNotFoundError:
        print("Inventory file not found.")
        return {}

# Saves the inventory dictionary to 'inventory.json' in a nicely formatted way.
def save_inventory(inventory):
    with open("inventory.json", "w") as file:
        modified_json = json.dump(inventory, file, indent=4)
        return modified_json

# Displays the current inventory in a readable format, showing each item's details.
def view_inventory(inventory):
    print('Current inventory:')
    for key, value in inventory.items():
        print(f'    {key}:')
        print(f"    Name: {value['name']}")
        print(f"    Price: {value['price']:.2f}")
        print(f"    Quantity: {value['quantity']}")
        print(f"    Type: {value['type']}")
        print('')

# Adds a new item to the inventory, checking for duplicates and validating inputs.
# Automatically assigns a new key based on item type.
def add_item(inventory):
    new_item_name = input('what is the item you would like to add to the inventory?: ').lower()

    # Prevents adding duplicates
    for key, value in inventory.items():
        if new_item_name == value['name'].lower():
            print('Item already exists in inventory')
            return inventory
    
    # Validates numeric input for price and quantity
    try:
        price = float(input("What is the price of the item: "))
        quantity = int(input("What is the quantity of the item: "))
    except ValueError:
        print("Invalid price or quantity")
        return inventory
    
    # Ensures the type is either 'food' or 'drink'
    item_type = input("Is it a food or drink: ").strip().lower()
    if item_type not in ['food', 'drink']:
        print("Invalid type. Must be 'food' or 'drink'.")
        return inventory

    # Determines key prefix and finds next available index
    prefix = 'A' if item_type == 'food' else 'B'
    index = 1
    while f"{prefix}{index}" in inventory:
        index += 1
    item_key = f"{prefix}{index}"

    # Creates and adds the new item
    new_item_dict = {
        'name': new_item_name.capitalize(), 
        'price': price, 
        'quantity': quantity, 
        'type': item_type
    }
    inventory[item_key] = new_item_dict
    print(f"Item '{new_item_name}' added under code {item_key}.")

    # Sorts the inventory and saves it
    sorted_inventory = dict(sorted(inventory.items()))
    save_inventory(sorted_inventory)
    return sorted_inventory

# Allows the user to update an existing item's fields one by one (name, price, quantity, type).
# Handles invalid keys and input validation.
def update_item(inventory):
    view_inventory(inventory)

    key_code = input("What is the key code of the item you would like to update? Example: 'A2' or enter 'q' to exit program: ").strip()
    while key_code not in inventory and key_code != 'q':
        key_code = input("What is the key code of the item you would like to update? Example: 'A2' \n or enter 'q' to exit program").strip()
        if key_code == 'q':
            return inventory
        
    if key_code == 'q':
        return inventory

    item = inventory.get(key_code)

    # Loop for choosing and updating fields
    choice = ""
    while choice != 'q':
        print(f"1. Name: {item['name']}")
        print(f"2. Price: {item['price']}")
        print(f"3. Quantity: {item['quantity']}")
        print(f"4. Type: {item['type']}")
        print("OR Press 'q' to exit")
        print('')
        choice = input(f"Enter 1-4 to choose what value you would like to update for OR enter 'q' to quit program: ") 

        # Each block updates a specific field
        if choice == '1':
            new_name = input('What would you like to update the name to?: ')
            print(f"{item['name']} has been changed to {new_name}")
            item['name'] = new_name
        elif choice == '2':
            new_price = float(input('What would you like to update the price to?: '))
            print(f"{item['price']} has been changed to {new_price}")
            item['price'] = new_price
        elif choice == '3':
            new_quantity = int(input('What would you like to update the quantity to?: '))
            print(f"{item['quantity']} has been changed to {new_quantity}")
            item['quantity'] = new_quantity
        elif choice == '4':
            new_type = input('What would you like to update the type to?: ')
            print(f"{item['type']} has been changed to {new_type}")
            item['type'] = new_type
        elif choice == 'q':
            print('program is exiting now')
            return inventory
        else:
            print("Invalid selection. Choose 1-4 or 'q'.")

        # Displays updated item details
        print("NEW VALUES:")
        print(f'    {key_code}:')
        print(f"    Name: {item['name']}")
        print(f"    Price: {item['price']:.2f}")
        print(f"    Quantity: {item['quantity']}")
        print(f"    Type: {item['type']}")
        print('')

    sorted_inventory = dict(sorted(inventory.items()))
    save_inventory(sorted_inventory)
    return sorted_inventory

# Removes an item from the inventory after confirmation.
def remove_item(inventory):
    view_inventory(inventory)

    key_code = input("What is the key code of the item you would like to remove? Example: 'A2' or enter 'q' to exit program: ").strip().upper()
    while key_code not in inventory and key_code != 'q':
        key_code = input("What is the key code of the item you would like to update? Example: 'A2' or enter 'q' to exit program").strip()
        if key_code.lower() == 'q':
            return inventory
        
    if key_code.lower() == 'q':
        return inventory

    # Confirmation before deletion
    confirm = input(f"Are you sure you want to remove item {key_code}? (y/n): ").lower()
    if confirm != 'y':
        print("Item not removed.")
        return inventory

    # Removes the item and saves
    inventory.pop(key_code)
    sorted_inventory = dict(sorted(inventory.items()))
    save_inventory(sorted_inventory)
    return sorted_inventory

# Displays the main menu and collects user's choice
def display_menu():
    print("1. View Inventory")
    print("2. Add New Item")
    print("3. Update Item")
    print("4. Remove Item")
    print("5. Exit")

    choice = input("Enter a choice (1-5): ")
    return choice

# ---------------------------
# Main program starts here

# Load existing inventory from file or initialize empty if not found
inventory = load_inventory()

# Main program loop: continuously prompts user for actions
while True:
    choice = display_menu()

    # Option 1: Show the full inventory
    if choice == "1":
        view_inventory(inventory)

    # Option 2: Add a new item; return value reassigns inventory to keep it updated
    elif choice == "2":
        inventory = add_item(inventory)

    # Option 3: Update an existing item’s name, price, quantity, or type
    elif choice == "3":
        inventory = update_item(inventory)

    # Option 4: Remove an item by code, with confirmation
    elif choice == "4":
        inventory = remove_item(inventory)

    # Option 5: Save current inventory to file and exit program
    elif choice == "5":
        save_inventory(inventory)
        print("Inventory saved. Exiting program.")
        break

    # Handles invalid menu choices
    else:
        print("Invalid choice. Try again.")
