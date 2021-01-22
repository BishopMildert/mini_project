from core import *

app_start = True
options_menu = {
    '0': False,
    '1': 'show product menu',
}
# text file where stock is permanentely saved
with open('app/data/products.txt') as f:
    stock_file = f.read().splitlines()

products_menu = {
    '0': 'return main menu',
    '1': 'product ',
    '2': 'add new product',
    '3': 'which product to update: ',
    '4': 'What product would you like to delete? ',
}

# MAIN MENU OPTIONS
main_menu_options = 'MAIN MENU\n 0: EXIT APP \n 1: MENU \n\n SELECTION: '
# Product Menu Options
product_menu_options = 'PRODUCT MENU \n\n 0: RETURN MAIN MENU \n 1: PRODUCTS IN STOCK \n 2: ADD NEW PRODUCT \n 3: UPDATE PRODUCT \n 4: DELETE PRODUCT \n'

# Keeps programme running
while app_start == True:
    print('WELCOME, PLEASE SELECT ONE OF THE FOLLOWING OPTIONS')
    # Print MAIN MENU
    print(main_menu_options)
    menu_select = input('SELECT OPTION: ')
    if menu_select == '0':
        break

    elif menu_select == '1':
        # print product menu options
        print(product_menu_options)

        # VARIABLE SETTING OPTION FOR PRODUCT MENU
        menu_option_select = input('OPTION: ')
        # OPTION 1: products in stock
        if menu_option_select == '1':
            for idex, item in enumerate(stock_file, 1):
                print(f'{idex}. {item}')
                continue
        
        # OPTION 2: add new product
        elif menu_option_select == '2':
            new_product = input('What product would you like to add? ')
            add_new_product(new_product, stock_file)
            print(stock_file)
            continue

        # OPTION 3: Update Product
        # elif menu_option_select == '3':
            # need to create function

            # OPTION 4: Delete Product
        elif menu_option_select == '4':
            for index, item in enumerate(stock_file):
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
