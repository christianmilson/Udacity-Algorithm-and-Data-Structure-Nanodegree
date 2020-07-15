## Represents a single node in the Trie
class TrieNode:
    def __init__(self, value=None):
        ## Initialize this node in the Trie
        self.value = value
        self.children = {}
        self.word = False
    
    def insert(self, char):
        ## Add a child node in this Trie
        if (char not in self.children):
            self.children[char] = TrieNode(char)
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.head = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        node = self.head

        for char in word:
            if (word not in node.children):
                node.insert(char)
            node = node.children[char]

        node.word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        if (prefix is None or prefix == ''):
            return -1

        node = self.head

        for char in prefix:
            if (char in node.children):
                node = node.children[char]
            else:
                return -1

        return self.search(node, '')

    def search(self, node, word):
        ## Search all children nodes until u reach a word
        words = []
        if (node.word == True and word != ''):
            words.append(word)

        for letter in node.children:
            words += self.search(node.children[letter], word + letter)

        return words

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]

for word in wordList:
    MyTrie.insert(word)

print('Pass' if (MyTrie.find('a') == ['nt', 'nthology', 'ntagonist', 'ntonym']) else 'Fail')
print('Pass' if (MyTrie.find('c') == -1) else 'Fail')
print('Pass' if (MyTrie.find('fun') == ['ction']) else 'Fail')
print('Pass' if (MyTrie.find(None) == -1) else 'Fail')
print('Pass' if (MyTrie.find('') == -1) else 'Fail')
