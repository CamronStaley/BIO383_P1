import os
import csv
from prettytable import PrettyTable


class Genotype:
    geno = {
        'TT': 0,
        'AA': 0,
        'CC': 0,
        'GG': 0,
        'AT': 0,
        'AC': 0,
        'AG': 0,
        'GT': 0,
        'CT': 0,
        'CG': 0
    }


# the rsids we are looking for to compare and keep
rs12913832 = Genotype()
rs1393350 = Genotype()
rs1800407 = Genotype()
rs1805008 = Genotype()
rs7495174 = Genotype()
rs16891982 = Genotype()
rsids = {
    'rs12913832': rs12913832,
    'rs1393350': rs1393350,
    'rs1800407': rs1800407,
    'rs1805008': rs1805008,
    'rs7495174': rs7495174,
    'rs16891982': rs16891982
}

# const locations of information in the list
FILE_LOC = 0  # filename location
RSID_LOC = 1  # rsid location
CHRO_LOC = 2  # chromosome location
POS_LOC = 3   # position of the SNP location
GENO_LOC = 4  # genotype location


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
            if words[0] in rsids:
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


# takes the list of data and then counts all of the individual genotype pairs and returns them as a dictionary
def count_genotypes(data):
    to_return = Genotype()
    for genotype in data:
        if genotype[GENO_LOC] in to_return.geno:
            to_return.geno[genotype[GENO_LOC]] += 1
    return to_return

# returns a dictionary containing the most frequent genotype for each rsid
# TODO: Tiebreaker????
def count_avg_genotypes(data):
    for genotype in data:
        rsid = genotype[RSID_LOC]
        geno = genotype[GENO_LOC]
        if rsid in rsids:
            if geno in rsids[rsid].geno:
                rsids[rsid].geno[geno] += 1
    genotype = {
        'rs12913832': "",
        'rs1393350': "",
        'rs1800407': "",
        'rs1805008': "",
        'rs7495174': "",
        'rs16891982': ""
    }
    for rsid in rsids:
        max_count = 0
        for key in rsids[rsid].geno:
            if rsids[rsid].geno[key] > max_count:
                max_count = rsids[rsid].geno[key]
                genotype[rsid] = key
    
    return genotype
        


        


