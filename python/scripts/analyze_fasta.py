import sys
from fasta_parser import parse_fasta
from sequence_analyzer import analyze_sequence, print_report

def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input("Enter file path: ")

    try:
        sequences = parse_fasta(filename)
    except FileNotFoundError:
        print("Provided file does not exist.")
        return

    for seq_id, sequence in sequences.items():
        try:
            result = analyze_sequence(sequence)
            print(seq_id)
            print_report(result)
        except ValueError:
            print(f"Warning: Sequence {seq_id} is empty.")

if __name__ == "__main__":
    main()
