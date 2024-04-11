def calculate_large_discounts(price, quantity):
    if quantity >= 20:
        discount_rate = 0.10
    elif quantity >= 10:
        discount_rate = 0.05
    else:
        discount_rate = 0.0
    
    discounted_price = price * (1 - discount_rate)
    total_price = discounted_price * quantity
    return round(total_price)
        

price = 100
quantity = 20
total_price = calculate_large_discounts(price, quantity)
print('入力1：購入数が20個の場合')
print(total_price)

print('-----------------------------')

quantity = 10
total_price = calculate_large_discounts(price, quantity)
print('入力2：購入数が10個の場合')
print(total_price)

print('-----------------------------')

quantity = 9
total_price = calculate_large_discounts(price, quantity)
print('入力3：購入数が9個の場合')
print(total_price)
