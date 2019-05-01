# Basketball Team Stats Tool

In this project you will be writing a program that reads from the "constants" data (`PLAYERS` and `TEAMS`) in `constants.py`. This data will need to be translated into a new collection of your choosing and the fields need to be changed to something that makes more sense for Python to do its comparisons.

## Project Requirements

### Meets Expectations

- Create a new file seperate from _constants.py_ called _app.py_ or _application.py_.
- Import and use the data from _constants.py_ in your program, but do not change the data in _constants_.
- Catch exceptions and errors
- Function calls, print statements, or any calculated execution logic should be wrapped inside a Dunder Main statement for your script.
- Clean the data from _constants.py_ when adding it to the new data structure: player experience should be boolean True or False instead of a string; player height should be an int; guardians should be split into a list of strings
- Assign players to each team so the teams are evenly balanced by total players. The same player cannot be assigned to multiple teams.
- Create a clear and readable menu for the user
- The team stats should display the team's name, the total number of players, and the player names as a comma-separated string (not a list object)

#### Exceeds Expectations

- Clean the guardians string so that it becomes a List of strings. Remove the and between the names and storing each guardian in a List together for that player.
- Also balance players in a way that also ensures teams have equal numbers of experienced vs inexperienced players.
- The user should be re-prompted with the main menu until they decide to "Quit the program".
- The stats should also display the number of experienced vs inexperienced players, average height, and all of the guardians as a comma-separated list.

## What I Learned

I struggled a bit with this project, especially the logic to combine the TEAMS list and the PLAYERS list of dictionaries. Balancing the teams was difficult also. I had to research the issue and them take the suggested code and modify it in my code (see comments in the code). I also learned:

- List comprehensions
- Tuple unpacking (returning a tuple in a function and then using that as the input to another function using *func)
- Zip to combine two iterables
- How to use deepcopy(); I had a bug where I set a variable to be a copy of PLAYERS. However, when I tried to modify the dictionaries inside of the copy, it changed the original. Deepcopy resolved this.
- What dunder main does and why you would use it
