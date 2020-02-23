import os
from parseri.analyzer import Parser
from strukturePodataka import trie
from strukturePodataka.graf import Graph

def obidji(rootdir):
    root = trie.TrieNode('*')
    graf = Graph()
    found = 0
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            if file.endswith('.html'):
                found = 1
                parser = Parser()
                parser.parse(os.path.join(subdir, file))
                graf.add_site(os.path.join(subdir, file), parser.links)
                for word in parser.words:
                    trie.add(root, word.lower(), os.path.join(subdir, file))
    if found == 0:
        print("Ne postoji html dokument u korenskom direktorijumu: ", rootdir)
        return False, root,graf
    return True, root,graf
