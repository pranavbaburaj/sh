import pyfiglet as figlet
import click as click
from project import Project, ApplicationRunner

# The application package manager
# get
from package import PackageManager

# print out the application name
def print_app_name(app_name):
    figlet_object = figlet.Figlet(font='slant')
    return figlet_object.renderText(str(app_name))

# call the project class
# and create a new project
def create_new_project(project_name):
    print(print_app_name(project_name))
    new_project = Project(project_name)

# call teh run class
# and run the specified project
def run_project(project_name):
    run = ApplicationRunner(project_name)

# call the package manager
# and install packages
def get_package(package):
    package_manager = PackageManager(package)

@click.command()
@click.argument('command', type=str)
@click.argument('name', type=str)
def index(command, name):
    if command == "new":
        create_new_project(name)
    elif command == "run":
        run_project(name)
    elif command == "install" or command == "i" or command == "get":
        get_package(name)
    else:
        print(f"{command}:command not found")


if __name__ == "__main__":
    index()