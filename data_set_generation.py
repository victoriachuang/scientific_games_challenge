import json
import random

# write to file: name, birth year, death year
# generate birth and death years between 1900 and 2000
# death year must be equal to or after birth year

MIN_YEAR = 1900
MAX_YEAR = 2000
DATA_SIZE = 1000

with open("data.json", "w") as outfile:
	outfile.write("[")
	for i in range(0, DATA_SIZE):	
		start = int((random.random() * (MAX_YEAR - MIN_YEAR))) + MIN_YEAR
		end = int(((MAX_YEAR - start) * random.random())) + start

		# need to separate each object
		json.dump({"name": "hello kale chips", "birth_year": start, "death_year": end}, outfile, indent=4)
		if i < DATA_SIZE - 1:
			outfile.write(",\n")
		else:
			outfile.write("]")