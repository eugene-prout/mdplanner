import click
from click_shell import shell

@shell(prompt='mdplanner > ', intro='Welcome to MD Planner...')
def core():
    pass

@core.command()
def testcommand():
    click.echo("testcommand is running")

if __name__ == '__main__':
    core()
