#!/usr/bin/env python
#this script needs 2 inputs [1] fin= host_uniq.tsv & [2] cOff= the cut-off Percentage
#this gives us a output .tsv file with only those hosts in Patric that are above
#the cutoff. Super chill!

#now can run the HcheckinP.py script

import sys
fin=sys.argv[1]         #for ex : host_SelcOff.in.tsv
cOff=sys.argv[2]        #like 70 or 80
fout="host_SelcOff"+str(cOff)+".tsv"

ln=[]
with open(fin, "r") as f:
    for line in f:
        line = line.rstrip()
        words = line.split('\t')
        genomeID = words[0]
        score = words[1]
        if score >= cOff:
                ln.append(genomeID)

thefile = open(fout, "w")
for item in ln:
    print>>thefile, item
thefile.close()
