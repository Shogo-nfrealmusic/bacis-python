def add_item_review(user, item, rating, review_text, reviews):
    new_review = {
        'user_id': user['user_id'],
        'item_id': item['id'],
        'rating': rating,
        'review_text': review_text
        
    }
    reviews.append(new_review)
    return reviews

reviews = [
    {'user_id': 1, 'item_id': 2, 'rating': 4, 'review_text': '音質が期待通り'},
    {'user_id': 3, 'item_id': 3, 'rating': 2, 'review_text': '画面がすぐに割れてしまった'}
]
user = {'user_id': 2, 'name': 'John'}
item = {'id': 1, 'name': 'ゲームソフト', 'price': 5000}
rating = 5
review_text = '時間を忘れてしまうほど面白い'
reviews = add_item_review(user, item, rating, review_text, reviews)
for review in reviews:
  print(review)
