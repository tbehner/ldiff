import click
import subprocess
from pathlib import Path

def run(cmd):
    return subprocess.run(cmd, shell=True, capture_output=False, check=True)

def current_branch():
    ret = subprocess.run("git rev-parse --abbrev-ref HEAD", shell=True, capture_output=True)
    return ret.stdout.decode().strip()

@click.command()
@click.argument("old-git-id")
@click.argument("new-git-id")
@click.argument("texfile")
@click.option("--preserve", default=False, is_flag=True)
def main(old_git_id, new_git_id, texfile, preserve):
    old_squashed = Path.cwd() / f"{old_git_id}-squashed.tex"
    new_squashed = Path.cwd() / f"{new_git_id}-squashed.tex"
    diff = Path.cwd() / f"{old_git_id}-{new_git_id}-diff.tex"

    cur_branch = current_branch()
    run(f"git checkout {old_git_id}; latexpand {texfile} > {old_squashed}")
    run(f"git checkout {new_git_id}; latexpand {texfile} > {new_squashed}")
    run(f"latexdiff {old_squashed} {new_squashed} > {diff}")
    run(f"latexmk -pdf {diff}")
    run(f"git checkout {cur_branch}")

    if not preserve:
        old_squashed.unlink()
        new_squashed.unlink()
        for suffix in ['.aux', '.bbl', '.blg', '.fdb_latexmk', '.fls', '.log', '.out', '.toc']:
            diff.with_suffix(suffix).unlink()
        diff.unlink()
