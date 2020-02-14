import trie

def find(root, search, logop):
    # results = list()
    # for word in search:
    #     results.append(trie.find(root, word))
    # return results
    if logop == "OR":
        i = -1
        for word in search:
            i += 1
            set[i] = trie.find(root, word)
            konacanSet = set[0].unija(set[i])
        return konacanSet
    elif logop == "AND":
        i = -1
        for word in search:
            i += 1
            set[i] = trie.find(root, word)
            konacanSet = set[0].presek(set[i])
    else:
        i = -1
        if len(search) == 2:
            for word in search:
                i += 1
                set[i] = trie.find(root, word)
                konacanSet = set[0].komplement(set[i])
        #else:
