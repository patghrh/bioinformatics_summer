import sys
from fasta_parser import parse_fasta
from sequence_analyzer import analyze_sequence, print_report

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = input("Enter file path: ")

sequences = parse_fasta(filename)

for seq_id, sequence in sequences.items():
    result = analyze_sequence(sequence)
    print(seq_id)
    print_report(result)
