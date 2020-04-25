import os
import csv
from prettytable import PrettyTable

rsids = set(['rs12913832', 'rs1393350', 'rs1800407', 'rs1805008', 'rs7495174', 'rs16891982'])


# reads in and parses all files in the directory
# formats the data as a list containing filename, rsid, chromosome, position, genotype
# then returns the list as a 2d list each row holding an element containing a different list
def parse_file(directory):
    to_return = []
    for file in os.listdir(directory):
        filename = directory + '/' + file
        f = open(filename, "r")
        text = f.readlines()
        for line in text:
            words = line.split()
            if words[0] != '#' and words[0] in rsids:
                words.insert(0, file)
                to_return.append(words)
    return to_return


# takes in a list of data and a name for the file and creates a cvs file containing that list
def data_to_cvs(data, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)


# takes in a list of data and displays neatly
def display_table(data):
    table = PrettyTable()
    table.field_names = ["filename", "rsid", "chromosome", "position", "genotype"]
    for x in data:
        table.add_row(x)
    print(table)
