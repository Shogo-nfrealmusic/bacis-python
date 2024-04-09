def get_order_history(user, orders):
    user_orders = []
    for order in orders:
        if order['user_id'] == user['user_id']:
            user_orders.append(order)
    return user_orders
    

orders = [
    {
        'order_id': 1,
        'user_id': 1,
        'items': [
            {'name': 'キャップ', 'type': 'cap', 'price': 8000},
            {'name': 'Tシャツ', 'type': 'clothes', 'price': 2000}
        ]
    },
    {
        'order_id': 2,
        'user_id': 2,
        'items': [
            {'name': 'ランニングシューズ', 'type': 'shoes', 'price': 15000},
        ]
    },
    {
        'order_id': 3,
        'user_id': 1,
        'items': [
            {'name': 'スポーツドリンク', 'type': 'food', 'price': 150}
        ]
    },
    {
        'order_id': 4,
        'user_id': 3,
        'items': [
            {'name': 'アンダーウェア', 'type': 'clothes', 'price': 4500},
            {'name': 'テニスラケット', 'type': 'sports goods', 'price': 8000}          
        ]
    }
]

user = {'user_id': 1, 'status': 'basic'}
user_orders = get_order_history(user, orders)
for order in user_orders:
    print(order)
