from fasta_parser import parse_fasta
from sequence_analyzer import analyze_sequence

sequences = parse_fasta("data/raw/example.fasta")

print(sequences)
