#import requests
#endpoint = "https://production.suggestic.com/graphql"
#api_key = "65ed059d39c7a036bc1713430c453a5220e62fb3"
#query_params = {"api_key" : api_key}
#response = requests.get(endpoint, params = query_params)



#print(response.status_code)
#print(response.reason)
#print(response.text)

import requests

# HTTP Headers including sg-user for especific user context
headers = {
    "Authorization": "Token 7b9f6fd852faba099be1984c97124b7f8d776f26",
    "sg-user": "e084268c-5487-4f35-9d74-9ce41de3992b"
}
# GraphQL query
query = """{ myProfile { id programName } }"""

# Make request
r = requests.post(
    "https://staging.suggestic.com/graphql",
    headers=headers,
    json={"query": query}
)

# print json response
print(r.json())