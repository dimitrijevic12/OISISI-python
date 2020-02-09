import trie

def find(root, search):
    # if logop == "OR" or logop == "":
    #     for word in search:
    #         print(trie.find(root, word))
    #     return trie.find(root, word)
    # elif logop == "OR":
    #     for word in search:
    #         print(trie.find(root, word))
    # else:
    #     for word in search:
    #         print(trie.find(root, word))
    results = list()
    for word in search:
        results.append(trie.find(root, word))
    return results