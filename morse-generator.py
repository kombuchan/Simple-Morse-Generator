
from collections import deque

class node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None
    

queue = deque()

def insertValue(data, root):
	newNode = node(data)
	if queue: temp = queue[0]

	if root == None: root = newNode

	elif temp.left == None: temp.left = newNode
	
	elif temp.right == None:
		temp.right = newNode
		atemp = queue.popleft()

	queue.append(newNode)
	return root


def createTree():
    treeOrder = ".ETIANMSURWDKGOHVF-L-PJBXCYZQ--"
    root = None
    for i in range(len(treeOrder)): 
        root = insertValue(treeOrder[i], root)
    return root

def dfs(node,target,path,morse):
    if node == None: return False
    path.append(node.data)
    if node.data == target: return True
    if dfs(node.left,target,path,morse):
        morse.append('.')
        return True
    if dfs(node.right,target,path,morse):
        morse.append('-')
        return True
    path.pop()
    return False


def morse_Generator(root,s): 
    for c in s.upper():
        if c.isalpha():
            path = []
            morse = []
            dfs(root,c,path, morse)
            print("".join(morse[::-1]),end=" ")
        

def driver(sentence):
    head = createTree()
    for i in range(len(sentence.split())):
        root = head
        morse_Generator(root,sentence.split()[i])
        if i < len(sentence.split())-1 : print("/",end="")
        

driver("Wubba Lubba Dub Dub")


        
