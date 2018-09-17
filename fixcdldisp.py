# This is fix the CDL parameter display in the schematic view.
# Design by Song 2018-09-15
import re

# Input file
infile = open("in.cdl", "r")

# Output file
outfile = open("out.cdl", "w")

# Read a line from infile
data = infile.read()
infile.close()

# Search parameter length and add parameter l
data = re.sub(r'length=(\S+)', 'length=\g<1> l=\g<1>', data)

# Search parameter width and add parameter w & fw
data = re.sub(r'width=(\S+)', 'width=\g<1> w=\g<1> fw=\g<1>', data)

# Connect FIX, Change vdd & vss net to VDD and VSS net
while (re.search(' vdd ', data) != None):
    data = re.sub(' vdd ', ' VDD ', data)
while (re.search(' vss ', data) != None):
    data = re.sub(' vss ', ' VSS ', data)
data = re.sub('vdd:B', 'VDD:B', data)
data = re.sub('vss:B', 'VSS:B', data)

# Connect FIX, Change VDD VSS PIN to vdd vss
# data = re.sub(' VDD VSS SUB', ' vdd vss SUB', data)

# Save to output file
outfile.write(data)
outfile.close()
