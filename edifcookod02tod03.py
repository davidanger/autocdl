# This is EDIF netlist editor
# Design by Song 2018-09-27
import re
import sexpdata

# Initial parameters
extliblist = []
extinslist = []

# List External Library & Instance
def list_ext(display_on = 0):
    while len(extliblist) != 0:
        extliblist.pop()
    while len(extinslist) != 0:
        extinslist.pop()
    for i in range(6, len(data)-1):
        extliblist.append([data[i][1].value(), i])
        for j in range(4, len(data[i])):
            extinslist.append([data[i][j][1].value(), i, j, data[i][1].value()])
            if display_on:
                print(data[i][1].value(), data[i][j][1].value(), i, j)

# Rename External Library
def rename_ext_lib(tarlib, deslib):
    for i in range(len(extliblist)):
        if tarlib in extliblist[i]:
            data[extliblist[i][1]][1] = sexpdata.loads(deslib)
            list_ext()
            return 1
    return 0

# Rename External Instance
def rename_ext_inst(tarinst, desinst):
    for i in range(len(extinslist)):
        if tarinst in extinslist[i]:
            data[extinslist[i][1]][extinslist[i][2]][1] = sexpdata.loads(desinst)
            list_ext()
            return 1
    return 0

# New External Library
def new_ext_lib(deslib):
    lastlib = len(extliblist)
    if lastlib < 1:
        return 0
    else:
        data.insert(6, data[6][0:4])
        data[6][1] = sexpdata.loads(deslib)
        list_ext()
        return 1

# Copy External Instance
def copy_ext_inst(tarlib, tarinst, deslib, desinst):
    for i in range(6, len(data) - 1):
        if sexpdata.loads(tarlib) == data[i][1]:
            for j in range(4, len(data[i])):
                if sexpdata.loads(tarinst) == data[i][j][1]:
                    tmpdata = data[i][j].copy()
                    for k in range(6, len(data) - 1):
                        if sexpdata.loads(deslib) == data[k][1]:
                            for l in range(4, len(data[k])):
                                if sexpdata.loads(desinst) == data[k][l][1]:
                                    return 1
                            data[k].append(tmpdata)
                            data[k][-1][1] = sexpdata.loads(desinst)
                            list_ext()
                            return 1
                    new_ext_lib(deslib)
                    data[6].append(tmpdata)
                    data[6][-1][1] = sexpdata.loads(desinst)
                    list_ext()
                    return 2
    return 0

# Change Netlist Instance
def change_net_inst(tarlib, tarinst, deslib, desinst):
    textdata = sexpdata.dumps(data[-1][-1][-1][-1][-1])
    textdata = re.sub('\(cellRef %s \(libraryRef %s' % (tarinst, tarlib), '(cellRef %s (libraryRef %s' % (desinst, deslib), textdata)
    data[-1][-1][-1][-1][-1] = sexpdata.loads(textdata)

# Change Netlist Library
def change_net_lib(tarlib, deslib):
    textdata = sexpdata.dumps(data[-1][-1][-1][-1][-1])
    textdata = re.sub('\(libraryRef %s' % (tarlib), '(libraryRef %s' % (deslib), textdata)
    data[-1][-1][-1][-1][-1] = sexpdata.loads(textdata)

# Remove External Instance

# Clear All Empty External Library
def clear_ext_lib():
    tdel = []
    for i in range(6, len(data) - 1):
        if len(data[i]) < 5:
            tdel.append(i)
    for i in range(len(tdel)):
        data.pop(tdel[len(tdel) - i - 1])
    list_ext()

# Replace Instance
def replace_ins(tarlib, tarinst, deslib, desinst):
    copy_ext_inst(tarlib, tarinst, deslib, desinst)
    change_net_inst(tarlib, tarinst, deslib, desinst)

def replace_lib(tarlib, deslib):
    rename_ext_lib(tarlib, deslib)
    change_net_lib(tarlib, deslib)


### Main from here ###
# Input file
infile = open("in.edif", "r")

# Output file
outfile = open("out.edif", "w")
logfile = open("log.edif", "w")

# Read a line from infile
data = sexpdata.load(infile)
infile.close()

# List Data
list_ext(0)
logfile.write('All EXT Instance:\n')
logfile.write(str(extinslist))
logfile.write('\nConverting begin\n')

# ## Convert OD02 to OD03
# Change hb180enh_digitalcell_S sizeB -> OD0003_sch_common sizeB
replace_ins('hb180enh_digitalcell_S', 'sizeB', 'OD0003_sch_common', 'sizeB')

# Change hb180enh nch5_iso_nbl -> 1830bd15ba nch_svt_iso_nbl_5p0v
replace_ins('hb180enh', 'nch5_iso_nbl', '1830bd15ba', 'nch_svt_iso_nbl_5p0v')

# Change OD0002_sch_ac LSH_5V -> OD0003_sch_common LSH_5V
replace_ins('OD0002_sch_ac', 'LSH_5V', 'OD0003_sch_common', 'LSH_5V')

# Change OD0002_sch_ac LS_5T1P8 -> OD0003_sch_common LS_5T1P8
replace_ins('OD0002_sch_ac', 'LS_5T1P8', 'OD0003_sch_common', 'LS_5T1P8')

# Change hb180enh_digitalcell_S INVX2_5v_ISO_NBL -> 1830bd15ba_v5nbl V5NBL_IVD1A
replace_ins('hb180enh_digitalcell_S', 'INVX2_5v_ISO_NBL', '1830bd15ba_v5nbl', 'V5NBL_IVD1A')

# Change hb180enh_digitalcell_S NOR2x1_5v_IOS_NBL -> 1830bd15ba_v5nbl V5NBL_NR2D0A
replace_ins('hb180enh_digitalcell_S', 'NOR2x1_5v_IOS_NBL', '1830bd15ba_v5nbl', 'V5NBL_NR2D0A')

# Change hb180enh_digitalcell_S INVX1_ISO_NBL -> 1830bd15ba_v5nbl V5NBL_IVD0A
replace_ins('hb180enh_digitalcell_S', 'INVX1_ISO_NBL', '1830bd15ba_v5nbl', 'V5NBL_IVD0A')

# Change hb180enh_digitalcell_S NAND2X1_5v_ISO_NBL -> 1830bd15ba_v5nbl V5NBL_ND2D0A
replace_ins('hb180enh_digitalcell_S', 'NAND2X1_5v_ISO_NBL', '1830bd15ba_v5nbl', 'V5NBL_ND2D0A')

# Change hb180enh_digitalcell_S INVX1_5v_ISO_NBL -> 1830bd15ba_v5nbl V5NBL_IV0A
replace_ins('hb180enh_digitalcell_S', 'INVX1_5v_ISO_NBL', '1830bd15ba_v5nbl', 'V5NBL_IV0A')

# Change hb180enh_digitalcell_S INVX2_ISO_NBL -> 1830bd15ba_v5nbl V5NBL_IV1A
replace_ins('hb180enh_digitalcell_S', 'INVX2_ISO_NBL', '1830bd15ba_v5nbl', 'V5NBL_IV1A')

# Change hb180enh_digitalcell_S INVX4_5v_ISO_NBL -> 1830bd15ba_v5nbl V5NBL_IV4A
replace_ins('hb180enh_digitalcell_S', 'INVX4_5v_ISO_NBL', '1830bd15ba_v5nbl', 'V5NBL_IV4A')

# Change hb180enh_digitalcell_S NAND2X1_ISO_NBL -> 1830bd15ba_v5nbl V5NBL_ND2D0A
replace_ins('hb180enh_digitalcell_S', 'NAND2X1_ISO_NBL', '1830bd15ba_v5nbl', 'V5NBL_ND2D0A')

# Change hb180enh_digitalcell_S NOR2X1_ISO_NBL -> 1830bd15ba_v5nbl V5NBL_NR2D0A
replace_ins('hb180enh_digitalcell_S', 'NOR2X1_ISO_NBL', '1830bd15ba_v5nbl', 'V5NBL_NR2D0A')

# Save to output file
outfile.write(sexpdata.dumps(data))
outfile.close()
logfile.write('\nConverting end\n')
logfile.write('Final List EXT Instance:\n')
logfile.write(str(extinslist))
logfile.close()
