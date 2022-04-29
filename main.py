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
    """Test if system is working correctly. Will output "testcommand is running" if system working.
    """
    click.echo("testcommand is running")

@core.command()
def add_task():
    """Add a new task to the board. Will ask user for title, category and description.
    """
    click.echo("Adding new task")
    title = click.prompt('Enter task title', type=str)
    all_cats = [x.name for x  in get_all_categories()]
    category = numbered_prompt(all_cats, 'Enter task category')
    description = click.prompt('Enter task description', type=str)
    note = Note(title, description, category)
    note.write_to_file()

@core.command()
def view_category():
    """Shows all tasks in a category and allows user to pick one task to view.
    """
    click.echo("Select a category to view")
    all_cats = [x.name for x  in get_all_categories()]
    category = numbered_prompt(all_cats, 'Enter task category')
    p = Path('./data') / category
    notes = []
    for filename in os.listdir(p):
        notes.append(Note.from_file(p / filename))
    titles = [x.title for x in notes]
    task = numbered_prompt(['MENU']+titles, 'Select a post to view more information about it')
    if task == 'MENU':
        return
    else:
        selected_task = [note for note in notes if note.title == task][0]
        view_task(selected_task)

def view_task(selected_task):
    """Output details from supplied task.
    :param selected_task: the task to view details about
    :type selected_task: Note
    """
    click.echo(selected_task.title)
    click.echo(selected_task.category)
    click.echo(selected_task.description)
    

def numbered_prompt(choices, text_prompt):
    """Enumerates the choices available for the user and allows them to enter either the value or the number. Uses click prompt and returns the option from choices that they pick.

    :param choices: list of acceptable inputs
    :type choices: list
    
    :return: string containing the user's choice from choices parameter
    :rtype: str
    """

    numbered = list(enumerate(choices, 1))
    for x in numbered:
        click.echo(f"({x[0]}) {x[1]}")
    flat_numbered = [str(item) for sublist in numbered for item in sublist]
    choice = click.prompt(text_prompt, type=click.Choice(flat_numbered),show_choices=False)
    if choice.isdigit():
        choice = next(i[1] for i in numbered if i[0] == int(choice))
    return choice

def get_all_categories():
    """Generate a list of all categories in the system. Looks at subdirectory names of the data folder.

    :return: list of all subdirectories
    :rtype: list
    """
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
