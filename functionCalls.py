import os
import csv


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
            if words[0] != '#':
                words.insert(0, file)
                to_return.append(words)
    header = ["filename", "rsid", "chromosome", "position", "genotype"]
    to_return.insert(0, header)
    return to_return


# takes in a list of data and a name for the file and creates a cvs file containing that list
def data_to_cvs(data, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
