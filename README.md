# scientific_games_challenge

Challenge: Given a list of people with their birth and end years, all between 1900 and 2000, find the year with the most number of people alive.

## Use

Run `python main.py`. The script will return an array of the years during which the most people were alive. For readability in the command line, I've printed the return value.

## `main.py`

Inside `main.py`, I've declared a function that takes a JSON file containing a list of names, birth years and end years. The function creates a dictionary of all possible years in a range defined by starting and ending year constants, and initializes the "tally" for each year to 0.

The function then iterates through the JSON file; for each year the each person was alive, the program will increment the count of the number of people alive during that year.

Then, to find the year with the most people alive, we find the key in the birth year tally dictionary with the highest value. However, Python's built-in method to retrieve the key with the maximum value will only return the **first** instance of the maximum value, which could potentially exclude multiple modes. In order to retrieve every instance of the maximum value, we find the key with the maximum value first, and then iterate through the birth year tally dictionary again; for each key whose value matches that of the maximum value, we store the key in a "result" array.

## Data generation

`data_set_generation.py` creates a JSON file containing 1000 records of names, birth years and end years.

Names are randomly selected from arrays of sample names.

The birth and end years are selected using the `random` library, using the minimum year as a "base" and casted as integers.
