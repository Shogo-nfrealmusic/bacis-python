def apply_coupon(coupon_code, total_price, coupons):
    for coupon in coupons:
        if coupon['code'] == coupon_code:
            discount = total_price * coupon['discount_percentage']
            total_price -= discount
        return round(total_price)

coupons = [
    {"code": "SAVE10", "discount_percentage": 0.1},
    {"code": "SAVE20", "discount_percentage": 0.2},
    {"code": "SAVE30", "discount_percentage": 0.3}
]
total_price = 12000
coupon_code = "SAVE10"
discount_total_price = apply_coupon(coupon_code, total_price, coupons)
print('入力1：10%割引になる場合')
print(discount_total_price)

print('-----------------------------')

coupon_code = "SAVE40"
discount_total_price = apply_coupon(coupon_code, total_price, coupons)
print('入力2：クーポンコードが該当しない場合')
print(discount_total_price)