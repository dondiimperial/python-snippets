"""Snippets for reading a csv file and converting each line into a python list"""
import csv
import fileinput

"""The path to the csv file"""
FILE_PATH = ''


### Snippet for using the csv module to read the file ###
# Open the file
with open(FILE_PATH) as csvfile:
    # get a reader object for the file.
    csv_lines = csv.reader(csvfile)
    # Iterate over each row in the csv file
    for row in csv_lines:
        # row is a list where each element is a column in the current row from the csv file.
        print(row)

### Snippet for reading line by line. ###
# Read file line by line
for line in fileinput.input(FILE_PATH):
    # The first line is normally the header and something we are not interested in.
    if not fileinput.isfirstline():
        # csv.reader returns a list of lists. When reading a single line get the first (only) element.
        line_parsed = [y.strip() for y in [x for x in csv.reader([line])][0]]
