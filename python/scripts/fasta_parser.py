def parse_fasta(filename):
    sequences = {}
    seq_id = None
    skip_sequence = False

    with open(filename) as file:
        for line in file:
            line = line.strip()

            if line == "":
                continue

            if line.startswith(">"):
                seq_id = line[1:]
                if seq_id in sequences:
                    skip_sequence = True
                    print(f"Warning: duplicate sequence ID: {seq_id}")
                else:
                    skip_sequence = False
                    sequences[seq_id] = ""
            else:
                if not skip_sequence:
                    if seq_id is not None:
                        sequences[seq_id] += line
                    else:
                        print(f"Warning: sequence found before fasta header: {line}")
    return sequences

# Test parser when running this file directly
if __name__ == "__main__":
    result = parse_fasta("data/raw/example.fasta")
    print(result)
