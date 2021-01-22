# CORE FUNCTIONS FOR APP

# Product Functions

def add_new_product(x:str, list_stock:list):
    
    if x not in list_stock:
        return list_stock.append(x)
    else:
        return 'product already in stock'


def delete_product(item:str, stock_list:list):
    if item in stock_list:
        return stock_list.remove(item)
    else:
        return 'product not in stock'

# CHECK ERROR
# def update_stock(x, y):
#     global stock
#     for element in stock:
#         if x in stock:



