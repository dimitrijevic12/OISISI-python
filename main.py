import obilazakFajlova
from analyzer import Parser
import trie

rootdir = r"C:\Users\Nemanja\PycharmProjects\PYTHON-OISISI-projekat\python-2.7.7-docs-html\faq"

root = obilazakFajlova.obidji(rootdir)

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
print(trie.find_prefix(root, 'Python'))

