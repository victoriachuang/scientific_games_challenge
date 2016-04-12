# scientific_games_challenge

Challenge: Given a list of people with their birth and end years, all between 1900 and 2000, find the year with the most number of people alive.

## Use

Run `python main.py`.

## Design decisions

In both the data generation and mode year scripts, I factored out certain variables to be constants, such as the maximum and minimum years, to improve readability. This would also allow for easy adjustments in the event that we want to change the year range or the sample data size.

## Data generation

In `data_set_generation.py`, I create a JSON file to hold sample data, which `birth_year_population.py` will read from.
I chose to generate the data set as an array of JSON, since that’s how many APIs feed their data.
Because the birth and end years are contained in the range of 1900 to 2000, I decided to not make realistic lifespans a priority; there would be a lot of overlapping lifespan years and the program would return more than half of the dates available.
However, the end year must be greater than or equal to the birth year. 

## Birth year count

I structured my tally of when each person was alive as a dictionary, as opposed to an array, for readability; the key could be stored as the year itself, without having to convert indices into the year.

## Possible improvements

