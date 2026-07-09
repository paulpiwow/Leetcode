class TrieNode: #create trieNode for the trie
    def __init__(self):
        self.children = {}  #hashmap for the 26 possible children
        self.endOfWord = False  #mark each node as if it is the end of a word

class Trie(object):

    def __init__(self):
        self.root = TrieNode()  #just initailize an empty tree

    def insert(self, word):
        #Iterate through every letter in the word
        cur = self.root

        for c in word:
            if c not in cur.children:   #is this char in our hashmap
                cur.children[c] = TrieNode()    #create trie node for this charater - key value is the character
            cur = cur.children[c]  #update cur cause char already exists
        cur.endOfWord = True    #we went through every char

    def search(self, word):
        #Search if a word exists
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]   #set cur to the child node of that character
        return cur.endOfWord    #if this is a word it will be set to true

    def startsWith(self, prefix):
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False    #the prefix does not exists
            cur = cur.children[c]
        return True #there is at least one word that has our prefix
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)