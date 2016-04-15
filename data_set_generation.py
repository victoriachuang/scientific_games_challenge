import json
import random

# write to file: name, birth year, death year
# generate birth and death years between 1900 and 2000
# death year must be equal to or after birth year

MIN_YEAR = 1900
MAX_YEAR = 2000
DATA_SIZE = 1000

first_names = ['Noah','Liam','Jacob','Mason','William','Ethan','Michael','Alexander','Jayden','Daniel','Elijah','Aiden','James','Benjamin','Matthew','Jackson','Logan','David','Anthony','Joseph','Joshua','Andrew','Lucas','Gabriel','Samuel','Christopher','Sophia','Emma','Olivia','Isabella','Ava','Mia','Emily','Abigail','Madison','Elizabeth','Charlotte','Avery','Sofia','Chloe','Ella','Harper','Amelia','Aubrey','Addison','Evelyn','Natalie','Grace','Hannah','Zoey','Victoria','Lillian']

last_names = ['Smith','Johnson','Williams','Brown','Jones','Miller','Davis','Garcia','Rodriguez','Wilson','Martinez','Anderson','Taylor','Thomas','Hernandez','Moore','Martin','Jackson','Thompson','White','Lopez','Lee','Gonzalez','Harris','Clark','Lewis','Robinson','Walker','Perez','Hall','Young','Allen','Sanchez','Wright','King','Scott','Green','Baker','Adams','Nelson']

with open("data.json", "w") as outfile:
	outfile.write("[")
	for i in range(0, DATA_SIZE):	
		full_name = random.choice(first_names) + ' ' + random.choice(last_names)	
		start = int((random.random() * (MAX_YEAR - MIN_YEAR))) + MIN_YEAR
		end = int(((MAX_YEAR - start) * random.random())) + start

		# need to separate each object
		json.dump({"name": full_name, "birth_year": start, "death_year": end}, outfile, indent=4)
		if i < DATA_SIZE - 1:
			outfile.write(",\n")
		else:
			outfile.write("]")