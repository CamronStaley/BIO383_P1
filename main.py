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
rsids_dict = functionCalls.count_avg_genotypes(bh_data)
rsids_dict = functionCalls.get_most_occur(rsids_dict)
for x in rsids_dict:
    print(x)
    print(rsids_dict.get(x).most_occur)
