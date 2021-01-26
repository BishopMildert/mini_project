# IMPORTING FUNCTIONS FROM CORE.PY SCRIPT
from src.core import add_new_product, delete_product
from src.data_structure import data_base
# 
app_start = True

# read products product (could )
with open('app/data/products.txt', 'r') as f:
    stock_list = f.read().splitlines()
# read courier file and pass it to a list
with open('app/data/couriers.txt', 'r') as f:
    couriers_list = f.read().splitlines()


# PRODUCT MENU DICT
products_menu = {
    '0': 'return main menu',
    '1': stock_list,
    '2': 'add new product',
    '3': 'Which product to update: ',
    '4': 'Which product would you like to delete? ',
}

# COURIER MENU DICT
courier_menu = {
    '0': 'return main menu',
    '1': couriers_list,
    '2': 'add new courier',
    '3': 'update courier',
    '4':'delete courier',
}

# MAIN MENU DICT
options_menu = {
    '0': False,
    '1': products_menu,
    '2': courier_menu,
}

# MAIN MENU OPTIONS
main_menu_options = 'MAIN MENU\n 0: EXIT APP \n 1: MENU \n\n SELECTION: '
# Product Menu Options
product_menu_options = 'PRODUCT MENU \n\n 0: RETURN MAIN MENU \n 1: PRODUCTS IN STOCK \n 2: ADD NEW PRODUCT \n 3: UPDATE PRODUCT \n 4: DELETE PRODUCT \n'

courier_menu_options = 'COURIER MENU \n\n 0: RETURN MAIN MENU \n 1: COURIERS AVAILABLE \n 2: ADD NEW COURIER \n 3: UPDATE A COURIER \n 4: DELETE COURIER \n'

# Keeps programme running
while app_start == True:
    print('WELCOME, PLEASE SELECT ONE OF THE FOLLOWING OPTIONS')
    
    # Print MAIN MENU
    print(main_menu_options)
    menu_select = input('SELECT OPTION: ')
    if menu_select == '0':
        break

    # 
    elif menu_select == '1':
        # print product menu options
        print(product_menu_options)

        # VARIABLE SETTING OPTION FOR PRODUCT MENU
        menu_option_select = input('OPTION: ')
        # OPTION 1: products in stock
        if menu_option_select == '1':
            for index, item in enumerate(stock_list, 1):
                print(f'{index}. {item}')
                continue
        
        # OPTION 2: add new product
        elif menu_option_select == '2':
            new_product = input('What product would you like to add? ')
            add_new_product(new_product, stock_list)
            print(stock_list)
            continue

        # OPTION 3: Update Product
        elif menu_option_select == '3':
            update_product_in_stock = input('Which product would you like to update?')

            # need to create function

            # OPTION 4: Delete Product
        elif menu_option_select == '4':
            for index, item in enumerate(stock_list):
                print(f'PRODUCT: {index}. {item}')
            delete_product = input(f'What product would you like to delete?')
            
        else:
            print('something went wrong')
            break

    else:
        print('Selection not valid')
        continue
        
print('bye')

# update stock txt file
print(data_base)