import trie
import set

def find(root, search, logop):
    # results = list()
    # for word in search:
    #     results.append(trie.find(root, word))
    # return results
    konacanSet = set.Set({})
    setovi = []
    if logop == "OR":
        print(len(search))
        if len(search) == 1:
            return trie.find(root, search[0])
        else:
            set1 = trie.find(root, search[0])
            print(set1)
            del search[0]
            for word in search:
                set2 = trie.find(root, word)
                print(set2)
                konacanSet = set1.unija(set2)
            # i = -1
            # for word in search:
            #     i += 1
            #     setovi[i] = trie.find(root, word)
            #     konacanSet = setovi[0].unija(setovi[i])
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
            set1 = trie.find(root, search[0])
            set2 = trie.find(root, search[1])
            konacanSet = set1.komplement(set2)
            return konacanSet
        #else:
