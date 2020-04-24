from Bio import SeqIO
import os
import sn
from boto import sns
import functionCalls

black_directory = "Data/Black Hair"
bh_data = functionCalls.parse_file(black_directory)
print(bh_data[0])
