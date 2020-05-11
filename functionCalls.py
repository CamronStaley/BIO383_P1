import os
import csv
from prettytable import PrettyTable

# const locations of information in the list
FILE_LOC = 0  # filename location
RSID_LOC = 1  # rsid location
CHRO_LOC = 2  # chromosome location
POS_LOC = 3  # position of the SNP location
GENO_LOC = 4  # genotype location


class Genotype:
    def __init__(self):
        self.most_occur = ''
        self.average = 0
        self.geno = {
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


# holds all the actions we are going to be doing
class FunctionCalls:

    def __init__(self):
        self.data = []
        self.geno = Genotype()
        self.rs12913832 = Genotype()
        self.rs1393350 = Genotype()
        self.rs1800407 = Genotype()
        self.rs1805008 = Genotype()
        self.rs7495174 = Genotype()
        self.rs16891982 = Genotype()
        self.rsids = {
            'rs12913832': self.rs12913832,
            'rs1393350': self.rs1393350,
            'rs1800407': self.rs1800407,
            'rs1805008': self.rs1805008,
            'rs7495174': self.rs7495174,
            'rs16891982': self.rs16891982
        }

    # reads in and parses all files in the directory
    # formats the data as a list containing filename, rsid, chromosome, position, genotype
    # then stores as a 2d list
    def parse_file(self, directory):
        for file in os.listdir(directory):
            filename = directory + '/' + file
            f = open(filename, "r")
            text = f.readlines()
            for line in text:
                words = line.split()
                if words[0] in self.rsids:
                    words.insert(0, file)
                    self.data.append(words)

    # displays data neatly
    def display_table(self):
        table = PrettyTable()
        table.field_names = ["filename", "rsid", "chromosome", "position", "genotype"]
        for x in self.data:
            table.add_row(x)
        print(table)

    # takes in another function calls object and prints a table comparison of the results
    def compare_results(self, hairColor, other, otherHairColor):
        table = PrettyTable()
        table.field_names = ["Hair color", "RSID", "Genotype"]
        for rsid in self.rsids:
            temp = [hairColor, rsid, self.rsids[rsid].most_occur]
            table.add_row(temp)
            temp = [otherHairColor, rsid, other.rsids[rsid].most_occur]
            table.add_row(temp)
        print(table)

    # compares the genotypes of a given rsid and two hair colors
    def compare_genos_by_rsid(self, rsid, self_color, other, other_color):
        table = PrettyTable()
        table.field_names = ["Genotype", self_color, other_color]
        for genos in self.rsids[rsid].geno:
            temp = [genos, self.rsids[rsid].geno[genos], other.rsids[rsid].geno[genos]]
            table.add_row(temp)
        print(table)

    # takes the list of data and then counts all of the individual genotype pairs and stores it
    def count_genotypes(self):
        for genotype in self.data:
            if genotype[GENO_LOC] in self.geno.geno:
                self.geno.geno[genotype[GENO_LOC]] += 1

    # displays the count of the total number of each genotype
    def display_total_genos(self):
        for genotype in self.geno.geno.items():
            print(genotype)

    # counts and stores the count of each genotype in a each rsid and the highest occurrences
    def count_geno_by_rsid(self):
        for genotype in self.data:
            rsid = genotype[RSID_LOC]
            geno = genotype[GENO_LOC]
            if geno in self.rsids[rsid].geno:
                self.rsids[rsid].geno[geno] += 1

        for rsid in self.rsids:
            max_count = 0
            for key in self.rsids[rsid].geno:
                if self.rsids[rsid].geno[key] > max_count:
                    max_count = self.rsids[rsid].geno[key]
                    self.rsids[rsid].average = max_count

    # displays the occurrences of genotypes by each rsid
    def display_geno_by_rsid(self):
        for rsid in self.rsids:
            print(rsid)
            for item in self.rsids[rsid].geno.items():
                print(item)

    # stores a string of the most common occurrences
    def get_most_occur(self):
        for rsid in self.rsids:
            flag = True
            for key in self.rsids[rsid].geno:
                if self.rsids[rsid].geno[key] >= self.rsids[rsid].average:
                    if not flag:
                        self.rsids[rsid].most_occur += ' or ' + key
                    else:
                        self.rsids[rsid].most_occur += key
                        flag = False

    # prints the most common occurrences of genotypes in each rsids
    def display_most_occur(self):
        for rsid in self.rsids:
            print(rsid + " " + self.rsids[rsid].most_occur)

