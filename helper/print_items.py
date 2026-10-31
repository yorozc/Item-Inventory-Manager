spacer = "-" * 20

def print_items(inv_data):
    if type(inv_data) == list:
        for item in inv_data:
            print(f"ID: {item[0]}")
            print(f"Name: {item[2]}")
            print(f"Category: {item[3]}")
            print(f"Cost of item: ${item[4]:.2f}")
            print(f"Retail price: ${item[5]:.2f}")
            print(f"Quantity: {item[6]}")
            print(f"Description: {item[7]}")
            print(spacer)
    elif type(inv_data) == tuple:
        print(f"ID: {inv_data[0]}")
        print(f"Name: {inv_data[2]}")
        print(f"Category: {inv_data[3]}")
        print(f"Cost of item: ${inv_data[4]:.2f}")
        print(f"Retail price: ${inv_data[5]:.2f}")
        print(f"Quantity: {inv_data[6]}")
        print(f"Description: {inv_data[7]}")
        print(spacer) 