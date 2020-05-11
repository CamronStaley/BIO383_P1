from functionCalls import FunctionCalls
from functionCalls import Genotype

bh_directory = "Data/Black Hair"
rh_directory = "Data/Red Hair"
brh_directory = "Data/Brown Hair"
blh_directory = "Data/Blonde Hair"

black_hair = FunctionCalls()
red_hair = FunctionCalls()
brown_hair = FunctionCalls()
blonde_hair = FunctionCalls()


black_hair.parse_file(bh_directory)
red_hair.parse_file(rh_directory)
brown_hair.parse_file(brh_directory)
blonde_hair.parse_file(blh_directory)

black_hair.count_genotypes()
red_hair.count_genotypes()
brown_hair.count_genotypes()
blonde_hair.count_genotypes()

black_hair.count_geno_by_rsid()
red_hair.count_geno_by_rsid()
brown_hair.count_geno_by_rsid()
blonde_hair.count_geno_by_rsid()

black_hair.get_most_occur()
red_hair.get_most_occur()
brown_hair.get_most_occur()
blonde_hair.get_most_occur()

print("Black Hair")
black_hair.display_most_occur()
print()

print("Red Hair")
red_hair.display_most_occur()
print()

print("Brown Hair")
brown_hair.display_most_occur()
print()

print("Blonde Hair")
blonde_hair.display_most_occur()
print()

black_hair.compare_results("Black", red_hair, "Red")

for rsid in black_hair.rsids:
    print(rsid + ': ')
    black_hair.compare_genos_by_rsid(rsid, 'Black', red_hair, 'Red')
    print()
