from .commands import token
from lang.modules import list_directories
import os
import webbrowser as browser

from clint.textui import colored as color
from error import error_logger

current_dir = os.getcwd()

class LexicalAnalyser():
    def __init__(self, data):
        self.data = data.split(" ")
        self.pos = 0
        self.exceptions = []
        self.token_values = []
        self.current = LexicalAnalyser.set_current_character(data, self.pos)


    @staticmethod
    def set_current_character(data, pos):
        if len(data) == pos:
            return None
        else:
            return data[pos]

    def start_lexical_evaluation(self):
        global current_dir

        self.current = LexicalAnalyser.set_current_character(self.data, self.pos)
        while self.current is not None:
            if self.current == " ":
                pass
            elif self.current == "ls" or self.current == "dir":
                list_directories(current_dir)
            elif self.current == "file" or self.current == "explorer":
                browser.open(current_dir)
            elif "cd" in self.current.split(":"):
                cd_command = self.current.split(":")
                if len(cd_command) > 1:
                    enter_dir = cd_command[1]
                    if enter_dir == '':
                        pass
                    else:
                        if enter_dir in os.listdir(current_dir):
                            n_dir_p = os.path.join(current_dir, enter_dir)
                            if os.path.isdir(n_dir_p):
                                current_dir = n_dir_p
                                pass
                            else:
                                error_logger("The path is not a directory")
                        else:
                            error_logger("Directory not found")
                else:
                    pass
            elif self.current == "path":
                print(color.green(current_dir))
            elif self.current == "directory":
                print(color.green(os.path.basename(current_dir)))
            elif self.current in token:
                self.token_values.append(token[self.current])
            else:
                # add an invalid aexception
                pass
            self.pos += 1
            self.current = LexicalAnalyser.set_current_character(self.data, self.pos)
        return self.token_values