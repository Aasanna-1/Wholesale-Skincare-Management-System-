def read_products():
    try:
        file = open("Product.txt", "r")
        product_dict = {}
        product_lines = file.readlines()
        item_id = 1
        for line in product_lines:
            line = line.replace("\n","").split(",")
            product_dict[item_id] = line # value insertion
            item_id += 1
        #Display loaded products from the dictionary
        print(product_dict)
        print("\n")
        return product_dict
    except FileNotFoundError:
        print("Error: Product.txt file not found!")
        exit()
    except Exception as error:
        print("An unexpected error occurred while reading the file:", str(error))
        exit()
