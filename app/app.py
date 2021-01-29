# IMPORTING FUNCTIONS FROM CORE.PY SCRIPT
from src.core import add_new_product, delete_product, update_product
from src.product_functions import products_function
from src.data_structure import data_base
#
# read products product (could )
# with open('app/data/products.txt', 'r') as f:
#     stock_list = f.read().splitlines()
# # read courier file and pass it to a list
# with open('app/data/couriers.txt', 'r') as f:
#     couriers_list = f.read().splitlines()

# --- DATA ---
# PRODUCT data - DICT
products = [{
    'item': 'banana',
    'price': 0.69,
    'stock': 12,
}, {
    'item': 'apple',
    'price': 0.75,
    'stock': 10,
}]

# COURIER data -- list
courier = []

# ORDERS DATA -- DICT
orders = []

# DICTIONARY WITH ALL THE DATA COMBINED
data = {'products': products, 'courier': courier, 'orders': orders}

# MAIN MENU DICT
# options_menu = {
#     '0': False,
#     '1': products_menu,
#     '2': courier_menu,
# }

# MAIN MENU OPTIONS
main_menu_options = '''
    ---MAIN MENU---
    [0] - EXIT APP
    [1] - MENU
    '''


courier_menu_options = '''
    ---COURIER MENU---
    [0] - RETURN
    [1] - COURIERS
    [2] - ADD COURIER
    [3] - UPDATE COURIER
    [4] - REMOVE COURIER
    '''


# Keeps programme running
while True:
    # Print MAIN MENU
    print(main_menu_options)
    # Takes menu selection as input
    menu_select = input('SELECT OPTION: ')
    if menu_select == '0':
        break

    # ----- PRODUCT MENU -----
    elif menu_select == '1':
        products_function(products)


        
        # OPTION 3: Update Product
        # elif menu_option_select == '3':
        #     update_product_in_stock = input(
        #         'Which product would you like to update?')

            # need to create function

            # OPTION 4: Delete Product
        # elif menu_option_select == '4':
        #     for index, item in enumerate(stock_list):
        #         print(f'PRODUCT: {index}. {item}')
        #     delete_product = input(f'What product would you like to delete?')

        # else:
        #     print('something went wrong')
        #     break

    else:
        print('Selection not valid')
        continue

print('bye')

