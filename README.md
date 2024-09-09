# cis6930fa24 -- Assignment0 

**Name:**  Archit Mittal
**Email:** mittalarchit@ufl.edu
**UFID:** 58408828

# Assignment Description 

This assignment involves creating a Python script that fetches data from the FBI Wanted API or from a local JSON file. It processes the data into thorn-separated values and outputs it to a text file. The script includes functionalities to fetch, parse, and store FBI wanted person data in a structured format.

## Installation Instructions
Ensure that you have a `pipenv` installed. If not, install it using command :- `pip install pipenv`. Now, set up the project environment with command:

# How to install
To install the required dependencies, run the following command:
```
pipenv install -e
```
# How to run
To fetch data from the FBI API by specifying the page number, use the following command:
```
pipenv run python main.py --page <page_number>
```
To read data from a local JSON file, use this command:
```
pipenv run python main.py --file <file_location>
```
# Functions
```get_data(page):```
This function fetches data from the FBI API for a specified page number. It returns the JSON response if the request is successful, otherwise returns None.

```get_data_from_file(filepath):```
This function reads data from a specified JSON file path and writes it to the file. It handles errors like file not found and returns the data.

```parse_data(data):```
This function takes the FBI API data and converts it into thorn-separated values (title, subjects, field_offices). It returns a list of thorn-separated strings.

```main(page=None, file=None):```
This is the main function that handles either API fetching or file-based input depending on the arguments passed. It processes the data and writes the thorn-separated output to a text file called result.txt.

# Bugs and Assumptions
* The API fetching function assumes the FBI API is available and responsive. 
* If the API goes down, data cannot be fetched.
* The function ```get_data_from_file``` assumes that the file structure is similar to the API output. Any deviation in structure may cause parsing errors.
* The script currently fetches data from page-based API responses but does not handle pagination beyond the current page specified.
* Ensure that the JSON data file exists when using the --file option, as the script does not create files if they are not found.
