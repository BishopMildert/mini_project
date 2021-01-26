data_base = {
    'products':[
        {
            'item':'coke',
            'price':1,
            'stock_quantity':10
        },
        {
        'item': 'coke',
        'price': 1,
        'stock_quantity': 10
        },

    ],
    'couriers': [
        'Bob', 'Martin'

    ],
    'orders': [{
        'customer_name': [
            'john',
        ],
        'customer_address':[
            'Drury Lane, London',
        ],
        'customer_phone':[
            '07855428765',
        ],
        'courier':[
            2,
        ],
        'order_status':[
            'preparing'
        ],
    },
        {
        'customer_name': [
            'maria',
        ],
        'customer_address':[
            'Down the road',
        ],
        'customer_phone':[
            '07854424123',
        ],
        'courier':[
            2,
        ],
        'order_status':[
            'preparing'
        ],

    },
     ]
}

print(type(data_base['products'][1]))
