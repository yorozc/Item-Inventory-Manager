spacer = "-" * 20

def print_items(inv_data):
    for item in inv_data:
        print(spacer)
        print(f"ID: {item[0]}")
        print(f"Name: {item[1]}")
        print(f"Price: ${item[2]:.2f}")
        print(f"Quantity: {item[3]}")
        print(f"Description: {item[4]}")
        print(spacer)