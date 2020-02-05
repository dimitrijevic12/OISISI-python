import obilazakFajlova
import queryParser
import trie
import searchAlgorithm
import rangiranje

print("Unesite korenski direktorijum: ")
rootdir = input()

print("Unesite upit:")
query = input()

root = obilazakFajlova.obidji(rootdir)
#print(root)

(logop, search) = queryParser.parse(query)
(tacno, counters, paths, links) = searchAlgorithm.find(root, logop, search)
lista = rangiranje.rangiraj(counters, paths, links)
for element in lista:
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

