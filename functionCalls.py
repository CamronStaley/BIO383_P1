import os


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
    return to_return
