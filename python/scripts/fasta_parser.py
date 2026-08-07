def parse_fasta(filename):
    sequences = {}
    seq_id = None

    with open(filename) as file:
        for line in file:
            line = line.strip()

            if line == "":
                continue

            if line.startswith(">"):
                seq_id = line[1:]
                sequences[seq_id] = ""
            else:
                if seq_id is not None:
                    sequences[seq_id] += line
                else:
                    print(f"Warning: sequence found before fasta header: {line}")
    return sequences

result = parse_fasta("data/raw/example.fasta")
print(result)
