import os, uuid
import json

class Project():
    def __init__(self, project_name):
        self.project_name = project_name.replace(" ", "_")
        self.project_dir = os.path.join(os.getcwd(), self.project_name)
        self.packages = []
        self.create_project_directory()
        self.create_project_config()
        self.create_entry_point()

    def create_project_directory(self):
        if self.project_name not in os.listdir(os.getcwd()):
            os.mkdir(self.project_dir)
            os.mkdir(os.path.join(self.project_dir, "mod"))
        else:
            print("folder already exists")
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
