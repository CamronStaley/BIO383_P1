import functionCalls

bh_directory = "Data/Black Hair"
bh_data = functionCalls.parse_file(bh_directory)
functionCalls.display_table(bh_data)

# only run if you want a csv file
functionCalls.data_to_cvs(bh_data, 'bh_datafile.csv')

genotype_dict = functionCalls.count_genotypes(bh_data)
for items in genotype_dict.geno.items():
    print(items)

# prints the most frequent genotypes for each rsid
genotype_avg_dict = functionCalls.count_avg_genotypes(bh_data)
for items in genotype_avg_dict.items():
    print(items)