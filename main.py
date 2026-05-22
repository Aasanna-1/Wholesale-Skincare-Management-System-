from read import read_products
from write import write_products, save_sold_bill, save_restocking_bill
from operation import sell_product, restock_product, display_products

print("\n" * 2)
print("\t\t\t\t\t\tWeCare Wholesale\n")
print("\t\t\t\t   Kamalpokhari, Kathmandu | Ph no: 01445833\n")
print("-" * 112)
print("\t\t\tWelcome to the system! Hope you have a great time")
print("-" * 112)
print("\n")

products = read_products()

#Looping options for admin
main_loop = True
while main_loop:
    print("-" * 100)
    print("Displaying your options below")
    print("-" * 100)
    print("Option 1 (Sell the product)")
    print("Option 2 (Buy from Manufacturer)")
    print("Option 3 (Exit the system)")
    print("-" * 100)
    print("\n")

    #Taking admin's choice
    try:
        option = int(input("Enter an option to proceed: "))
        print("\n")
    except ValueError:
        print("Invalid input. Please enter a number (1-3).\n")
        continue

#For option 1
    if option == 1:
        print("-" * 100)
        print("Enter your details to generate bill")
        print("-" * 100)
        
        result=sell_product(products)

        if result is not None:
            name, ph_no, sold_items, total, shipping_cost, grand_total = result
            save_sold_bill(name, ph_no, sold_items, total, shipping_cost, grand_total)

#For option 2
    elif option == 2:
        print("-" * 100)
        print("Restock from Manufacturer")
        print("-" * 100)
        result = restock_product(products)

        if result is not None:
            restocked_items, total_restock_cost = result
            save_restocking_bill(restocked_items, total_restock_cost)

#For option 3
    elif option == 3:
        print("Exiting the system. Thank you!")
        write_products(products)
        main_loop = False
    else:
        print("Invalid option. Please select between 1-3.\n")
