class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        
    def search(self, word):
        return self.dfs(word, 0, self.root)

    def dfs(self, word, index, node):
            if index == len(word):
                return node.is_end
            
            char = word[index]

            if char == '.':
                for child in node.children.values():   # try every possible child node
                    if self.dfs(word, index + 1, child):    # if any path succeeds
                        return True                         # return True immediately
                return False                            # no child path worked
            else:
                if char not in node.children:           # character doesn't exist in trie
                    return False
                return self.dfs(word, index + 1, node.children[char]) 
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)