#!/usr/bin/env python
#run host_dict.py script before running this!
    #requires host.pickle file as input.
#this script does what it says: checks if the hosts in the input file are present in Patric or not.
#if yes - then check for quality cut-off value
    #if okay then append (the FOUND) "genomeID	\t completeness-contamination" to "inPat.tsv" file
    #if not okay then append (the FOUND) "genomeID	\t completeness-contamination" to "LowQinPat.tsv" file
#if not found- then too bad , (the NOT found) "taxID" will appended to the file "NotinPat.tsv"
import pickle
import sys

pickle_in=open("host.pickle","rb")
Hdict=pickle.load(pickle_in)
pickle_in.close()

fin=sys.argv[1]     #for example "BacAll.txt"
cOff=sys.argv[2]    #pass the cutoff value here!!

fout1="VS_inPat_"+cOff+".tsv"
fout0="VS_NotinPat.tsv"
fout2="VS_LowQinPat_"+cOff+".tsv"
lin0=[]
lin1=[]
lin2=[]

with open(fin, "r") as f:
    for ln in f:
        ln = ln.rstrip()
        if ln in Hdict:
            # lin=Hdict[ln]
            # lin=lin.rstrip()
            words=Hdict[ln].rstrip().split('\t')
            if float(words[1])>float(cOff):
                lin1.append(Hdict[ln])
            else:
                lin2.append(Hdict[ln])
        else:
            lin0.append(ln)

thefile = open(fout1, "w")
for item in lin1:
    print>>thefile, item
thefile.close()

thefile = open(fout0, "w")
for item in lin0:
    print>>thefile, item
thefile.close()

thefile = open(fout2, "w")
for item in lin2:
    print>>thefile, item
thefile.close()
