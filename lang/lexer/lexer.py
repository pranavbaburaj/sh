
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
        return self.token_values