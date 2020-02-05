import os
from analyzer import Parser
import trie

def obidji(rootdir):
    root = trie.TrieNode('*')
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            if file.endswith('.html'):
                parser = Parser()
                parser.parse(os.path.join(subdir, file))
                #print(parser.links)
                #print(os.path.join(subdir, file))
                for word in parser.words:
                   #print(word)
                    trie.add(root, word.lower(), os.path.join(subdir, file), parser.links)
    return root