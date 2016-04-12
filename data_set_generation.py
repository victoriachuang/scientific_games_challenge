import json

# write to file: name, birth year, death year
with open("data.json", "w") as outfile:
	for i in range(0, 1000):	
		start = int((random.random() * 100)) + 1900
		end = int(((2000 - start) * random.random())) + start

		# need to separate each object
		json.dump({"name": "hello kale chips", "birth_year": start, "death_year": end}, outfile, indent=4)