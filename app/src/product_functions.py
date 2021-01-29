
from core import add_new_product, delete_product, update_product

product_menu_options = '''
    ---PRODUCT MENU---
    [0] - RETURN
    [1] - PRODUCTS
    [2] - ADD PRODUCT
    [3] - UPDATED PRODUCT
    [4] - DELETE PRODUCT
    '''

def products_function(products: list):
    while True:
        # print product menu options
        print(product_menu_options)

    # REQUEST USER INPUT
        menu_option_select = input('OPTION: ')
    # PRODUCT OPTION 0: return main menu
        if menu_option_select == '0':
            break
        # PRODUCT OPTIOM 1: products in stock
        elif menu_option_select == '1':
            for index, item in enumerate(products):
                print(index, item['item'])

    # PRODUCT OPTION 2: add new product
        elif menu_option_select == '2':
            print('What product would you like to add?')
            add_new_product(products)
            print(products)
            continue

    # PRODUCTS OPTION 3: update product
        elif menu_option_select == '3':
            print('SELECT A PRODUCT:')

            for index, item in enumerate(products):
                print(index, item['item'].title())

            update_product(products)
            print('PRODUCT UPDATED')

        elif menu_option_select == '4':
            print('SELECT PRODUCT TO DELETE:')
            for index, item in enumerate(products):
                print(index, item['item'].title())

            delete_product(products)
            print('PRODUCT DELETED')

        else:
            continue
