import obilazakFajlova
import queryParser
import searchAlgorithm
import rangiranje
import time

print("Unesite korenski direktorijum: ")
rootdir = input()

print("Unesite upit:")
query = input()

start_time = time.time()
root = obilazakFajlova.obidji(rootdir)
#print(root)

(logop, search) = queryParser.parse(query)
(tacno, counter, counters, links) = searchAlgorithm.find(root, logop, search)
print("--- %s seconds ---" % (time.time() - start_time))
#lista = rangiranje.rangiraj(counters, links)
print("Ukupno ima: ", counter)
"""for element in lista:
    print(element)"""
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

