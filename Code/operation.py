import datetime
from write import save_sold_bill, save_restocking_bill, write_products
#Displaying products that are available to buy
def display_products(products):
    print("*" * 100)
    print("id  \t Name\t\t\t Brand\t\tQuantity \tPrice \t\tCountry")
    print("*" * 100)
    for key, value in products.items():
        print(key, end="\t")
        cost_price = int(value[3])
        selling_price = cost_price * 2
        for i in range(len(value)):
            if i == 3:
                #Displaying selling price of that is double of cost price
                print(selling_price, end="\t\t")
            else:
                print(value[i], end="\t\t")
        print()
    print("*" * 100)
    print("\n")

def sell_product(products):
    while True:
        
        name = input("Enter the customer's name: ")
        if name == "":
            print("\n***** Name cannot be empty! Please enter a valid name. *****\n")
        elif name.isdigit():
            print("\n***** Name cannot be a integer! Please enter a valid name. *****\n")
            
        else:
            break
        
    while True:
        ph_no = input("Enter the phone number: ")
        if ph_no.isdigit() and len(ph_no) == 10:
            break
        else:
            print("\n*****Invalid phone number, Please enter a 10 digit number!*****\n")

    sold_items = []
    total = 0
    shipping_cost = 0
    sell_loop = True

    while sell_loop:
        display_products(products)
        
#Getting valid product Id from the customer
        try:
            item_id = int(input("Please provide the Id of the product to sell: "))
            print("\n")

            #Verifying product Id
            while item_id <= 0 or item_id > len(products):
                print("\n********************Please provide a valid Id!!!********************\n")
                item_id = int(input("Please Provide the Id of the product to sell: "))

            #Taking Quantity
            item_quantity = int(input("Please enter the quantity of product to sell: "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.\n")
            continue

#Free items (Buy 3 get 1 free)
        selected_product_quantity = products[item_id][2]
        free_item = item_quantity // 3
        stock_deduct = item_quantity + free_item

#Validating available stock
        while item_quantity <= 0 or stock_deduct > int(selected_product_quantity):
            if item_quantity <= 0:
                print("The given input is not valid, Please enter a valid item quantity")
            elif stock_deduct > int(selected_product_quantity):
                print("The stock for selected item is not available. Please look into available stock!\n")

            try:
                item_quantity = int(input("Please enter the quantity of product to buy: "))
                free_item = item_quantity // 3
                stock_deduct = item_quantity + free_item
            except ValueError:
                print("Invalid quantity.\n")
                continue

#Announcing about the free items scheme
        if item_quantity >= 3:
            print("*" * 10 + " Dear " + name + ", as per the buy 3 get 1 free offer going on, you have received " +str(free_item) + " " + products[item_id][0] + " for free. " + "*" * 10)
        products[item_id][2] = str(int(products[item_id][2]) - stock_deduct)
        display_products(products)
        write_products(products)

        cost_price = int(products[item_id][3])
        selling_price = cost_price * 2
        total_price = selling_price * item_quantity
        total += total_price

#Appending the item sold for billing
        sold_items.append([products[item_id][0], item_quantity, selling_price, total_price])
        more = input("Do you want to sell another product? (y/n): ").lower()
        if more != "y":
            sell_loop = False

    if total > 10000:
        shipping_cost = 0
    else:
        shipping_cost = 1200
        
    grand_total = total + shipping_cost

#Generating the bill
    print("=" * 100)
    print("\t\t\t\t\tWeCare Wholesale Bill")
    print("=" * 100)
    now = datetime.datetime.now()
    print("Date & Time:\t", now)#Adding the current date and time of the bill generated               
    print("Customer Name:\t", name)
    print("Phone Number:\t", ph_no)
    print("-" * 100)
    print("Product\t\tQuantity\tUnit Price\tTotal Price")
    print("-" * 100)
    for item in sold_items:
        print(item[0], "\t", item[1], "\t\t", item[2], "\t\t", item[3])
    print("-" * 100)
    print("Subtotal:\t", total)
    print("Shipping Cost:\t", shipping_cost)
    print("Grand Total:\t", grand_total)
    print("=" * 100)
    print("\n")

    return name, ph_no, sold_items, total, shipping_cost, grand_total


def restock_product(products):
    
    restock_loop = True
    restocked_items = []
    total_restock_cost = 0
    while restock_loop:
        display_products(products)#Display product before restocking
        try:
            restock_id = int(input("Please provide the Id of the product to restock: "))
            while restock_id <= 0 or restock_id > len(products):
                print("Please provide a valid Id!!!\n")
                restock_id = int(input("Please provide the Id of the product to restock: "))
            restock_quantity = int(input("Please enter the quantity of product to add: "))
            while restock_quantity <= 0:
                print("Please enter a valid quantity greater than 0!!!\n")
                restock_quantity = int(input("Please enter the quantity of product to add: "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.\n")
            continue
        
        products[restock_id][2] = str(int(products[restock_id][2]) + restock_quantity)
        write_products(products)
        cost_price = int(products[restock_id][3])
        total_price = cost_price * restock_quantity
        total_restock_cost += total_price

        restocked_items.append([products[restock_id][0], restock_quantity, cost_price, total_price])
        
        print("Stock successfully updated!\n")
        display_products(products)

        more = input ("Do you want to restock another product? (y/n): ").lower()
        if more != "y":
            restock_loop = False


    # Generate the restocking bill
    print("=" * 100)
    print("\t\t\t\t\tWeCare Restocking Bill")
    print("=" * 100)
    now = datetime.datetime.now()
    print("Date & Time:\t", now)
    print("-" * 100)
    print("Product\t\tQuantity\tUnit Cost\tTotal Cost")
    print("-" * 100)
    for item in restocked_items:
        print(item[0], "\t", item[1], "\t\t", item[2], "\t\t", item[3])
    print("-" * 100)
    print("Total Restocking Cost:\t", total_restock_cost)
    print("=" * 100)
    print("\n")

    return restocked_items, total_restock_cost
