from Bio import Phylo
import os
os.chdir("~/parse_phylobayesResults/")
with open('tiny.map','r') as file:
    trees = file.readlines()

p = Phylo.parse('tiny.map', 'newick')