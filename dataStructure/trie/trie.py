
# coding: utf-8

# # What is Trie?

# “Trie” basically comes from the word “retrieval”, as the main purpose of using this structure is that it provides fast retrieval. Tries are mostly used for searching words in the dictionary, provide auto-suggestions in search engines, and for IP routing as well.

# ## Define TrieNode

# In[1]:


class TrieNode:
    def __init__(self):
        self.children=[None]*26
        #Let's assume Trie is for english alphabet
        #Intialise all children to none
#         for i in range(26):
#             self.children.append(None)
        self.val=-1
        self.flagEndWord=False
    #Function to mark current node as leaf
    def markAsLeaf(self,val):
        self.val=val
        self.flagEndWord=True
    
    #Function to unmark current node as leaf
    def unmarkAsLeaf(self):
        self.val=-1
        self.flagEndWord=False
    def isLeaf(self):
        return self.flagEndWord


# ## Implementing TRIE class

# In Tries, Insertion is a lengthy process. It depends on how lengthy the words are and how many words the Trie contains. 
# In worst case scenario, a Trie takes O(N*M) time where M is the number of words present in Tries and N is the length of the longest word. 
# Same goes for Searching and Deletion in Tries.
# You need to perform at least N lookups for all M words.

# In[2]:


class Trie:
    def __init__(self):
        self.root = TrieNode() #Root node
    
      #Function to get the index of character 't'
    def getIndex(self,t):
        return ord(t) - ord('a')
  
      #Function to insert a key,value pair in the Trie
    def insert(self,key,value):
        #If Key is None return
        
        if key==None:
            return
        currentNode=self.root
        for i in range(len(key)):
            tempkey=key[i].lower()
            index=self.getIndex(tempkey)
            if currentNode.children[index]==None:
                currentNode.children[index]=TrieNode()
            currentNode=currentNode.children[index]
        currentNode.markAsLeaf(value)
        
    
      #Function to search a given key in Trie
    def search(self,key):
        if key==None:
            return False
        currentNode=self.root
        for i in range(len(key)):
            tempkey=key[i].lower()
            index=self.getIndex(tempkey)
            
            if currentNode.children[index]==None:
                return False
            currentNode=currentNode.children[index]
                  
        return currentNode!=None and currentNode.isLeaf()
  
      #Function to delete given key from Trie
    def delete(self,key):
        if self.root== None or key==None:
            print("Error condition :either key or Trie is Null")
        elif not self.search(key):
            print("Key is not present")
        #Case 1 no childern or included word
  


# In[5]:


def main():
    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the", "a", "there", "answer", "any",
                     "by", "bye", "their","abc"]
    output = ["Not present in trie", "Present in trie"]
    search_keys=['the','these','abc','be','bygone']
    
    t = Trie()
    print("Keys to insert: ")
    print(keys)
    
    #Construct Trie
    for i in range(len(keys)):
        t.insert(keys[i], i)
    for key in search_keys:
        result= output[1] if t.search(key) else output[0]
        print("{} ---- {}".format(key,result))
        if not t.search(key):
            t.insert(key,1)
            print("=======================================")
            print("Checking again for key :{}".format(key))
            result= output[1] if t.search(key) else output[0]
            print("{} ---- {}".format(key,result))
            print("=======================================")
if __name__=='__main__':
    main()

