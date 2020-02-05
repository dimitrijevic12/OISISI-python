import trie

def find(root, logop, search):
    if logop == "AND" or logop == "":
        for word in search:
            print(trie.find(root, word))
        return trie.find(root, word)
    elif logop == "OR":
        for word in search:
            print(trie.find(root, word))
    else:
        for word in search:
            print(trie.find(root, word))