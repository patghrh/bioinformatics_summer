from Bio.Seq import Seq

VALID_BASES = "ATGC"
COMPLEMENT = {
    "A": "T",
    "T": "A",
    "G": "C",
    "C": "G",
}

def analyze_sequence(sequence):
    if len(sequence) == 0:
        raise ValueError("Sequence is empty.")

    correct_sequence = []
    invalid_nucleotides = []

    for nucleotide in sequence:
        if nucleotide in VALID_BASES:
            correct_sequence.append(nucleotide)
        else:
            invalid_nucleotides.append(nucleotide)

    a_count = correct_sequence.count("A")
    t_count = correct_sequence.count("T")
    g_count = correct_sequence.count("G")
    c_count = correct_sequence.count("C")

    if len(correct_sequence) > 0:
        gc_content = (g_count + c_count) / len(correct_sequence) * 100
    else:
        gc_content = 0
    return {
        "original_length": len(sequence),
        "clean_length": len(correct_sequence),
        "a_count": a_count,
        "t_count": t_count,
        "g_count": g_count,
        "c_count": c_count,
        "gc_content": round(gc_content, 2),
        "invalid_nucleotides": invalid_nucleotides,
    }

def reverse_complement(sequence):
    complement = ""

    for nucleotide in sequence:
        if nucleotide not in COMPLEMENT:
            raise ValueError(f"Invalid nucleotide: {nucleotide}")

        complement += COMPLEMENT[nucleotide]

    return complement[::-1]

def transcribe_dna(sequence):
    return sequence.replace("T", "U")

def translate_dna(sequence):
    return str(Seq(sequence).translate())

def print_report(result):
    print("Sequence report\n---------------")
    print(f"Original sequence length: {result['original_length']}")
    print(f"Clean sequence length: {result['clean_length']}")
    print(f"A: {result['a_count']}")
    print(f"T: {result['t_count']}")
    print(f"G: {result['g_count']}")
    print(f"C: {result['c_count']}")
    print(f"GC content: {result['gc_content']}%")
    print(f"Invalid nucleotides: {result['invalid_nucleotides']}")


if __name__ == "__main__":
    result1 = analyze_sequence("ATGCGATXG")
    print_report(result1)
    result2 = analyze_sequence("CCCCGGGG")
    print_report(result2)
    result3 = analyze_sequence("XXXXXXXX")
    print_report(result3)
