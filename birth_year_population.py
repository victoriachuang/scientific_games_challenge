import json
import operator

MIN_YEAR = 1900
MAX_YEAR = 2000

# open json file
with open('data.json') as data_file:
	data = json.load(data_file)

# create dictionary => key is each year, initialize each value to 0
birth_year_tally = {}
for i in range(MIN_YEAR, MAX_YEAR + 1):
	birth_year_tally[i] = 0

# "tally" years that each person was alive
for person in data:
	for key in birth_year_tally:
		if key >= person["birth_year"] and key <= person["death_year"]:
			birth_year_tally[key] += 1

# return key with max value
mode_year = max(birth_year_tally.iteritems(), key=operator.itemgetter(1))[0]
print mode_year