from flask import Flask, render_template, request, redirect, url_for
# from test_recipes import recipes, getRecipe
from API import getMatchingRecipes, getRecipe

app = Flask(__name__)

ingredients = []

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html', ingredients=ingredients)

@app.route('/add/', methods=['POST'])
def home_add():
    ingredient = request.form['ingredient']
    if ingredient:
        ingredients.append(ingredient)
    return redirect(url_for('home'))

@app.route('/clear/', methods=['GET', 'POST'])
def home_clear():
    ingredients.clear()
    return redirect(url_for('home'))

@app.route('/results')
def results():
    if not ingredients:
        return redirect(url_for('home'))
    recipes = getMatchingRecipes(ingredients)
    print('-------before--------')
    print(recipes)
    return render_template('results.html', ingredients=ingredients, recipes=recipes)

@app.route('/recipe/<id>')
def recipe(id):
    recipe = getRecipe(id)
    if not recipe:
        print('Error: no recipe found with id {}'.format(id))
        exit(1)

    return render_template('recipe.html', recipe=recipe)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
