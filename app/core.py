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

# # CHECK ERROR
# def update_item(a_list:list, list_item:str, to_update:str):
#     for index, element in enumerate(a_list):
#         if element:
