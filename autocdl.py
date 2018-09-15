import re

# Input file
infile = open("in.cdl", "r")

# Output file
outfile = open("out.cdl", "w")

# Read a line from infile
data = infile.read()
infile.close()

# Search parameter length and add parameter l
datal = re.sub(r'length=(\S+)', 'length=\g<1> l=\g<1>', data)

# Search parameter width and add parameter w & fw
datao = re.sub(r'width=(\S+)', 'width=\g<1> w=\g<1> fw=\g<1>', datal)

# Save to output file
outfile.write(datao)
outfile.close()
