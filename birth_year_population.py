import json
import operator

# write to file: name, birth year, death year

# open json file
with open('data_set.json') as data_file:
	data = json.load(data_file)

# create dictionary => key is each year, initialize each value to 0
birth_year_tally = {}
for i in range(1900, 2001):
	birth_year_tally[i] = 0

# "tally" years that each person was alive
for person in data:
	for key in birth_year_tally:
		if key >= person["birth_year"] and key <= person["death_year"]:
			birth_year_tally[key] += 1

# return key with max value
max_year = max(birth_year_tally.iteritems(), key=operator.itemgetter(1))[0]
print max_year