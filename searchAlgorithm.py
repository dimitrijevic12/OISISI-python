import trie
import set

def find(root, search, logop):
    # results = list()
    # for word in search:
    #     results.append(trie.find(root, word))
    # return results
    konacanSet = set.Set()
    konacanDict = {}
    #setovi = []
    if logop == "OR":
        if len(search) == 1:
            konacanSet, konacanDict = trie.find(root, search[0])
            return konacanSet, konacanDict
        else:
            set1, dict1 = trie.find(root, search[0])
            #print(set1)
            del search[0]
            for word in search:
                set2, dict2 = trie.find(root, word)
                #print(set2)
                #konacanSet = set1.unija(set2)
                konacanSet = set1 | set2
                for key2 in dict2:
                    if key2 not in dict1:
                        dict1[key2] = dict2[key2]
            # i = -1
            # for word in search:
            #     i += 1
            #     setovi[i] = trie.find(root, word)
            #     konacanSet = setovi[0].unija(setovi[i])
            return konacanSet, dict1
    elif logop == "AND":
        i = -1
        #setovi = []
        #recnik = []
        konacanDict = {}
        set1, dict1 = trie.find(root, search[0])
        del search[0]
        for word in search:
            i += 1
            set2, dict2 = trie.find(root, word)
            #konacanSet = set[0].presek(set[i])
            konacanSet = set1 & set2
            for key in dict1:
                if key in dict2:
                    dict1[key] = dict2[key]
        return konacanSet, dict1
    else:
        i = -1
        if len(search) == 2:
            set1, dict1 = trie.find(root, search[0])
            set2, dict2 = trie.find(root, search[1])
            konacanSet = set1.komplement(set2)
            delete = [key for key in dict2 if key in dict1]
            for key in delete:
                del dict1[key]
            return konacanSet, dict1
        #else:
