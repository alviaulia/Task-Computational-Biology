# -*- coding: utf-8 -*-
"""AlviAuliaF_2602182865_BE20_Session4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1iWQy1I8-6S14oB1ev9BHRsCRml2wi_w8

#Global dan Local Alignment
"""

!pip install biopython

from Bio import pairwise2
from Bio.pairwise2 import format_alignment

import Bio

from Bio.Seq import Seq

seq1 = Seq('ATGCATGGTGCGCGA')
seq2 = Seq('ATTTGTGCTCCTGGA')

#Global Alignment
alignments = pairwise2.align.globalxx(seq1, seq2)

alignments

#To display the alignment
print(format_alignment(*alignments[0]))

#View all
for a in alignments:
  print(format_alignment(*a))

#Local Alignment
loc_alignments = pairwise2.align.localxx(seq1, seq2)

#View all
for a in loc_alignments:
  print(format_alignment(*a))

#Get the alignment by only the score
alignment2 = pairwise2.align.globalxx(seq1, seq2, one_alignment_only=True, score_only=True)

alignment2

seq1

seq2

alignment2/len(seq1)*100

#Get the alignment by only the score
loc_alignment2 = pairwise2.align.localxx(seq1, seq2, one_alignment_only=True, score_only=True)

alignment2/len(seq1)*100

"""#Similarity Analysis"""

from Bio.Seq import Seq

seqA = Seq('ATGCATGGTGCGCGA')
seqB = Seq('ATTTGTGCTCCTGGA')

from Bio import pairwise2

AvB = pairwise2.align.localxx(seqA, seqB, one_alignment_only=True, score_only=True)

print("AvB", AvB/len(seqB)*100)

#Check if same
seqA == seqB

"""#Hamming Distance dan Levenstein"""

seq1 = Seq('ATGCATGGTGCGCGA')
seq2 = Seq('ATTTGTGCTCCTGGA')

#Hamming Distance fxn
def hamming_distance(lhs,rhs):
  return len([(x,y) for x,y in zip(lhs,rhs) if x != y])

hamming_distance(seq1, seq2)

# 0 if the same
hamming_distance(seq1, seq1)

print(seq1)
print(seq1[::-1])

hamming_distance(seq1, seq1[::-1])

!pip install python-Levenshtein
from Levenshtein import distance

distance(str(seq1), str(seq2))

print("Hamming Distance", hamming_distance(seq1, seq2))
print("Levenshtein Distance", distance(str(seq1), str(seq2)))

"""#Define The Function"""

def delta(x,y):
  return 0 if x == y else 1

def M(seq1, seq2, i, j, k):
  return sum(delta(x,y) for x,y in zip(seq1[i:i+k], seq2[j:j+k]))

def makeMatrix(seq1, seq2, k):
  n = len(seq1)
  m = len(seq2)
  return [[M(seq1, seq2, i, j, k) for j in range(m-k+1)] for i in range(n-k+1)]

def plotMatrix(M, t, seq1, seq2, nonblank = chr(0x25A0), blank = ' '):
  print(' |' + seq2)
  print('-'*(2 + len(seq2)))
  for label, row in zip(seq1, M):
    line = ''.join(nonblank if s < t else blank for s in row)
    print(label + '|' + line)

import matplotlib.pyplot as plt
import numpy as np

#Add Some fancyness to it
plt.imshow(np.array(makeMatrix(seq1, seq2, 1)))
xt=plt.xticks(np.arange(len(list(seq1))), list(seq1))