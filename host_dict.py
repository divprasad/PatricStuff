#!/usr/bin/env python
#this script needs 1 input , the file like resultsCheckm_wotopL.txt
#this contains the checkm results in the format "taxID	\t genomeID	\t completeness-contamination"
#for a given taxID of host, we want to know the genomeID with the highest scores
#this we can use as a representative species/strain for the phage-host linkage

# so this script outputs two files : (1) a "host.pickle" file with the key as the genome ID
#and the value as "genomeID	\t completeness-contamination" with the HIGHEST scores
#(2) a "host_uniq.tsv" human readable file with only "genomeID	\t completeness-contamination" on each line
#we can Easily get the taxID by splitting the genomeID.split('.')[1]
#by doing wc host_uniq.tsv, we can get the number of unique hosts in PatricDB

#now can run host_Scut.py script
#now can run the HcheckinP.py script

import pickle
import sys

fin=sys.argv[1]
fout="host.pickle"
Hdict={}

ln=[]
lin1=[]

def recurse(d):
  if type(d)==type({}):
    for k in d:
      recurse(d[k])
  else:
      lin1.append(d)


with open(fin, "r") as f:
    for line in f:
        line = line.rstrip()
        words = line.split('\t')
        taxID = words[0]
        genomeID = words[1]
        score = words[2]
        #print line
        if taxID not in Hdict:
            Hdict[taxID] = {}
            del ln[:]
            ln.append(genomeID)
            ln.append(score)
            newline = '\t'.join(str(v) for v in ln)
            Hdict[taxID] = newline
        else:
            oldline=Hdict[taxID]
            oldline = oldline.rstrip()
            oldwords = oldline.split('\t')
            OgenomeID = oldwords[0]
            Oscore = oldwords[1]
            if score > Oscore :
                del ln[:]
                ln.append(genomeID)
                ln.append(score)
                newline = '\t'.join(str(v) for v in ln)
                Hdict[taxID] = newline
            elif score == Oscore:
                if genomeID > OgenomeID:
                    del ln[:]
                    ln.append(genomeID)
                    ln.append(score)
                    newline = '\t'.join(str(v) for v in ln)
                    Hdict[taxID] = newline

pickle_out=open(fout,"wb")
pickle.dump(Hdict,pickle_out)
pickle_out.close()

recurse(Hdict)

thefile = open("host_uniq.tsv", "w")
for item in lin1:
    print>>thefile, item
