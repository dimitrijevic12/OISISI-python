from strukturePodataka import set


class TrieNode(object):
    """
    Our trie node implementation. Very basic. but does the job
    """

    def __init__(self, char: str):
        self.char = char                # karakter
        self.children = []              # sva deca jednog cvora
        self.word_finished = False      # da li je rec zavrsena
        self.dictionary = {}            # recnik koji sadrzi path stranice kao kljuc i broj reci na toj stranici kao vrednost
        self.set = set.Set()            # skup stranica
        self.counter = 0

def add(root, word: str, path):
    """
    Dodavanje podataka u cvor
    """
    node = root
    for char in word:
        found_in_child = False

        # Trazi karakter u listi dece trenutnog cvora

        for child in node.children:
            if child.char == char:
                node = child

                # Ako pronadje, to 'dete' sada postaje trenutni cvor
                found_in_child = True
                break
        # Ako ne pronadje karakter, inicijalizuje se novo 'dete'
        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node)
            # Dobijeno 'dete' postaje trenutni cvor
            node = new_node
    # Na redu je poslednji karakter reci
    node.word_finished = True

    # Ako vec postoji path stranice u recniku, povecava se brojac u suprotnom, path se dodaje u recnik
    if path in node.dictionary:
        node.dictionary[path] += 1
        node.set.add(path)
        node.counter += 1
    else:
        node.dictionary[path] = 1
        node.set.add(path)
        node.counter += 1


def find(root, word: str) :
    """
    Trazi da li zadata rec postoji u stablu.
    Ako nadje, vraca path stranice i broj reci na njoj

    """
    node = root
    setStranica = set.Set()
    konacanDict = {}
    # Ako koren nema 'dece' (stablo je prazno), vraca se False
    if not root.children:
        return setStranica, node.dictionary
    for char in word:
        char_not_found = True
        # Trazi karakter u listi 'dece' trenutnog cvora
        for child in node.children:
            if child.char == char:
                # Karakter je pronadjen
                char_not_found = False
                # 'Dete' u kome je nadjen karakter postaje trenutni cvor
                node = child
                break
        # Ako nije pronadjen karakter, vraca False
        if char_not_found:
            return setStranica, node.dictionary
    # Trazena rec je pronadjena i vracamo set i recnik stranica

    for stranica in node.dictionary:
        setStranica.add(stranica)
        konacanDict[stranica] = node.dictionary[stranica]
    return setStranica, konacanDict
