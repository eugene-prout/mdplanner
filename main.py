from note import Note
import click
import os
from click_shell import shell

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
    category = click.prompt('Enter post category', type=str)
    description = click.prompt('Enter post description', type=str)
    note = Note(title, description, category)
    note.write_to_file()

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
