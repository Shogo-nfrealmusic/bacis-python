def display_product_and_color(items, colors):
    for item in items:
        for color in colors:
            print(item['name'] + ': '+ color)
        

items = [
    {'name': 'Tシャツ', 'type': 'clothes', 'price': 2000},
    {'name': 'キャップ', 'type': 'cap', 'price': 8000}
]
colors = ['Red', 'Blue', 'Black']
display_product_and_color(items, colors)
