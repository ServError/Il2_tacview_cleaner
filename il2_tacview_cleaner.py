#!/usr/bin/env python3
import fileinput
import sys

if len(sys.argv) != 2:
    raise ValueError('Please supply a single TacView acmi file.')

fname = sys.argv[1]

if not fname.endswith('.txt.acmi', 1):
    raise ValueError('Invalid file. Please supply a TacView .txt.acmi file.')

outf = open(fname.replace('.txt.acmi', '') + '_cleaned.txt.acmi',"w", newline='')

# Each line contains a hex coded ID for an object.
# For some entries, both Coalition and Color exist.
# We want to fix these to Axis + Blue and Allies + Red (easy)
# In addition, later references to the same hex ID may cause the color to swap
# There are basically three main approaches here:
#     Keep an array of IDs and remove all color references after the initial
#     Reference a list of IL2 objects and associate them to a consistent color
#     Fix the coalition colors and then remove and coalition-less color entries (easy, used below)

with fileinput.input(files=(fname)) as f:
    for line in f:
        if fileinput.isfirstline():
            # Validate that this is a tacview file
            if (not line.__contains__('FileType=text/acmi/tacview')):
                raise ValueError('Invalid file. Please supply a TacView acmi file.')

        # Check if this is a coalition + color line. Always ,Coalition=X,Color=Y
        elif (line.__contains__(',Coalition=Axis,Color=Red')):
            line = line.replace(',Color=Red',',Color=Blue')
        elif (line.__contains__(',Coalition=Allies,Color=Blue')):
            line = line.replace(',Color=Blue',',Color=Red')
        # If it's only a color line, remove ,Color=color
        elif (line.__contains__('Color=') and not line.__contains__('Coalition=')):
            line = line.replace(',Color=Blue','')
            line = line.replace(',Color=Red','')

        # Now find bombs and other static objects and remove extra entries without real position info
        # At a glance, searching for 'AGL=0\n' could probably work, but don't want to risk
        # the rare case where an entry is actually at precisely AGL=0.
        # The approach used instead is to find object declarations with less than 3 '|'
        # which dilineate info fields. These don't have good data.
        if (line.__contains__('Color=') and line.__contains__('Coalition=')):
            if (line.count('|') < 3):
                continue

        outf.write(line)

outf.close()
print("Completed Successfully.")
#input("Completed Successfully, press Enter to exit.")
# Notes: Bombs and other objects get declared without a position initially it seems.
# A minus sign preceding the hex ID removes the object from view.
