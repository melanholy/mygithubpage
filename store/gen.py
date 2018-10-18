import json

foodInfos = [
    {'name': "Ribollita da Delfina", 'price': 1.50, 'imagePath': '0.jpg'},
    {'name': "Martinez cocktail", 'price': 4, 'imagePath': '1.jpg'},
    {'name': "Salmon teriyaki", 'price': 10, 'imagePath': '2.jpg'},
    {'name': "Beef tongue with green onion sauce", 'price': 14, 'imagePath': '3.jpg'},
    {'name': "Ramos gin fizz", 'price': 531, 'imagePath': '4.jpg'},
    {'name': "Ice cream sundae", 'price': 7.30, 'imagePath': '5.jpg'},
    {'name': "Belgian chocolate truffle cake", 'price': 100, 'imagePath': '6.jpg'},
    {'name': "Pasta con le sarde", 'price': 21, 'imagePath': '7.jpg'},
    {'name': "Chicken cordon bleu with wild rice and ratatouille", 'price': 5.99, 'imagePath': '8.jpg'},
    {'name': "Buttermilk pancakes", 'price': 5, 'imagePath': '9.jpg'},
    {'name': "Pilaf", 'price': 88, 'imagePath': '10.jpg'},
    {'name': "Bee's Knees", 'price': 213, 'imagePath': '11.jpg'},
    {'name': "Pineapple and coconut extravaganza dessert", 'price': 6, 'imagePath': '12.jpg'}
]

with open('get.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps({'totalCount': 1000, 'items': foodInfos}))
