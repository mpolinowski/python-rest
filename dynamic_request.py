import requests
from pathlib import Path

# user defined search request

def get_drink(drink):
    url = f'https://www.thecocktaildb.com/api/json/v1/1/search.php?s={drink}'
    r = requests.get(url)
    drink = r.json()['drinks'][0]
    with open(results_path, 'a') as file:
        file.write(f"{drink['strDrink']}, {drink['strInstructions']}, {drink['strImageSource']}"+'\n')
    return


# prepare CSV file to store results

results_path = Path('files/drinks.csv')

content = "NAME, INSTRUCTIONS, IMAGE"

if not results_path.exists():
    with open(results_path, 'w') as file:
        file.write("NAME, INSTRUCTIONS, IMAGE\n")

# run search

get_drink(drink='Daiquiri')