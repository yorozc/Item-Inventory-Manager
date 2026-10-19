from db.item_repo import ItemRepository
from classes.inventory_item import InventoryItem
from rich.console import Console

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

        console.print(f"[{TEXT_COLOR}]1. Add new item")
        console.print(spacer)
        console.print(f"[{TEXT_COLOR}]2. Display all items")
        console.print(spacer)
        console.print(f"[{TEXT_COLOR}]3. Display specific item via ID")
        console.print(spacer)
        console.print(f"[{TEXT_COLOR}]4. Delete item")
        console.print(spacer)
        # TODO: other operations
        # TODO: use rich to make tui look nice
        user_inp = input("What operation would you like to perform: ")
        console.print(spacer)

        match user_inp:
            case "1": # add to db

                while True:
                    name = input("Name of item: ")
                    price = input("Price of item: ")
                    quantity = input("Quantity: ")
                    description = input("Description (optional): ")
                    confirmation = input(f"Is the information entered correctly (y/n) : {name}, {price}, {quantity}, {description} ")

                    if confirmation.lower() == "y" or confirmation.lower() == "yes":

                        new_item = InventoryItem(name, price, quantity, description)
                        item_repo.add_item(new_item)

                        inv_data = item_repo.get_all_items()
                        for item in inv_data:
                            print(item)

                        break

                    print("Item added!")

            case "2": # get all from db
                inv_data = item_repo.get_all_items()
                if len(inv_data) == 0:
                    print("Database is empty")
                    print(spacer)
                    break
                for item in inv_data:
                    print(spacer)
                    print(f"ID: {item[0]}")
                    print(f"Name: {item[1]}")
                    print(f"Price: ${item[2]:.2f}")
                    print(f"Quantity: {item[3]}")
                    print(f"Description: {item[4]}")
                    print(spacer)

            case "3": # get using id
                id = int(input("Please enter id of item: "))
                data = item_repo.get_item(id)

                if data != None:
                    print(spacer)
                    print(f"ID: {data[0]}")
                    print(f"Name: {data[1]}")
                    print(f"Price: ${data[2]:.2f}")
                    print(f"Quantity: {data[3]}")
                    print(f"Description: {data[4]}")
                    print(spacer)

                print(spacer)
                print("ID cannot be empty")
                print(spacer)


            case "4": # delete using id
                id = int(input("Enter id of item to delete: "))
                item_repo.del_from_db(id)
                print("Item deleted")

        