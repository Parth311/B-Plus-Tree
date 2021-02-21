import sys

class TreeNode(object):
    def __init__(self):
        self.keys=[]
        self.child=[]
        self.par=None
        self.isLeaf=True
        self.next=None
        self.key_count=[]

    def get_left_leaf(self):
        temp=TreeNode()
        temp=self

        if len(temp.child) == 0:
            return None

        while  temp.isLeaf == False:
            temp = temp.child[0]

        return temp

    def add_key(self,key):
        if len(self.keys) == 0:
            self.keys.append(key)
            self.key_count.append(1)
            return
        
        for i in range(len(self.keys)):
            if self.keys[i] == key:
                self.key_count[i]+=1
                return

        ind = 0

        for k in self.keys:
            if key < k:
                
                self.keys = self.keys[:ind] + [key] + self.keys[ind:]
                self.key_count = self.key_count[:ind] + [1] + self.key_count[ind:]

                return
            ind+=1

        
        self.keys.append(key)
        self.key_count.append(1)
        return 


    def split_node(self,parent,cp):
        t=root.get_left_leaf()
        self.isLeaf=False
        length = len(self.keys)

        if length  <= (order-1):
            return


        mid=length//2
        left=TreeNode()
        right=TreeNode()

        if cp == 0:

            left.keys=self.keys[:mid]               # LEFT: [21,22]
            right.keys=self.keys[mid:]              # RIGHT: [23,24]

            left.key_count=self.key_count[:mid]
            right.key_count=self.key_count[mid:]


            if t!=None and t!=self:
                while t.next!=self:
                    t=t.next

                t.next=left

            left.par=parent
            right.par=parent

            left.next=right

            self.keys=[right.keys[0]]
            self.child=[left,right]

        if cp == 1:

            temp_keys=self.keys
            temp_child=self.child

            left.keys=self.keys[:mid]               
            right.keys=self.keys[mid+1:]

            left.child=self.child[:mid+1]
            right.child=self.child[mid+1:]

            left.isLeaf=False
            right.isLeaf=False

            self.keys=[self.keys[mid]]

            self.child=[left,right]

            

            

        # MERGING WITH THE PARENT NODE
        if parent!=None:
            ind = 0
            flag=False
            for k in parent.keys:
                if self.keys[0] < k:
                    parent.keys = parent.keys[:ind] + self.keys + parent.keys[ind:]

                    if ind == 0:
                        parent.child = self.child + parent.child[1:]
                    else:
                        parent.child = parent.child[:ind] + self.child + parent.child[ind+1:]
        
                    flag=True
                    break
                ind+=1

            if flag == False:
                parent.keys.append(self.keys[0])


                if parent.child[-1].next != None:
                    self.child[1].next = parent.child[-1].next
                    parent.child[-1].next = self.child[0]

                parent.child[-1] = self.child[0]
                parent.child.append(self.child[1])

            if cp == 0:
                for i in range(len(parent.child)-1):
                    parent.child[i].next=parent.child[i+1]
        
            if len(parent.keys) > (order-1):
                parent.split_node(parent.par,1)



    def display(self,count):
        print(count,str(self.keys))

        if self.isLeaf == False:
            for i in self.child:
                i.display(count+1)

def find_child(node,key):
    ind=0
    for k in node.keys:
        if key < k:
            return node.child[ind],ind
        ind+=1

    return node.child[ind],ind


def insert(key):
    node=root
    parent=None
    ind=0

    while node.isLeaf == False:
        parent=node
        node,ind = find_child(node,key)
        node.par = parent


    node.add_key(key)

    if len(node.keys) > (order-1):
        node.split_node(parent,0)


def find(key):
    node=root
    ind=0

    while node.isLeaf == False:
        node,ind = find_child(node,key)

    for k in node.keys:
        if k==key:
            return "YES"
    return "NO"

def count(key):

    if find(key) == "NO":
        return 0

    node=root
    ind=0

    while node.isLeaf == False:
        node,ind = find_child(node,key)    

    for i in range(len(node.keys)):
        if node.keys[i] == key:
            return node.key_count[i]

def get_range(key1,key2):
    node=root
    ind=0

    while node.isLeaf == False:
        node,ind = find_child(node,key1)  

    count_val=0

    while node!=None:
        for i in range(len(node.keys)):
            if node.keys[i] >= key1:
                if node.keys[i] > key2:
                    return count_val
                else:
                    count_val+=node.key_count[i]
        node=node.next

    return count_val

order = 3
root = TreeNode()

fi=open(sys.argv[1],'r')
fo=open('output.txt','w')

while True:
    cont=fi.readline()
    if len(cont) == 0:
        break
    cont=cont.replace('\n','')
    mylst=cont.split()

    if mylst[0].lower() == "insert":
        insert(int(mylst[1]))

    elif mylst[0].lower() == "find":
        fo.write(find(int(mylst[1]))+'\n')

    elif mylst[0].lower() == "count":
        fo.write(str(count(int(mylst[1])))+'\n')

    elif mylst[0].lower() == "range":
        fo.write(str(get_range(int(mylst[1]),int(mylst[2])))+'\n')    

    else:
        print("Invaid query: ",cont)    

fi.close()
fo.close()