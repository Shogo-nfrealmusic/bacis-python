def calculate_total_price(cart_items):
    total_price = 0
    for cart in cart_items:
        if cart['type'] == 'food':
            total_price += round(cart['price'] * 0.9)
        elif cart['type'] == 'clothes':
            total_price += cart['price'] - 1000
        else:
            total_price += cart['price']
    return total_price
       

cart_items = [
    {'name': 'Tシャツ', 'type': 'clothes', 'price': 2000},
    {'name': 'キャップ', 'type': 'cap', 'price': 8000},
    {'name': 'ランニングシューズ', 'type': 'shoes', 'price': 15000},
    {'name': 'アンダーウェア', 'type': 'clothes', 'price': 4500},
    {'name': 'テニスラケット', 'type': 'sports goods', 'price': 8000},
    {'name': 'スポーツドリンク', 'type': 'food', 'price': 150}
]
total_price = calculate_total_price(cart_items)
print(total_price)