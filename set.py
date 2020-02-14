class Set:
    def __init__(self, bool, counter, dictionary):
        self.bool = bool
        self.counter = counter
        self.dictionary = dictionary

    def __getitem__(self, item):
        if item == 0:
            return self.bool
        elif item == 1:
            return self.counter
        elif item == 2:
            return self.dictionary

    def __str__(self):
        return "Ukupno ima: " + str(self.counter) + " reci\n" + str(self.dictionary)  # + " " +str(self.links)

    def unija(self, other):
        for key2 in other.dictionary:
            if key2 in self.dictionary:
                self.dictionary[key2] = other.dictionary[key2]
                self.counter += other.dictionary[key2][0]
                print(self.counter)
        return self

    def komplement(self, other):
        delete = []
        delete = [key for key in other.dictionary if key in self.dictionary]
        for key in delete:
            print(self.dictionary[key][0])
            self.counter -= self.dictionary[key][0]
            print(self.counter)
            del self.dictionary[key]
        return self