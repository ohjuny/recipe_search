stock_img = 'stock_food.jpeg'

recipes = [
    {
        'id': 0,
        'name': 'Recipe 0',
        'ingredients': ['ingA', 'ingB', 'ingC'],
        'text': 'some description about how to actually make the dish',
        'rating': 10,
        'time': 30,
        'image': stock_img
    },
    {
        'id': 1,
        'name': 'Recipe 1',
        'ingredients': ['ingB', 'ingC'],
        'text': 'some description about how to actually make the dish',
        'rating': 8,
        'time': 15,
        'image': stock_img
    },
    {
        'id': 2,
        'name': 'Recipe 2',
        'ingredients': ['ingA', 'ingC', 'ingD'],
        'text': 'some description about how to actually make the dish',
        'rating': 5,
        'time': 50,
        'image': stock_img
    },
    {
        'id': 3,
        'name': 'Recipe 3',
        'ingredients': ['ingA', 'ingB', 'ingC', 'ingD'],
        'text': 'some description about how to actually make the dish',
        'rating': 8,
        'time': 10,
        'image': stock_img
    },
    {
        'id': 4,
        'name': 'Recipe 4',
        'ingredients': ['ingA', 'ingB', 'ingC'],
        'text': 'some description about how to actually make the dish',
        'rating': 9,
        'time': 90,
        'image': stock_img
    },
]

def getRecipe(id):
    id = int(id)
    for recipe in recipes:
        if id == recipe['id']:
            return recipe
    return None
