import os, uuid
import json

# local imports

from error import error_logger

class Project():
    def __init__(self, project_name):
        self.project_name = project_name.replace(" ", "_")
        self.project_dir = os.path.join(os.getcwd(), self.project_name)
        self.packages = []
        self.create_project_directory()
        self.create_project_config()
        self.create_entry_point()

    def create_project_directory(self):
        """
        => Check if the project directory exists, an d
        if it exists throw out an error
        else create the directory
        """
        if self.project_name not in os.listdir(os.getcwd()):
            os.mkdir(self.project_dir)
            os.mkdir(os.path.join(self.project_dir, "mod"))
        else:
            error_logger("folder already exists")
        return True

    def create_project_config(self):
        """
        Create configuration json files
        for the project
        """
        config_file_parh = os.path.join(self.project_dir, f"{self.project_name}.json")
        with open(config_file_parh, "w") as config_file:
            json.dump(
                self.get_config(),
                config_file,
                indent=6
            )

    def create_entry_point(self):
        """
        Create the entry point
        file
        """
        entry_point_path = os.path.join(self.project_dir, f"{self.project_name}.lss")
        with open(entry_point_path, "w") as entry_point:
            entry_point.write(" ")
        return entry_point_path


    def get_config(self):
        """
        Get the project configuration
        settings
        """
        return {
            "name" : self.project_name,
            "path" : self.project_dir,
            "entry-point" : f"{self.project_name}.lss",
            "description" : "",
            "packages" : self.packages
        }
