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
