# Link to the Problem:- https://www.geeksforgeeks.org/efficient-huffman-coding-for-sorted-input-greedy-algo-4/

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
firstQueue = []
secondQueue = []
for i in range(len(symbol)):
    firstQueue.append(createNode(freq[i], symbol[i]));

while((len(firstQueue)+len(secondQueue))>1):
    elem = []
    for i in range(2):
        if(len(secondQueue) == 0):
            elem.append(firstQueue.pop(0))
        elif(len(firstQueue) == 0):
            elem.append(secondQueue.pop(0))
        else:
            if(firstQueue[0].freq < secondQueue[0].freq):
                elem.append(firstQueue.pop(0));
            else:
                elem.append(secondQueue.pop(0));
    elem[0].huff = '0';
    elem[1].huff = '1';
    newNode = createNode(elem[0].freq+elem[1].freq, elem[0].symb+elem[1].symb, elem[0], elem[1]);
    
    secondQueue.append(newNode);
printCode(secondQueue[0]);
