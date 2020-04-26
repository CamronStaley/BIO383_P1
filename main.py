import functionCalls

bh_directory = "Data/Black Hair"
bh_data = functionCalls.parse_file(bh_directory)
functionCalls.display_table(bh_data)

# only run if you want a cvs file
functionCalls.data_to_cvs(bh_data, 'bh_datafile.csv')

