import pyfiglet as figlet
import click as click
from project import Project, ApplicationRunner

def print_app_name(app_name):
    figlet_object = figlet.Figlet(font='slant')
    return figlet_object.renderText(str(app_name))

def create_new_project(project_name):
    print(print_app_name(project_name))
    new_project = Project(project_name)

def run_project(project_name):
    run = ApplicationRunner(project_name)

@click.command()
@click.argument('command', type=str)
@click.argument('name', type=str)
def index(command, name):
    if command == "new":
        create_new_project(name)
    elif command == "run":
        run_project(name)
    else:
        print(f"{command}:command not found")


if __name__ == "__main__":
    index()