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

# return all keys with max value
# find key with the max value and append all keys with the same value to a result list
max_population_year = max(birth_year_tally, key=birth_year_tally.get)
all_max_keys = []
for year in birth_year_tally:
	if birth_year_tally[year] == birth_year_tally[max_population_year]:
		all_max_keys.append(year)

print all_max_keys