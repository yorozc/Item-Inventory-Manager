spacer = "-" * 20

def print_items(inv_data):
    if type(inv_data) == list:
        for item in inv_data:
            print(f"ID: {item[0]}")
            print(f"Name: {item[1]}")
            print(f"Price: ${item[2]:.2f}")
            print(f"Quantity: {item[3]}")
            print(f"Description: {item[4]}")
            print(spacer)
    elif type(inv_data) == tuple:
        print(f"ID: {inv_data[0]}")
        print(f"Name: {inv_data[1]}")
        print(f"Price: ${inv_data[2]}")
        print(f"Quantity: {inv_data[3]}")
        print(f"Description: {inv_data[4]}")
        print(spacer) 