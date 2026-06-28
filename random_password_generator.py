def replace_nucleotide (dna_strand):
    trna = dna_strand.replace('T','U')

    return f'{trna}'

# Enter your desired Nucleotide Strand Sequence inside ' ' below
nucleotides = 'GATGGAACTTGACTACGTAAATT'
print(replace_nucleotide(nucleotides))
