import requests

# static request

r = requests.get('https://www.thecocktaildb.com/api/json/v1/1/search.php?s=Gin%20Tonic')
drink = r.json()['drinks'][0]

for item in drink:
    print('NAME:\n', drink['strDrink'], '\nINSTRUCTIONS:\n', drink['strInstructions'], '\nIMAGE:\n', drink['strImageSource'])