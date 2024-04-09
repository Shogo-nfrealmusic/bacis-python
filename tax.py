def calculate_total_with_tax(cart_items, tax_rate):
    total_price = 0
    for cart in cart_items:
        total_price += cart['price']
    total_price *= (1 + tax_rate)
    return round(total_price)
       

cart_items = [
    {'name': 'Tシャツ', 'type': 'clothes', 'price': 2000},
    {'name': 'キャップ', 'type': 'cap', 'price': 8000}
]
tax_rate = 0.1
total_with_tax = calculate_total_with_tax(cart_items, tax_rate)
print(total_with_tax)