import datetime
def write_products(products):
    with open("product_stock.txt", "w") as file:
        file.write("ID\t  Name\t\t\tBrand\t\t Quantity\t  Price\t\t Country\n")
        file.write("=" * 90 + "\n")
        for key, value in products.items():
            cost_price = int(value[3])
            selling_price = cost_price * 2
            line = str(key) + "\t" + value[0] + "\t\t" + value[1] + "\t\t   " + value[2] + "\t\t   " + str(selling_price) + "\t\t  " + value[4] + "\n"
            file.write(line)

        
def save_sold_bill(customer_name, phone, sold_items, total, shipping_cost, grand_total):
    now = datetime.datetime.now()

    
    now_string = str(now.year) + "-" + str(now.month).zfill(2) + "-" + str(now.day).zfill(2) + " " + str(now.hour).zfill(2) + ":" + str(now.minute).zfill(2) + ":" + str(now.second).zfill(2)

    filename = "WeCare_Bill_"+customer_name.replace(" ","_") + str(now.year) + str(now.month) + str(now.day) + str(now.hour) + str(now.minute) + str(now.second) + ".txt"

    try:
        with open(filename, "w") as file:
            file.write("=" * 100 + "\n")
            file.write("\t\t\t\t\tWeCare Wholesale Bill\n")
            file.write("=" * 100 + "\n")
            file.write("Date & Time:\t " + now_string + "\n")  
            file.write("Customer Name:\t " + customer_name + "\n")
            file.write("Phone Number:\t " + phone + "\n")
            file.write("-" * 100 + "\n")
            file.write("Product\t\tQuantity\tUnit Price\tTotal Price\n")
            file.write("-" * 100 + "\n")
            for item in sold_items:
                file.write(item[0] + "\t " + str(item[1]) + "\t\t" + str(item[2]) + "\t\t" + str(item[3]) + "\n")
            file.write("-" * 100 + "\n")
            file.write("Subtotal:\t " + str(total) + "\n")
            file.write("Shipping Cost:\t " + str(shipping_cost) + "\n")
            file.write("Grand Total:\t " + str(grand_total) + "\n")
            file.write("=" * 100 + "\n")
            file.write("\n")
        print("Bill saved successfully as " + filename)
    except Exception as e:
        print("\n*****Error saving bill:", str(e)+"*****")


def save_restocking_bill(restocked_items, total_restock_cost):
    now = datetime.datetime.now()

    
    now_string = str(now.year) + "-" + str(now.month).zfill(2) + "-" + str(now.day).zfill(2) + " " + str(now.hour).zfill(2) + ":" + str(now.minute).zfill(2) + ":" + str(now.second).zfill(2)

    filename = "WeCare Bill" + str(now.year) + str(now.month) + str(now.day) + str(now.hour) + str(now.minute) + str(now.second) + ".txt"

    try:
        with open(filename, "w") as file:
            file.write("=" * 100 + "\n")
            file.write("\t\t\t\t\tWeCare Restocking Bill\n")
            file.write("=" * 100 + "\n")
            file.write("Date & Time:\t " + now_string + "\n")  
            file.write("-" * 100 + "\n")
            file.write("Product\t\tQuantity\tUnit Cost\tTotal Cost\n")
            file.write("-" * 100 + "\n")
            for item in restocked_items:
                file.write(item[0] + "\t " + str(item[1]) + "\t\t" + str(item[2]) + "\t\t" + str(item[3]) + "\n")
            file.write("-" * 100 + "\n")
            file.write("Total Restocking Cost:\t " + str(total_restock_cost) + "\n")
            file.write("=" * 100 + "\n")
            file.write("\n")
        print("Restocking bill saved successfully as " + filename)
    except Exception as e:
        print("*****Error saving restocking bill:", str(e)+"*****")
