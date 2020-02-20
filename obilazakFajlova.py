import os
from analyzer import Parser
import trie

def obidji(rootdir):
    root = trie.TrieNode('*')
    found = 0
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            if file.endswith('.html'):
                found = 1
                parser = Parser()
                parser.parse(os.path.join(subdir, file))
                for word in parser.words:
                    trie.add(root, word.lower(), os.path.join(subdir, file))
    if found == 0:
        print("Ne postoji html dokument u korenskom direktorijumu: ", rootdir)
        return False, root
    return True, root
