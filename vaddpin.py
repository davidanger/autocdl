# This is add Power PIN to verilog model
# Design by Song 2018-09-17
import re

# Input file
infile = open("in.v", "r")

# Output file
outfile = open("out.v", "w")

# Read a line from infile
data = infile.read()
infile.close()

# ADD Power PIN
data = re.sub(r'(module .+)\);\n', '\g<1> VDD, VSS, SUB);\ninout VDD, VSS, SUB;\n', data)

# Remove ' '
data = re.sub('\( VDD, VSS, SUB\);', '(VDD, VSS, SUB);', data)

# Add ,
data = re.sub('(\(.+) VDD, VSS, SUB\);', '\g<1>, VDD, VSS, SUB);', data)

# Save to output file
outfile.write(data)
outfile.close()
