#!/usr/bin/env python3

from Bio import SeqIO
import gzip
import tompytools

# IO files
mt_read_file = 'test/stats/mapped_reads.fastq.gz'
pe_read_file = 'data/pe_merged.fastq.gz'
output_fq = 'test/stats/mapped_reads_with_qual.fastq'

# index mitochondrial reads
tompytools.generate_message("Getting IDs of mapped reads from %s"
                            % mt_read_file)
with gzip.open(mt_read_file, "rt") as unzipped_file:
    mt_ids = [x.id for x in SeqIO.parse(unzipped_file, 'fastq')]

# read other reads if they're in the mt_ids
tompytools.generate_message("Extracting those reads from %s" % pe_read_file)
with gzip.open(pe_read_file, "rt") as unzipped_file:
    mt_reads = [x for x in SeqIO.parse(unzipped_file, 'fastq')
                if x.id in mt_ids]

# write mt_reads to fastq
tompytools.generate_message("Writing reads with original quality scores to %s"
                            % output_fq)
SeqIO.write(sequences=mt_reads,
            handle=output_fq,
            format='fastq')
