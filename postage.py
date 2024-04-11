def is_shipping_free(cart_items, user):
    total_price = 0
    for cart in cart_items:
        total_price += cart['price']
    if total_price >= 10000:
        is_discount_postage = True
    elif total_price >= 5000 and user['status'] == 'premium':
        is_discount_postage = True
    else:
        is_discount_postage = False
    return  is_discount_postage
        

cart_items = [
    {'id': 2, 'name': 'ヘッドホン', 'price': 5500},
    {'id': 4, 'name': '乾電池', 'price': 100}
]
user = {'user_id': 2, 'name': 'John', 'status': 'basic'}
free_shipping = is_shipping_free(cart_items, user)
print('入力1：送料有料になる金額の場合')
if free_shipping:
    print("配送料は無料です")
else:
    print("配送料がかかります")

print('-----------------------------')

cart_items = [
    {'id': 1, 'name': 'ゲームソフト', 'price': 5000}
]
user = {'user_id': 2, 'name': 'John', 'status': 'premium'}
free_shipping = is_shipping_free(cart_items, user)
print('入力2：送料無料になる金額の場合')
if free_shipping:
    print("配送料は無料です")
else:
    print("配送料がかかります")
