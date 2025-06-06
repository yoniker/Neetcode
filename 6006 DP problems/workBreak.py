from types import List

class Trie:
    class TrieNode:
        def __init__(self):
            self.isWord=False
            self.lettersEdges = dict()
    
    def __init__(self):
        self.root = Trie.TrieNode()

    def addWord(self,word):
        currentNode = self.root
        for c in word:
            if c not in currentNode.letterEdges:
                currentNode.letterEdges[c] = Trie.TrieNode()
            currentNode = currentNode.letterEdges[c]
        currentNode.isWord = True
        




class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordsTrie = Trie()
        #1. Add words to trie
        for word in wordDict:
            wordsTrie.addWord(word)
        memPad = dict()
        def isInterprateable(i): #Is it possible to interpret all the characters starting from i using the words in dictionary
            if i>=len(s):
                return True
            if i in memPad:
                return memPad[i]
            currentNodeAtTrie = wordDict.root
            for j in range(i,len(s)):
                if s[j] not in currentNodeAtTrie.letterEdges:
                    return False
                currentNodeAtTrie = currentNodeAtTrie.letterEdges[s[j]]
                #if I can interpret this as a word then I can try the substring without it
                if currentNodeAtTrie.isWord:
                    if isInterprateable(j):
                        memPad[i] = True
                        return memPad
        return isInterprateable(0)


        