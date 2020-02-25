from strukturePodataka import set, trie


def find(root, search, logop):
    konacanSet = set.Set()
    konacanDict = {}
    if logop == "OR":
        if len(search) == 1:
            konacanSet, konacanDict = trie.find(root, search[0])
            return konacanSet, konacanDict
        else:
            set1, dict1 = trie.find(root, search[0])
            del search[0]
            for word in search:
                set2, dict2 = trie.find(root, word)
                konacanSet = set1 | set2
                for key2 in dict2:
                    if key2 not in dict1:
                        dict1[key2] = dict2[key2]
            return konacanSet, dict1
    elif logop == "AND":
        i = -1
        konacanSet = set.Set()
        konacanDict = {}
        set1, dict1 = trie.find(root, search[0])
        set2, dict2 = trie.find(root, search[1])
        konacanSet = set1 & set2
        for key in dict1:
            if key in dict2:
                konacanDict[key] = dict2[key]

        # del search[0]
        # for word in search:
        #     i += 1
        #     set2, dict2 = trie.find(root, word)
        #     konacanSet = set1 & set2
        #     for key in dict1:
        #         if key in dict2:
        #             dict1[key] = dict2[key]
        return konacanSet, konacanDict
    else:
        set1, dict1 = trie.find(root, search[0])
        set2, dict2 = trie.find(root, search[1])
        konacanSet = set1.komplement(set2)
        delete = []
        for key in dict1:
            if key in dict2:
                delete.append(key)

        konacanDict = dict1
        for key in delete:
            del konacanDict[key]
        return konacanSet, konacanDict
