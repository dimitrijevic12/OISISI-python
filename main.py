import obilazakFajlova
import queryParser
import searchAlgorithm
import rangiranje
import time
import set

#print("Unesite korenski direktorijum: ")
# while True:
#     rootdir = input("Unesite korenski direktorijum: ")
#     (bool, root) = obilazakFajlova.obidji(rootdir)
#     if bool == True:
#         break
# #print("Unesite upit:")
# start_time = time.time()
# #root = obilazakFajlova.obidji(rootdir)
# #print(root)
# bool2 = '1'
# while bool2 == '1':
#     bool = False
#     while not bool:
#         query = input("Unesite upit: ")
#         (bool, logop, search) = queryParser.parse(query)
#     print(logop)
#     # konacanSet = set.Set(False, 0, {})
#     konacanSet = searchAlgorithm.find(root, search, logop)
#     print("--- %s seconds ---" % (time.time() - start_time))
#     # print(counters['C:\\python-2.7.7-docs-html\\whatsnew\\2.0.html'])
#     # lista = rangiranje.rangiraj(counters, links)
#     print(konacanSet)
#     bool2 = input("Ako zelite ponovo da pretrazite unesite broj 1, u suprotnom unesite pritisnite ENTER: ")
bool1 = '1'
bool2 = '1'
while bool1 == '1':
    if bool2 == '1':
        while True:
            rootdir = input("Unesite korenski direktorijum: ")
            (bool, root) = obilazakFajlova.obidji(rootdir)
            if bool == True:
                break
        print('**********************************************************************\n')
        bool2 = input('Ako zelite ponovo da unesete korenski direktorijum, unesite broj 1\nAko zelite da unesete upit, unesite broj 2\nAko zelite da izadjete iz programa, unesite broj 3\nOpcija: ')
        print('\n**********************************************************************\n')
    elif bool2 == '2':
        bool3 = False
        while not bool3:
            query = input("Unesite upit: ")
            (bool3, logop, search) = queryParser.parse(query)
        #print(logop)
        # konacanSet = set.Set(False, 0, {})
        konacanSet = searchAlgorithm.find(root, search, logop)
        #print("--- %s seconds ---" % (time.time() - start_time))
        # print(counters['C:\\python-2.7.7-docs-html\\whatsnew\\2.0.html'])
        # lista = rangiranje.rangiraj(counters, links)
        print('\n**********************************************************************\n')
        print(konacanSet)
        print('**********************************************************************\n')
        bool2 = input('Ako zelite da unesete novi korenski direktorijum, unesite broj 1\nAko zelite ponovo da unesete upit, unesite broj 2\nAko zelite da izadjete iz programa, unesite broj 3\nOpcija: ')
        print('\n**********************************************************************\n')
    elif bool2 == '3':
        bool1 = '3'
    else:
        bool2 = input("Unesite jednu od opcija(1, 2, 3): ")

#print(type(konacanSet))
"""
root = trie.TrieNode('*')
parser = Parser()
parser.parse(rootdir)
i = 0
for word in parser.words:
    if word == 'Python':
        i = i+1
        print('************************** ' , i , ' ****************************')
    else:
        print(word)
    trie.add(root, word)

print(trie.find_prefix(root, 'Python'))
"""
#print(trie.find_prefix(root, 'Python'))

