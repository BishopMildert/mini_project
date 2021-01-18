from app_functions import add_new_product
options_menu = {
    '0': False,
    '1': 'show product menu',
}
stock = []

products_menu = {
    '0': 'return main menu',
    '1': 'product ',
    '2': 'add new product',
    '3': 'which product to update: ',
    '4': 'What product would you like to delete? ',
}


while True:
    print('Welcome, select one of the following:')
    menu_select = input('MAIN MENU\n 0: EXIT APP \n 1: MENU \n\n SELECTION: ')
    if menu_select == '0':
        break

    else:
        print('PRODUCT MENU \n\n 0: RETURN MAIN MENU \n 1: PRODUCTS IN STOCK \n 2: ADD NEW PRODUCT \n 3: UPDATE PRODUCT \n 4: DELETE PRODUCT \n')
    product_menu_select = input('OPTION: ')
    
    
    

    print(products_menu[product_menu_select])

    break
print(stock)