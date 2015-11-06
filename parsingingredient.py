import json
from sets import Set

with open('train.json') as data_file:    
    data = json.load(data_file) # list of all recipes 

lengthTrain = len(data)

ingredientsSet = set()

for i in xrange(0, lengthTrain):
	for e in data[i]['ingredients']:
 		ingredientsSet.add(e)


masterListIngre = list(ingredientsSet)



# print(len(data)) # num of recipes = 39774

# ingredients = data[0]['ingredients']
# cuisine = data[0]['cuisine']

# print(ingredients[0])
# print(cuisine)



data_file.close()
