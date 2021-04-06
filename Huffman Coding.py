# Link to the Problem:- https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/

class createNode:
    def __init__(self, freq, symb, left = None, right = None):
        self.freq = freq;
        self.symb = symb;
        self.left = left;
        self.right = right;
        self.huff = '';


def printCode(node, val=''):
    newVal = val + str(node.huff);
    
    if(node.left):
        printCode(node.left, newVal);
    if(node.right):
        printCode(node.right, newVal);
        
    if(not node.left and not node.right):
        print(f'{node.symb} : {newVal}');
    
symbol = ['a', 'b', 'c', 'd', 'e', 'f']
freq = [5,9,12,13,16,45];

node = []
for i in range(len(symbol)):
    node.append(createNode(freq[i], symbol[i]));
    
while(len(node)>1):
    node = sorted(node, key = lambda x: x.freq);
    left = node[0];
    right = node[1];
    left.huff = '0';
    right.huff = '1';
    newNode = createNode(left.freq+right.freq, left.symb+right.symb, left, right);
    print(left.freq , right.freq, left.symb , right.symb, left.huff, right.huff)
    node.remove(left);
    node.remove(right);
    
    node.append(newNode);
printCode(node[0])
