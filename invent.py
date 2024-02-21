# Inventory System

inventory = {
    "apples":13,
    "oranges":8,
    "pears":15,
    "bananas":12,
    "watermelon":5,
    "mangoes":10
    }

def add_item():
    item_name = input("Enter the item name: ")
    quantity = int(input("Enter the quantity: "))
    
    if item_name in inventory:
        inventory[item_name] += quantity
        print(f"Quantity updated for {item_name}.")
    else:
        inventory[item_name] = quantity
        print(f"{item_name} added to the inventory.")

def retrieve_item():
    item_name = input("Enter the item name: ")
    
    if item_name in inventory:
        print(f"Item: {item_name}")
        print(f"Quantity: {inventory[item_name]}")
    else:
        print(f"{item_name} is not found in the inventory.")

def calculate_total_quantity():
    total_quantity = sum(inventory.values())
    print(f"Total quantity of all items: {total_quantity}")

# Main program loop
while True:
    print("\n===== fruits System =====")
    print("1. Add item to inventory")
    print("2. Retrieve item information")
    print("3. Calculate total quantity of all items")
    print("0. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_item()
    elif choice == "2":
        retrieve_item()
    elif choice == "3":
        calculate_total_quantity()
    elif choice == "0":
        break
    else:
        print("Invalid choice. Please try again.")
        
print("Exiting inventory system.")





