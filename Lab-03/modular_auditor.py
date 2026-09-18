# Global Constants
MAX_CAPACITY = 500
TAX_RATE = 0.1
FAILED_ENTRY = 0    

def main():
    inventory = 0
    tax_amount = 0
    exit_program = False
    global MAX_CAPACITY

    while not exit_program:
        stockQty = get_valid_input()
        if stockQty == "quit":
            exit_program = True
        elif stockQty == None:
            continue
        else:
            if inventory >= MAX_CAPACITY:
                break
            inventory = process_delivery(inventory, stockQty)

def get_valid_input():
    global FAILED_ENTRY
    user_input = input("Enter Stock Quantity: ")
    if user_input == "quit":
        return "quit"
    elif user_input.isdigit() != True:
        print("Please input a number")
        FAILED_ENTRY += 1
        return None
    return user_input

def process_delivery(current_total, new_value):
    new_total = current_total + int(new_value)
    return new_total

if __name__ == "__main__":
    main()