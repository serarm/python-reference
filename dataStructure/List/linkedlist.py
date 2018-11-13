
# coding: utf-8

# In[11]:


class Node:
    def __init__(self, data):
        self.data = data
        self.nextElement = None
    def __str__(self):
        return str(self.data)


# In[23]:


class LinkedList:
      def __init__(self):
        self.headNode = Node(-1)
    
      def insertAtHead(self,dt):
        tempNode= Node(dt)
        tempNode.nextElement = self.headNode.nextElement
        self.headNode.nextElement = tempNode
        return self.headNode
  
      def isEmpty(self): 
        if(self.headNode.nextElement == None):
            return True
        else :
            return False
        
    
      def insertAtEnd(self,dt):
        tempNode=Node(dt)
        currentNode=self.headNode
        while currentNode.nextElement:
            currentNode=currentNode.nextElement
        currentNode.nextElement=tempNode
        
    
      def __str__(self):
            result=""
            if(self.isEmpty()):
                result="List is Empty"
                return result   
            temp=self.headNode.nextElement     
            while(temp.nextElement!=None):
                result=result+str(temp.data)+ "->"
                temp=temp.nextElement    
            result+=str(temp.data)+ "-> None"
            return result 


# In[24]:


def main():
    lst = LinkedList()
    print(lst)
    for i in range(1,10,1):
        lst.insertAtHead(i)
    print(lst)
    for i in range(10,15):
        lst.insertAtEnd(i)
    print(lst)
if __name__=='__main__':
    main()

