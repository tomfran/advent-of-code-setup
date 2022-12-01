# Advent of code setup

Jump start your AoC experience with this repo.

## Setup
Run `make setup`, this will create the `inputs` directory, and the `session.cookie` file, please rememeber to fill the latter with you session cookie to auto download inputs, add a newline after it, just in case.

To find it on Chrome: right click, inspect, Application tab, Storage, Coookies, session. 

## Creating a new solution

```make new``` creates a new file for today, it checks for the files in `src/` and creates the "next int" one. On the first run it will create `01.py`, later `02.py`, and so on.

A new solution is initialized as follows: 
```
from utils.api import get_input

input_str = get_input(1)

# WRITE YOUR SOLUTION HERE
```
The `get_input` function takes a day and returns the content of the input for that day, this internally makes a request to obtain the input if it is not found on disk. 

## Running a new solution

From the main directory, run `python src/<DAY>.py`.

## Pretty README
`make readme` creates a cool `README.md` file with a list of the soutions in the source directory, with working links. Note that this original readme will be overwritten.
If you want to use this, please edit `src/utils/build_md.py` with a correct repository link.
Also, the `parse` method could be extended to display what you want for each solution. For instance, by uncommenting line 8, and renaming your files like `DAY_Cool_Problem_name.py`, you will get a list entry like `DAY. Cool Problem name`.
