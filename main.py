from Bio import SeqIO
import os

directory = "Data/Black Hair"

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    print(filename)



