from fasta_parser import parse_fasta

def test_parse_fasta():
    result = parse_fasta("data/raw/example.fasta")
    assert result["seq1_example"] == "ATGCGATCGATCG"

def test_duplicate_sequence_id():
    result = parse_fasta("data/raw/example.fasta")
    assert result["seq6_example"] == "ATGC"

def test_empty_header():
    result = parse_fasta("data/raw/example.fasta")
    assert "" not in result

def test_sequence_before_header(tmp_path):
    fasta_file = tmp_path / "test.fasta"
    fasta_file.write_text("ATGC\n>seq1\nCCCC")
    
    result = parse_fasta(fasta_file)
    assert result["seq1"] == "CCCC"

