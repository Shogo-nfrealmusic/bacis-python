def calculate_points(total_price, user):
    point_rate = 0.01
    points = total_price * point_rate
    if user['status'] == 'premium':
        points += total_price * point_rate
    return round(points)
    

total_price = 10000

user = {'user_id': 1, 'status': 'basic'}
points = calculate_points(total_price, user)
print('入力1：会員ステータスがbasicの場合')
print(points)

print('-----------------------------')

user = {'user_id': 2, 'status': 'premium'}
points = calculate_points(total_price, user)
print('入力1：会員ステータスがpremiumの場合')
print(points)