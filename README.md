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
