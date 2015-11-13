import json
from sets import Set

with open('train.json') as data_file:    
    data = json.load(data_file) # list of all recipes 

lengthTrain = len(data)

ingredientsSet = set()
cuisineSet = set()

for i in xrange(0, lengthTrain):
	cuisineSet.add(data[i]['cuisine']) # only 20 distinct cuisines
	for e in data[i]['ingredients']:
 		ingredientsSet.add(e) # 6714 ingredients
 
masterListIngre = list(ingredientsSet) # list of all ingredients in our recipe data file
masterListCuisine = list(cuisineSet) # list of all cuisines in our data file

##################################################
Dict = {} # key: cuisine, val: all its ingredients 
for a in xrange(0, lengthTrain):
	for b in masterListCuisine:
		if b == data[a]['cuisine']:
			Dict[b] = data[a]['ingredients']

##################################################

print Dict['greek']#[0]
print Dict['thai']

data_file.close()