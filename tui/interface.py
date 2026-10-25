from db.item_repo import ItemRepository
from classes.inventory_item import InventoryItem
from rich.console import Console
from helper.print_items import print_items

console = Console()
item_repo = ItemRepository()
spacer = "-" * 20
TEXT_COLOR = "#fdfcdc"
HEADER_COLOR = "#f07167"

console.print("[#023e7d bold italic]Welcome to Item MGR")
console.print(spacer)

def run_tui():
    while True:
        console.print(f"[{HEADER_COLOR} bold]Select an operation: ")

        console.print(f"[{TEXT_COLOR}]1. Display all items")
        console.print(spacer)
        console.print(f"[{TEXT_COLOR}]2. Display specific item")
        console.print(spacer)
        console.print(f"[{TEXT_COLOR}]3. Add item")
        console.print(spacer)
        console.print(f"[{TEXT_COLOR}]4. Delete item")
        console.print(spacer)
        console.print(f"[{TEXT_COLOR}]5. Edit item")
        console.print(spacer)
        console.print(f"[{TEXT_COLOR}]6. Quit")
        # TODO: other operations
        user_inp = console.input(f"[{HEADER_COLOR} bold]What operation would you like to perform: ")
        console.print(spacer)

        match user_inp:
            case "1": # get all items
                # TODO: implement "more" linux command func to show 
                # 10 items and then let the user press space to show more 
                # or q to exit
                inv_data = item_repo.get_all_items()
                if len(inv_data) == 0:
                    print("Database is empty")
                    print(spacer)
                    break

                print_items(item_repo.get_all_items())

            case "2": # get specific from db
                id = int(input("Please enter id of item: "))
                print(spacer)
                data = item_repo.get_item(id)
               
                if data:
                    print_items(data)
                else:
                    print("Item not found!")
                    print(spacer)

            case "3": # add to db
                # TODO: allow user to quit while adding items (just get out of add operation)
                while True:
                    name = input("Name of item: ")
                    price = input("Price of item: ")
                    quantity = input("Quantity: ")
                    description = input("Description (optional): ")
                    confirmation = input(f"Is the information entered correctly (y/n) : {name}, {price}, {quantity}, {description} ")
                    
                    if confirmation.lower() == "y" or confirmation.lower() == "yes":
                        try:
                            new_item = InventoryItem(name, price, quantity, description)
                            item_repo.add_item(new_item)
                            print(spacer)
                            console.print("[green bold]Item added!")
                            print(spacer)
                        except Exception as e:
                            print(spacer)
                            print(e)
                            print(spacer)
                        break

            case "4": # delete using id
                id = int(input("Enter id of item to delete: "))
                print(spacer)
                if item_repo.del_from_db(id):
                    print("Item deleted")
                else:
                    print("Item not found!")
                    print(spacer)

            case "5": # edit item
                id = int(input("Enter id of item to edit: "))
                print(spacer)

                if item_repo.get_item(id) != None:
                    column = input("Enter the property that you want to edit: ")
                    print(f"Editing {column}")
                    value = input("Enter new value: ")
                    try:
                        item_repo.edit_item(column, value, id)
                    except Exception as e:
                        print(e)
                    
                    print(f"{column.capitalize()} edited!") 

                print(f"Item with id {id} not found!")
                
            case "6":
                exit(0)
            





                

        