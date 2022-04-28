from unicodedata import category
from note import Note
import click
import os
from click_shell import shell
from pathlib import Path

@shell(prompt='mdplanner > ', intro='Welcome to MD Planner...')
def core():
    pass

@core.command()
def testcommand():
    click.echo("testcommand is running")

@core.command()
def add_task():
    click.echo("Adding new task")
    title = click.prompt('Enter post title', type=str)
    all_cats = [x.name for x  in get_all_categories()]
    category = numbered_prompt(all_cats, 'Enter post category')
    description = click.prompt('Enter post description', type=str)
    note = Note(title, description, category)
    note.write_to_file()

def numbered_prompt(choices, text_prompt):
    
    numbered = list(enumerate(choices, 1))
    for x in numbered:
        click.echo(f"({x[0]}) {x[1]}")
    flat_numbered = [str(item) for sublist in numbered for item in sublist]
    choice = click.prompt(text_prompt, type=click.Choice(flat_numbered),show_choices=False)
    if choice.isdigit():
        choice = next(i[1] for i in numbered if i[0] == int(choice))
    return choice

def get_all_categories():
    p = Path('./data')

    # All subdirectories in the current directory, not recursive.
    return [f for f in p.iterdir() if f.is_dir()]

@core.command()
def init():
    """ Create directory structure. If it already exists, warn that it isn't blank """
    click.echo("Creating structure...")
    try:
        os.mkdir('data/')
    except FileExistsError:
        click.echo("data folder exists, skipping")
    try:
        os.mkdir('data/to-do/')
    except FileExistsError:
        click.echo("To-do folder exists, not creating")
    try:
        os.mkdir('data/in-progress/')
    except FileExistsError:
        click.echo("In-progress folder exists, not creating")
    try:
        os.mkdir('data/done/')
    except FileExistsError:
        click.echo("Done folder exists, not creating")
    

if __name__ == '__main__':
    core()
