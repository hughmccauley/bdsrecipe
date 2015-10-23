import json

with open('train.json') as data_file:    
    data = json.load(data_file)

matrix = [[]]



for i in data:

print(data[0])

print(len(data)) # num of recipes = 39774

ingredients = data[0]['ingredients']
cuisine = data[0]['cuisine']

print(ingredients[0])
print(cuisine)

