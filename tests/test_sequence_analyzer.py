from sequence_analyzer import analyze_sequence, reverse_complement, transcribe_dna, translate_dna
import pytest

def test_analyze_valid_sequence():
    result = analyze_sequence("ATGC")

    assert result["original_length"] == 4
    assert result["clean_length"] == 4
    assert result["a_count"] == 1
    assert result["t_count"] == 1
    assert result["g_count"] == 1
    assert result["c_count"] == 1
    assert result["gc_content"] == 50.0

def test_invalid_nucleotides():
    result = analyze_sequence("ATGXXX")

    assert result["original_length"] == 6
    assert result["clean_length"] == 3
    assert result["invalid_nucleotides"] == ["X", "X", "X"]

def test_empty_sequence():
    with pytest.raises(ValueError):
        analyze_sequence("")

def test_gc_content():
    result = analyze_sequence("GGGCCC")

    assert result["gc_content"] == 100.0

def test_reverse_complement():
    result = reverse_complement("ATGC")

    assert result == "GCAT"

def test_reverse_complement_invalid_nucleotides():
    with pytest.raises(ValueError):
        reverse_complement("ATGX")

def test_transcribe_dna():
    result = transcribe_dna("ATGC")

    assert result == "AUGC"

def test_translate_dna():
    result = translate_dna("ATGGCC")

    assert result == "MA"
