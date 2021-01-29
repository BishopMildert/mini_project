# functions pulling

# read txt from file
def read_from_file(file_path):
    '''

    '''
    with open(file_path, 'r') as f:
        a_list = f.read().splitlines()
    return a_list

# save txt to file
def save_to_file(file_path, a_list):
    '''

    '''
    with open(file_path, 'w') as f:
        for item in a_list:
            return f.write(item)
