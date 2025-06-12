# PythonTouchstone4Project

Project for intro to Python Programming

BEGIN PROGRAM

DEFINE function load_inventory()
IF inventory file exists
OPEN the JSON file in read mode
LOAD data into inventory dictionary
ELSE
SET inventory dictionary to empty
RETURN inventory

DEFINE function save_inventory(inventory)
OPEN the JSON file in write mode
WRITE inventory dictionary to file in JSON format

DEFINE function display_menu()
PRINT main menu options: 1. View Inventory 2. Add New Item 3. Update Item 4. Remove Item 5. Exit
PROMPT user for menu choice
RETURN user input

DEFINE function view_inventory(inventory)
FOR each item_code and item_data in inventory
PRINT item_code, item name, price, and quantity

DEFINE function add_item(inventory)
PROMPT user for new item code
IF item code already exists in inventory
PRINT "Item code already exists"
RETURN
PROMPT for item name
PROMPT for item price
PROMPT for item quantity
ADD new item to inventory with item code as key and item details as values
PRINT confirmation message

DEFINE function update_item(inventory)
PROMPT user for item code to update
IF item code not in inventory
PRINT "Item not found"
RETURN
PROMPT user to update: 1. Name 2. Price 3. Quantity
PROMPT for which attribute to update
IF updating name
PROMPT for new name
UPDATE item name
IF updating price
PROMPT for new price
UPDATE item price
IF updating quantity
PROMPT for new quantity
UPDATE item quantity
PRINT confirmation message

DEFINE function remove_item(inventory)
PROMPT user for item code to remove
IF item code not in inventory
PRINT "Item not found"
RETURN
DELETE item from inventory
PRINT confirmation message

SET inventory = load_inventory()

WHILE True
SET choice = display_menu()

    IF choice == "1"
        CALL view_inventory(inventory)

    ELSE IF choice == "2"
        CALL add_item(inventory)
        CALL save_inventory(inventory)

    ELSE IF choice == "3"
        CALL update_item(inventory)
        CALL save_inventory(inventory)

    ELSE IF choice == "4"
        CALL remove_item(inventory)
        CALL save_inventory(inventory)

    ELSE IF choice == "5"
        CALL save_inventory(inventory)
        PRINT "Exiting program."
        BREAK

    ELSE
        PRINT "Invalid choice. Try again."

END PROGRAM
