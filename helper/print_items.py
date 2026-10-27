spacer = "-" * 20

def print_items(inv_data):
    if type(inv_data) == list:
        for item in inv_data:
            print(f"ID: {item[0]}")
            print(f"Name: {item[1]}")
            print(f"Category: {item[2]}")
            print(f"Cost of item: ${item[3]:.2f}")
            print(f"Retail price: ${item[4]:.2f}")
            print(f"Quantity: {item[5]}")
            print(f"Description: {item[6]}")
            print(spacer)
    elif type(inv_data) == tuple:
        print(f"ID: {item[0]}")
        print(f"Name: {item[1]}")
        print(f"Category: ${item[2]}")
        print(f"Cost of item: ${item[3]:.2f}")
        print(f"Retail price: ${item[4]:.2f}")
        print(f"Quantity: {item[5]}")
        print(f"Description: {item[6]}")
        print(spacer) 