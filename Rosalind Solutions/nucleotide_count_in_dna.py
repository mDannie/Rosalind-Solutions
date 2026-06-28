def count_nucleotides (dna_strand):
    a = dna_strand.count('A')
    c = dna_strand.count('C')
    g = dna_strand.count('G')
    t = dna_strand.count('T')

    return f"{a} {c} {g} {t}"

# Enter your desired Nucleotide Strand's Sequence inside ' ' below
nucleotides = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
print(count_nucleotides(nucleotides))