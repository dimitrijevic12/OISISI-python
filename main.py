import obilazakFajlova
import queryParser
import searchAlgorithm
import rangiranje
import time

#print("Unesite korenski direktorijum: ")
while True:
    rootdir = input("Unesite korenski direktorijum: ")
    (bool, root) = obilazakFajlova.obidji(rootdir)
    if bool == True:
        break
#print("Unesite upit:")
start_time = time.time()
#root = obilazakFajlova.obidji(rootdir)
#print(root)
while True:
    query = input("Unesite upit: ")
    (bool, logop, search) = queryParser.parse(query)
    if bool == True:
        break

listaStranica = searchAlgorithm.find(root, search)
print("--- %s seconds ---" % (time.time() - start_time))
#print(counters['C:\\python-2.7.7-docs-html\\whatsnew\\2.0.html'])
#lista = rangiranje.rangiraj(counters, links)
for stranica in listaStranica:
    print("Ukupno ima: ", stranica[1])
for element in listaStranica:
     print(element)
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

