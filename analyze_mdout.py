import os
# Open the file for reading
filename = os.path.join('data', '03_Prod.mdout')
f = open(filename, 'r')
# Read the data in the file.
data = f.readlines()
f.close()
# Open a file for writing
f_write = open('Etot.txt', 'w+')
f_write.write('Total Energy\n')
# Loop through lines in the file.
for line in data:
    split_line = line.split()
    # Get information from the line
    if 'Etot' in line:
        #print(split_line[2])
        # Get information from the line
        f_write.write(f'{split_line[2]}\n')

        
f_write.close()