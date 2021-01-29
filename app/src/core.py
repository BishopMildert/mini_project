# CORE FUNCTIONS FOR APP


# file reader function
def file_reader(file_path):
    with open(file_path, 'r') as f:
        a_list = f.read().splitlines()
    return a_list


# SHOW ITEMS IN THE LIST FUNCTION
def show_items_in_list(a_list:list):
    for index, item in enumerate(a_list, 1):
        print(f'{index}. {item}')

# ------ PRODUCT FUNCTIONS --------
def add_new_product(products:list):
    '''
    This function takes user input 
    for ITEM, PRICE and STOCK and
    creates a dictionary and 
    appends to a list.
    '''
    try:
        item = input('Product: ')
        price = float(input('Price: £'))
        quantity = int(input('Stock Quantity:'))
    except TypeError:
        'ITEM has to be word. PRICE and QUANTITY msut be numerical values'
    product = {
        'item': item,
        'price': price,
        'stock': quantity,
    }
    products.append(product)
    return products

# FUNCTION TO CHECK IF ITEM IS IN LIST/DICTIONARY
def check_item(products:list, user_input:str):
    for item in range(len(products)):
        if products[item]['item'] == user_input:
            return True
        else:
            return False

# Function to delete product
def delete_product(products:list):
    user_input = input('ITEM: ')
    for item in range(len(products)): 
        if products[item]['item'] == user_input: 
            del products[item] 
            return products
    else:
        print('ITEM NO IN STOCK')
    return products

# function to update product
def update_product(products:list):
    user_input = input('ITEM: ')
    for item in range(len(products)):
        if products[item]['item'] == user_input:
            products[item]['item'] = user_input
        else:
            return 'INVALID INPUT'
    return products

# # CHECK ERROR
# def update_item(a_list:list, list_item:str, to_update:str):
#     for index, element in enumerate(a_list):
#         if element:
