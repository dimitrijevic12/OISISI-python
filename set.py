class Set:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def __str__(self):
        string = ""
        for key in self.dictionary:
            string += str(self.dictionary[key][0])
            string += " "
            string += key
            string += "\n"
        return string

    def unija(self, other):
        for key2 in other.dictionary:
            if key2 in self.dictionary:
                self.dictionary[key2] = other.dictionary[key2]
        return self

    def komplement(self, other):
        delete = []
        delete = [key for key in other.dictionary if key in self.dictionary]
        for key in delete:
            del self.dictionary[key]
        return self