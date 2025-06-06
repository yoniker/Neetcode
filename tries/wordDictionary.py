

class WordDictionary:


    class TrieNode:
 
        def __init__(self,isWord=False):
            self.isWord = isWord
            self.lettersEdges=dict() #A dictionary where keys are letters and values are subsequent nodes
        def __str__(self):
            children_text = ''
            for k,v in self.lettersEdges.items():
                children_text = children_text + f'{k}:{v} '
            return f'TrieNode(isword:{self.isWord},children:[{children_text}] )'

    def __init__(self):
        self.root = WordDictionary.TrieNode()
    def __str__(self):
        return str(self.root)


    def __getLastNode(self,word):
        last_node_trie_with_prefix = self.root
        while len(word)>0 and (word[0] in last_node_trie_with_prefix.lettersEdges):
            last_node_trie_with_prefix = last_node_trie_with_prefix.lettersEdges[word[0]]
            word = word[1:]
        return last_node_trie_with_prefix,word 

        
    def addWord(self, word: str) -> None:
        #traverse the tree from root, until we get to a node from which we can't traverse further. Enter the rest of the word
        last_node_trie_with_prefix,word = self.__getLastNode(word)
        #Now i want to iteratively enter the word into the trie
        while len(word)>0:
            last_node_trie_with_prefix.lettersEdges[word[0]] = WordDictionary.TrieNode()
            last_node_trie_with_prefix = last_node_trie_with_prefix.lettersEdges[word[0]]
            word = word[1:]
        last_node_trie_with_prefix.isWord = True 

    def _searchFromNode(self,currentNode,word):
        if word=='':
            if currentNode and currentNode.isWord:
                return True
            return False

        
        if word[0]=='.':
            for letter in currentNode.lettersEdges.keys():
                if self._searchFromNode(currentNode=currentNode.lettersEdges[letter],word=word[1:]):
                    return True
            return False
        if word[0] not in currentNode.lettersEdges:
            return False
        return self._searchFromNode(currentNode=currentNode.lettersEdges[word[0]],word = word[1:])
            


    def search(self, word: str) -> bool:
        return self._searchFromNode(currentNode=self.root,word=word)

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

a = Trie()
a.insert('dorking')
print(a)



#1,2,3,5