from .commands import token
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

        self.current = LexicalAnalyser.set_current_character(self.data, self.pos)
        while self.current is not None:
            if self.current == " ":
                pass
            elif self.current in token:
                self.token_values.append(token[self.current])
            else:
                # add an invalid aexception
            self.pos += 1
            self.current = LexicalAnalyser.set_current_character(self.data, self.pos)
        return self.token_values