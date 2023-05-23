# A class to create a new node
 
 
class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
# Returns maximum value in a
# given Binary Tree
 
 
def find_min(root):
 
    # Base case
    if (root == None):
        return float('inf')
 
    # Return minimum of 3 values:
    
    res = root.data
    lres = find_min(root.left)
    rres = find_min(root.right)
    if (lres < res):
        res = lres
    if (rres < res):
        res = rres
    return res
 
# Driver Code
if __name__ == '__main__':
    root = newNode(2)
    root.left = newNode(7)
    root.right = newNode(5)
    root.left.right = newNode(6)
    root.left.right.left = newNode(1)
    root.left.right.right = newNode(11)
    root.right.right = newNode(9)
    root.right.right.left = newNode(4)
 
    # Function call
    print("*******************************************Welcome to Binary Tree ********************************************\n minimum element is",
          find_min(root))