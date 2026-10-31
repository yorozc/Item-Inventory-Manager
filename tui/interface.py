from db.db_repo import DBRepository

from classes.inventory_item import InventoryItem
from rich.console import Console
from helper.print_items import print_items

console = Console()
db_repo = DBRepository()

profile = db_repo.profile
spacer = "-" * 20
TEXT_COLOR = "#fdfcdc"
HEADER_COLOR = "#f07167"

console.print("[#023e7d bold italic]Welcome to Item MGR")
console.print(spacer)

def run_tui():
    while True:
        console.print(f"[{HEADER_COLOR} bold]Select an operation: ")
        print(f"Currently in profile: {db_repo.profile}")

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
        console.print(f"[{TEXT_COLOR}]6. Create New Profile")
        console.print(spacer)
        console.print(f"[{TEXT_COLOR}]7. Change Profile")
        console.print(spacer)
        console.print(f"[{TEXT_COLOR}]8. Show All Profiles")
        console.print(spacer)
        console.print(f"[{TEXT_COLOR}]9. Delete Profile")
        console.print(spacer)
        console.print(f"[{TEXT_COLOR}]10. Quit")
        # TODO: other operations
        user_inp = console.input(f"[{HEADER_COLOR} bold]What operation would you like to perform: ")
        console.print(spacer)

        match user_inp:
            case "1": # get all items
                # TODO: implement "more" linux command func to show 
                # 10 items and then let the user press space to show more 
                # or q to exit
                inv_data = db_repo.get_all_items()
                if len(inv_data) == 0:
                    print("Database is empty")
                    print(spacer)
                    

                print_items(db_repo.get_all_items())

            case "2": # get specific from db
                id = int(input("Please enter id of item: "))
                print(spacer)
                data = db_repo.get_item(id)
               
                if data:
                    print_items(data)
                else:
                    print("Item not found!")
                    print(spacer)

            case "3": # add to db
                # TODO: allow user to quit while adding items (just get out of add operation)
                while True:
                    name = input("Name of item: ")
                    category = input("Category of item: ")
                    cost_price = input("Cost of item: ")
                    retail_price = input("Retail cost of item: ")
                    quantity = input("Quantity: ")
                    description = input("Description (optional): ")
                    confirmation = input(f"Is the information entered correctly [{name}, {category}, {cost_price}, {retail_price}, {quantity}, {description}]: (y/n)")
                    
                    if confirmation.lower() == "y" or confirmation.lower() == "yes":
                        try:
                            new_item = InventoryItem(name, category, cost_price, retail_price, quantity, description)
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

                try:
                    db_repo.del_from_db(id)
                    print("Item deleted")
                except Exception as e:
                    print(e)

            case "5": # edit item
                try:
                    id = int(input("Enter id of item to edit: "))
                    print(spacer)

                    if not db_repo.get_item(id):
                        print(f"Error: Item with ID {id} does not exist.")

                    else: 
                        column = input("Enter the property that you want to edit: ")
                        value = input("Enter new value: ")
                        db_repo.edit_item(column, value, id)
                        print(f"{column.capitalize()} edited!") 

                except Exception as e:
                    print(e)

            case "6": # create profile
                try:
                    new_profile = input("Enter new profile name: ")
                    db_repo.create_profile(new_profile)
                    db_repo.switch_profile(new_profile)
                    
                except Exception as e:
                    print(e)

                print(f"New profile created: {new_profile}")

            case "7": # switch profile
                try:
                    profile = input("Input Profile: ")
                    db_repo.switch_profile(profile)
                except Exception as e:
                    print(e)

            case "8": # print profiles
                print(db_repo.show_all_profiles())

            case "9": # delete profile
                try:
                    profile_name = input("Enter profile name: ")
                    db_repo.delete_profile(profile_name)
                    print(f"Profile {profile_name} deleted.")
                except Exception as e:
                    print(e)

            case "10":
                exit(0)
            





                

        