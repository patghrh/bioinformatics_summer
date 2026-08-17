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
or 
2) run the script without an argumetn. The program will then ask for the file path:
```bash
python python/scripts/analyze_fasta.py
```
