#!/usr/bin/env python3

from Bio import SeqIO

# read fasta
fasta_file = 'output/mt_contig/unicycler/assembly.fasta'
fasta = next(SeqIO.parse(fasta_file, 'fasta'))

# rotate
new_start_position = 9048
first_fragment = fasta[new_start_position - 1:]
second_fragment = fasta[:new_start_position - 1]
rotated_fasta = first_fragment + second_fragment

# write output
rotated_fasta_file = 'output/mt_contig/unicycler/assembly_rotated.fasta'
SeqIO.write(rotated_fasta,
            rotated_fasta_file,
            'fasta')
