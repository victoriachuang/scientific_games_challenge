import json

# write to file: name, birth year, death year

# open json file
with open('data_set.json') as data_file:
	data = json.load(data_file)

# create dictionary => key is each year
birth_year_tally = {}
for i in range(1900, 2001):
	birth_year_tally[i] = 0

# "tally" years that each person was alive
# traverse through list of birth year and death year
# traverse through hash
# if key >= birth year and key <= death year, key[i]++
for key in birth_year_tally:
	if key >= data["birth_year"] and key <= data["death_year"]:
		birth_year_tally[key] += 1

# return key with max value