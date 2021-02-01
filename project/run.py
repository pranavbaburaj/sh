import os
import json, logging

# local imports
from error import error_logger
from lang.lexer import LexicalAnalyser

class ApplicationRunner():
    def __init__(self, app_name):
        # the project name
        self.project_file = self.get_project_entry_point(app_name)
        self.content = self.get_file_content(self.project_file)
        self.entry_point = self.get_entry_point(self.content)

        # the execution of the code
        # takes place
        self.execute_file(self.entry_point, app_name)

    def execute_file(self, entry, app):
        """
        Determine the filepath base
        on the argument [., project_name].
        by reading the <project_name>.json(config file)
        and taking out the entry-point and passing the 
        file to the lexer
        """
        file_path = ""

        if entry is not None:
            if app == ".":
                file_path = os.path.join(os.getcwd(), entry)
            else:
                file_path = os.path.join(os.getcwd(), app, entry)
        else:
            error_logger("Cannot run the project")

        self.tokens = []
        file_data = self.read_file(file_path).split("\n")
        for index, line in enumerate(file_data):
            lexer = LexicalAnalyser(line)
            self.tokens.append(lexer.start_lexical_evaluation())

    def read_file(self, path):
        """
        Read the file if the path
        exists
        """
        if os.path.exists(path):
            with open(path, "r") as reader:
                return reader.read()
        else:
            error_logger("Cannot find entry point")

    def get_project_entry_point(self, app_name):
        """
        Get the entry point
        of the project
        """
        if app_name == ".":
            return os.path.join(
                os.getcwd(),
                f"{os.path.basename(os.getcwd())}.json"
            )
        else:
            return os.path.join(
                os.getcwd(),
                app_name,
                f"{app_name}.json"
            )

    def get_file_content(self, project_file):
        """
        Get the content of the
        project file
        """
        if os.path.exists(project_file) and os.path.isfile(project_file):
            with open(project_file, "r") as reader:
                return json.load(reader)
        else:
            error_logger("It seems that the directory is not a project")
            return None

    def get_entry_point(self, content):
        """
        Get the project entry point
        file name
        """
        if isinstance(content, dict):
            if 'entry-point' in content:
                return content['entry-point']
            else:
                error_logger("Aborted:Cannot find entry point")
                return None