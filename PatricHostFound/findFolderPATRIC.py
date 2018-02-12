#!/usr/bin/env python

import pickle
import sys

Fdict={}

fin1=sys.argv[1]        #allP_11.txt
fin2=sys.argv[2]        #NotinPat.tsv

lin1=[]
lin0=[]

fout1="FoundNow.txt"
fout0="stillNotfound.txt"

def recurse(d):
  if type(d)==type({}):
    for k in d:
      recurse(d[k])
  else:
      lin1.append(d)

with open(fin1, "r") as f:
    for ln in f:
        ln = ln.rstrip()
        wd=ln.split(':')
        fl = wd[0]
        genomeID = wd[1]
        genomeID=genomeID.split('.')[0]
        #print line
        if genomeID not in Fdict:
            Fdict[genomeID] = {}
            Fdict[genomeID] = fl

with open(fin2, "r") as f:
    for ln in f:
        ln = ln.rstrip()
        if ln in Fdict:
            lin1.append(ln)
            #lin1.append(Fdict[ln])
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
