Assignment 3: Analyzing Pokémon Data
Overview
This assignment involves analyzing a CSV file containing Pokémon data to determine the most common species and ability1. The provided Python script reads the CSV file, processes the data, and outputs the most common species and ability1.

Files
assignment3.py: The main Python script that performs the data analysis.
pokemon_data.csv: The CSV file containing Pokémon data.

Script Explanation
The script performs the following steps:

Read the CSV file: Opens the pokemon_data.csv file in read mode and reads its contents.
Split the contents by lines: Splits the file contents into individual lines.
Parse the CSV data: Splits each line by commas to create a list of columns.
Extract the header: Identifies the column names from the first row.
Find column indices: Determines the indices of the species and ability1 columns.
Create lists of species and ability1: Extracts the species and ability1 values from the CSV data, excluding the header.
Count occurrences: Uses dictionaries to count the occurrences of each species and ability1.
Find the most common values: Identifies the most common species and ability1 by finding the maximum values in the dictionaries.
Output the results: Prints the most common species and ability1.
