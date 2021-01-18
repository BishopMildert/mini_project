# START APP
# SHOW LIST OF OPTIONS TO USER AND ACCEPT NUMERICAL INPUT

# IF USER ENTERS 0 THEN EXIT APP

# IF USER ENTERS 1 THEN SHOW PRODUCT MENU

# IF USER ENTERS 0 RETURN TO MAIN MENU

# IF USER ENTERS 1 PRINT OUT PRODUCTS TO SCREEN

# IF USER ENTER 2 CREATE NEW PRODUCT

# ASK USER FOR THE NAME OF THE PRODUCT

# APPEND THIS TO THE LIST OF PRODUCTS

# STRETCH IF USER ENTERS 3 UPDATE PRODUCT

# ASK USER TO SELECT A PRODUCT TO UPDATE

# ASK USER FOR NEW NAME OF PRODUCT

# REPLACE PRODUCT AT SELECTED IDX WITH NEW NAME

# STRETCH IF USER ENTERS 4 DELETE PRODUCT
# ASK USER TO SELECT A PRODUCT TO DELETE

# REMOVE THIS ITEM FROM THE PRODUCT LIST

options_menu = {
    '0': False,
    '1': 'show product menu',
}


products_menu = {
    '0': 'return main menu',
    '1': 'print products to screen',
    '2': 'What product would you like to add?',
    '3': 'update product',
    '4': 'deletes product',

}

stock = []

# Function to add new product to stock list


def add_new_product():
    x = input('what would you like to add? ')
    global stock
    if x not in stock:
        return stock.append(x)
    else:
        return 'product already in stock'


def delete_product(x):
    global stock
    if x in stock:
        return stock.remove(x)
    else:
        return 'product not in stock'


# def update_stock(x, y):
#     global stock
#     for element in stock:
#         if x in stock:



# USER COMMANDS