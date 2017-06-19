# Python program to build dictionary using Trie data structure
charToIndex = lambda x: ord(x) - ord('a')

# TrieNode class performs core insert, search operations
class TrieNode:

    def __init__(self):
        self.children = {}
        self.isLeaf = False

    # creates a new trie node to insert for an index
    def __createNode__(self) : return TrieNode()

    # search the word characters from root till the level reaches the (len(word) + 1) and
    # isLeaf is set true
    def __search__(self, word, level=0):

        if (level < len(word)):
            index = charToIndex(word[level])
            if index in self.children.keys():
                level = level + 1
                return self.children[index].__search__(word, level)
        else:
            if self.isLeaf:
                return True
        return False
                
    # Map the index of character in the word as new trienode if not found any.
    # If the index already exists, move to the node pointed by the respective
    # character index and repeat the same till the level reaches len(word) + 1.
    def __insert__(self, word, level=0):

        if (level < len(word)):
            index = charToIndex(word[level])
            if index not in self.children.keys():
                 self.children[index] = self.__createNode__()
            level = level + 1
            self.children[index].__insert__(word, level)
        else :
            self.isLeaf = True

# Wrapper class exposed to user to create a Trie Node and perform necessary operations 
# like insert and search
class Trie:
    def __init__(self, root):
        self.node = root

    def insert(self, word):
        if word:
             self.node.__insert__(word)
        else:
             print 'Empty Strings are not supported'

    def search(self, word):
        if word:
             if self.node.__search__(word):
                print '{} - found in dictionary'.format(word)
             else:
                print '{} - not found in dictionary'.format(word)
        else:
             print 'Empty Strings are not supported'


#Driver program to test Trie insertion, deletion and searching
root = TrieNode()
dictionary = Trie(root)

dictionary.insert('the')
dictionary.insert('they')
dictionary.insert('tees')
dictionary.insert('geeks')
dictionary.insert('tee')
dictionary.search('the')
dictionary.search('te')
dictionary.search('tees')
dictionary.search('geeks')
