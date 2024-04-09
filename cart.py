def get_cart_message(cart_items):
    if len(cart_items) == 0:
        return 'カートに商品がありません。お買い物をお楽しみください。'
    else:
        return '購入手続きを進めるか、引き続きお買い物をお楽しみください。'

cart_items = [
    {'name': 'Tシャツ', 'type': 'clothes', 'price': 2000},
    {'name': 'キャップ', 'type': 'cap', 'price': 8000}
]
message = get_cart_message(cart_items)
print('入力1：カートに商品がある場合')
print(message)

print('-----------------------------')

cart_items = []
message = get_cart_message(cart_items)
print('入力2：カートに商品がない場合')
print(message)
