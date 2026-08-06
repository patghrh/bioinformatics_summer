sequence = "ATGCGATXG"
a_count = sequence.count("A")
t_count = sequence.count("T")
g_count = sequence.count("G")
c_count = sequence.count("C")
 
print(f"A: {a_count}\nT: {t_count}\nG: {g_count}\nC: {c_count}")

valid_bases = "ATGC"
correct_sequence = []
invalid_nucleotides = []

for nucleotide in sequence:
    if nucleotide in valid_bases:
        correct_sequence.append(nucleotide)
    else:
        invalid_nucleotides.append(nucleotide)

print("Invalid nucleotides:", invalid_nucleotides)

gc_content = (g_count + c_count) / len(correct_sequence) * 100
print(f"GC content: {gc_content:.2f}%")
