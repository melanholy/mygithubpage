import json

foodInfos = [
    {'name': "Ribollita da Delfina", 'price': 1.50, 'path': '0.jpg'},
    {'name': "Martinez cocktail", 'price': 4, 'path': '1.jpg'},
    {'name': "Salmon teriyaki", 'price': 10, 'path': '2.jpg'},
    {'name': "Beef tongue with green onion sauce", 'price': 14, 'path': '3.jpg'},
    {'name': "Ramos gin fizz", 'price': 531, 'path': '4.jpg'},
    {'name': "Ice cream sundae", 'price': 7.30, 'path': '5.jpg'},
    {'name': "Belgian chocolate truffle cake", 'price': 100, 'path': '6.jpg'},
    {'name': "Pasta con le sarde", 'price': 21, 'path': '7.jpg'},
    {'name': "Chicken cordon bleu with wild rice and ratatouille", 'price': 5.99, 'path': '8.jpg'},
    {'name': "Buttermilk pancakes", 'price': 5, 'path': '9.jpg'},
    {'name': "Pilaf", 'price': 88, 'path': '10.jpg'},
    {'name': "Bee's Knees", 'price': 213, 'path': '11.jpg'},
    {'name': "Pineapple and coconut extravaganza dessert", 'price': 6, 'path': '12.jpg'}
]

with open('get.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(foodInfos))
