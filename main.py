from functionCalls import FunctionCalls
from functionCalls import Genotype

bh_directory = "Data/Black Hair"
rh_directory = "Data/Red Hair"
black_hair = FunctionCalls()
red_hair = FunctionCalls()

black_hair.parse_file(bh_directory)
red_hair.parse_file(rh_directory)

black_hair.display_table()
red_hair.display_table()

black_hair.count_genotypes()
red_hair.count_genotypes()

print("Black Hair")
black_hair.display_total_genos()
print()
print("Red Hair")
red_hair.display_total_genos()
print()

black_hair.count_geno_by_rsid()
red_hair.count_geno_by_rsid()

print("Black Hair")
black_hair.display_geno_by_rsid()
print()
print("Red Hair")
red_hair.display_geno_by_rsid()
print()

black_hair.get_most_occur()
red_hair.get_most_occur()

print("Black Hair")
black_hair.display_most_occur()
print()
print("Red Hair")
red_hair.display_most_occur()
print()

black_hair.compare_results("Black", red_hair, "Red")
