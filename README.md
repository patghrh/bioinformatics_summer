## Bash notes

### Command chaining

`|` - pipe: passes output of one command to another command

Example:
grep "ATG" genes.fasta | wc -l


`;` - executes commands sequentially, regardless of previous result

Example:
mkdir test ; cd test


`&&` - executes next command only if previous succeeded

Example:
mkdir project && cd project


`&` - runs command in background

## Environment

Python version:
3.14.3

Main packages:
- biopython 1.87
- numpy 2.5.1

Activate environment:

source .venv/bin/activate

## Git notes

### Useful commands

`git fetch`  
Downloads information about changes from GitHub without changing local files.

`git pull --rebase`  
Updates local branch from GitHub and puts my local commits on top of the updated history.

`git status`  
Shows current repository state (modified files, staged files, conflicts).

`git checkout --theirs <file>`  
During a conflict, keeps the version from the commit being applied.

`git add <file>`  
Marks a resolved conflict or changed file as ready for commit.

`git rebase --continue`  
Continues the rebase process after resolving conflicts.

### What happened in this project

I had two different versions of history:
- GitHub had a commit that was already pushed.
- My local branch had a newer commit.

`git pull --rebase` combined both histories into one linear history.  
Because the same file was modified in both versions, Git created a conflict.  
I resolved it by keeping my newer version of `sequence_analyzer.py`.

## Data parsing and validation notes

When working with biological data, do not assume that input files are always correct.

Important things to remember:

- Use `.strip()` when reading lines to remove unnecessary whitespace and newline characters.
- FASTA files contain:
  - header lines starting with `>`
  - sequence lines containing nucleotides
- The parser should only read and organize data.
- Sequence validation and analysis should be handled separately.

Possible problems in input files:
- sequence before the first FASTA header
- empty sequences
- duplicated IDs
- invalid nucleotide characters

Good practice:
Separate responsibilities:
- parser → reads and organizes data
- analyzer → validates sequences and calculates properties
- reporter → displays results

### Running FASTA analysis (analyze_fasta.py)

The FASTA analysis script can be run in two ways:
1) You can provide the file path directly as a command-line argument:
```bash
python python/scripts/analyze_fasta.py <filepath>
```
or..

2) Run the script without an argumetn. The program will then ask for the file path:
```bash
python python/scripts/analyze_fasta.py
```

## Analyzer design and error handling

When designing the analyzer, we should remember that input data may contain different types of errors or unexpected cases. The program should handle these cases deliberately rather than assuming that every FASTA record is valid.

Examples include:

* empty sequences,
* invalid nucleotides,
* duplicate sequence IDs,
* invalid FASTA records, such as a sequence appearing before a header or a header without an ID.

Not every problem should stop the whole program. Depending on the type of error, we can display a warning, skip the problematic sequence, or raise an exception and handle it at a higher level.

We also separate responsibilities between modules:

* `fasta_parser.py` — reads FASTA data and handles structural problems in the input,
* `sequence_analyzer.py` — analyzes individual sequences,
* `analyze_fasta.py` — runs the analysis, handles errors, and displays the results.

### Error handling

We learned how to use `try` / `except` to handle expected errors without stopping the entire program.

We also use boolean variables as flags to control program flow. For example:

```python
skip_sequence = True
```

means that the current FASTA record should be skipped, while:

```python
skip_sequence = False
```

means that the sequence can be processed normally.

`skip_sequence` is just a regular variable whose value we define ourselves. The program then uses its `True`/`False` value to decide what to do.

## Testing with pytest

We introduced `pytest` for automated testing.

Tests are stored in the `tests/` directory and test functions start with `test_`.

Basic example:

```python
def test_parse_fasta():
    result = parse_fasta("data/raw/example.fasta")
    assert result["seq1_example"] == "ATGCGATCGATCG"
```

`assert` checks whether the actual result matches our expected result. If the condition is true, the test passes. If it is false, pytest reports a failure.

We also learned how to use `tmp_path` to create temporary files for tests:

```python
def test_sequence_before_header(tmp_path):
    fasta_file = tmp_path / "test.fasta"
    fasta_file.write_text("ATGC\n>seq1\nCCCC")

    result = parse_fasta(fasta_file)

    assert result["seq1"] == "CCCC"
```

This allows us to test specific input cases without adding artificial files to `data/raw/`.

The `pytest.ini` file configures pytest so that our modules in `python/scripts/` can be imported during testing.

### Current parser tests

The parser is currently tested for:

* correct parsing of a valid sequence,
* duplicate sequence IDs,
* FASTA headers without a sequence ID,
* sequences appearing before the first FASTA header.
