#import requests
#endpoint = "https://production.suggestic.com/graphql"
#api_key = "65ed059d39c7a036bc1713430c453a5220e62fb3"
#query_params = {"api_key" : api_key}
#response = requests.get(endpoint, params = query_params)



#print(response.status_code)
#print(response.reason)
#print(response.text)

import requests

def getRecipe(id):
    recipes = getRecipes()
    for recipe in recipes:
        if recipe['id'] == id:
            return recipe
    return None

def getRecipes():
    # HTTP Headers including sg-user for especific user context
    headers = {
        "Authorization": "Token 7b9f6fd852faba099be1984c97124b7f8d776f26",
        "sg-user": "e084268c-5487-4f35-9d74-9ce41de3992b"
    }
    # GraphQL query
    query = """{
    popularRecipes {
        edges {
        node {
            id
            name
            totalTime
            rating
            ingredients {
                name
            }
            instructions
            mainImage
        }
        }
    }
    }"""

    # Make request
    r = requests.post(
        "https://staging.suggestic.com/graphql",
        headers=headers,
        json={"query": query}
    )

    recipes = []
    for node in r.json()['data']['popularRecipes']['edges']:
        recipe = {
            'id': node['node']['id'],
            'name': node['node']['name'],
            'ingredients': set([obj['name'].lower() for obj in node['node']['ingredients']]),
            'time': node['node']['totalTime'],
            'rating': node['node']['rating'],
            'image': node['node']['mainImage'],
            'instructions' : node['node']['instructions']
        }
        recipes.append(recipe)

    # print(recipes)
    return recipes

def getMatchingRecipes(ingredients):
    recipes = getRecipes()
    results = []
    for ing in ingredients:
        for recipe in recipes:
            if ing in recipe['ingredients']:
                results.append(recipe)
                break
    return results
