#https://gist.githubusercontent.com/red574890/0a703356947ad4618d787c89f5402f0e/raw/3480953838e6521c212fd81b351f59c0d8087a30/WQUPC.py
#https://medium.com/datascienceray/quick-union-improvement-6798449e2781
class WQUPC():

    def __init__(self,N):
        if(type(N)!=int):
            print("Size must be integer")
        else:
            self.id_array=list(range(0,N))
            self.size=N
            self.sz=[1]*10 # size array for weighted structure

    def root(self,i):
        if(type(i)!=int):
            print("Input must be integer")
        else: 
            while(i!=self.id_array[i]):  # iteratively track up to find root
                self.id_array[i]=self.id_array[self.id_array[i]]
                i=self.id_array[i]
            return i

    def connected(self,p,q):
        if(type(p)!=int or type(q)!=int):
            print("Input must be integer")
        else:
            return self.root(p)==self.root(q)     # check whether two nodes have the same root

    def union(self,p,q):
        if(type(p)!=int or type(q)!=int):
            print("Input must be integer")
        else:
            i = self.root(p)
            j = self.root(q)
            if(i == j): return # same root, no need to do union
            if(self.sz[i]<self.sz[j]): # link smaller size tree to larger size tree
                self.id_array[i]=j  
                self.sz[j]+=self.sz[i] # add the size of smaller tree to bigger tree
            else:
                self.id_array[j]=i
                self.sz[i]+=self.sz[j] # add the size of smaller tree to bigger tree
