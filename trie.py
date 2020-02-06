from typing import Tuple

class TrieNode(object):
    """
    Our trie node implementation. Very basic. but does the job
    """

    def __init__(self, char: str):
        self.char = char
        self.children = []
        # Is it the last character of the word.`
        self.word_finished = False
        # How many times this character appeared in the addition process
        self.counters = []
        self.links = []
        self.paths = []

def add(root, word: str, path: str, links):
    """
    Adding a word in the trie structure
    """
    temp = 0
    node = root
    for char in word:
        found_in_child = False

        # Search for the character in the children of the present `node`
        for child in node.children:
            if child.char == char:
                # We found it, increase the counter by 1 to keep track that another
                # word has it as well
                node = child

                # And point the node to the child that contains this char
                found_in_child = True
                break
        # We did not find it so add a new child
        if not found_in_child:
            new_node = TrieNode(char)
            new_node.counters.append(1)
            new_node.paths.append(path)
            new_node.links.append(links)
            node.children.append(new_node)
            # And then point node to the new child
            node = new_node
            temp = 1
    # Everything finished. Mark it as the end of a word.
    node.word_finished = True
    if temp != 1:
        if path not in node.paths:
            node.paths.append(path)
            node.counters.append(1)
            node.links.append(links)
        else:
            i = -1
            for path in node.paths:
                i = i + 1
            node.counters[i] += 1
    """if path not in node.paths:
        node.paths.append(path)
        node.counters.append(1)
        node.links.append(links)
    else:
        i = -1
        for path in node.paths:
            i = i + 1
        node.counters[i] += 1"""


def find(root, prefix: str) -> Tuple[bool, int, list, list]:
    """
    Check and return
      1. If the prefix exsists in any of the words we added so far
      2. If yes then how may words actually have the prefix
    """
    node = root
    #linkovi = []
    # If the root node has no children, then return False.
    # Because it means we are trying to search in an empty trie
    if not root.children:
        return False, 0
    for char in prefix:
        char_not_found = True
        # Search through all the children of the present `node`
        for child in node.children:
            if child.char == char:
                # We found the char existing in the child.
                char_not_found = False
                # Assign node as the child containing the char and break
                node = child
                """
                for link in node.links:
                    if link not in linkovi:
                        linkovi.append(link)
                linkovi = list(set(linkovi))
                """
                break
        # Return False anyway when we did not find a char.
        if char_not_found:
            return False, 0
    # Well, we are here means we have found the prefix. Return true to indicate that
    # And also the counter of the last node. This indicates how many words have this
    # prefix
    if node.word_finished == True:
        print(node.word_finished)
        return True, node.counters, node.paths, node.links
    else:
        return False, [], [], []