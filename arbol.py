class Arbol :
    
    def __init__(self, iz, der) :
        self.left=iz
        self.right=der
    
    
    def num_hojas(self):
        if self.left==None:
            return 1
        else:
            return self.left.num_hojas() + self.right.num_hojas()
    
    def num_aristas(self):
        if self.left == None:
            return 0
        else:
            return 2 + self.left.num_aristas() + self.right.num_aristas()
    
    def num_nodos(self):
        if Arbol.left == None:
            return 1
        else:
            return 1 + self.left.num_nodos() + self.right.num_nodos()
    
    def altura(self):
        if self.left == None:
            return 0
        else:
            return 1 + max(self.left.altura(), self.right.altura())
        
h=Arbol(None,None)
r2=Arbol(h,h)
r1=Arbol(r2,h)

print(r1.altura())