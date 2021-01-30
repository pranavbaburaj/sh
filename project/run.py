import os
import json, logging

class ApplicationRunner():
    def __init__(self, app_name):
        self.project_file = self.get_project_entry_point(app_name)
        self.content = self.get_file_content(self.project_file)
        self.entry_point = self.get_entry_point(self.content)

        self.execute_file(self.entry_point, app_name)

    def execute_file(self, entry, app):
        file_path = ""

        if entry is not None:
            if app == ".":
                file_path = os.path.join(os.getcwd(), entry)
            else:
                file_path = os.path.join(os.getcwd(), app, entry)
        else:
            logging.error("Cannot run the project")

        print(file_path)

    def get_project_entry_point(self, app_name):
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
            logging.error("It seems that the directory is not a project")
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
                print("Aborted:Cannot find entry point")
                return None