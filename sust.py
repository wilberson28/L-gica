class Formula :
    def __init__(self) :
        pass
    
    
    def __str__(self) :
        if type(self) == Letra:
            return self.letra
        elif type(self) == Negacion:
            return '-' + str(self.subf)
        elif type(self) == Binario:
            return "(" + str(self.left) + self.conectivo + str(self.right) + ")"
    
    
    ##conjunto de letras

    def conj_letras(self):
        if type(self) == Letra:
            return set(self.letra)
        elif type(self) == Negacion:
            return self.subf.conj_letras()
        elif type(self) == Binario:
            return self.left.conj_letras().union(self.right.conj_letras())


    #conjunto de subformulas
    def subforms(self):
        if type(self) == Letra:
            return set(self.letra)
        elif type(self) == Negacion:
            return {str(self)}.union(self.subf.subforms())
        elif type(self) == Binario:
            return {str(self)}.union(self.left.subforms().union(self.right.subforms()))

    #SUSTITUCION
    def sust(self,a,b):
        if a not in self.subforms():
            return self
        elif a==self:
            return b
        elif type(self) == Negacion:
            return Negacion(self.subf.sust(a,b))
        elif type(self) == Binario:
            return Binario(self.conectivo, self.left.sust(a,b), self.right.sust(a,b))
    
    
    
    
    
    
    
    
    
    
    
    #num subforms
    def num_subforms(self) :
        if type(self) == Letra:
            return 1
        elif type(self) == Negacion:
            return 1 + self.subf.num_subforms()
        elif type(self) == Binario:
            return 1+ self.left.num_subforms() + self.right.num_subforms()

    #setattr(Formula, "num_subforms", num_subforms)




    def num_conec(self) :
        if type(self) == Letra:
            return 0
        elif type(self) == Negacion:
            return 1 + self.subf.num_conec()
        elif type(self) == Binario:
            return 1 + self.left.num_conec() + self.right.num_conec()

    #setattr(Formula, "num_conec", num_conec)

    def num_paren(self) :
        if type(self) == Letra:
            return 0
        elif type(self) == Negacion:
            return 0 + self.subf.num_paren()
        elif type(self) == Binario:
            return 2 + self.left.num_paren() + self.right.num_paren()

    #setattr(Formula, "num_paren", num_paren)

    def num_letras(self):
        if type(self)==Letra:
            return 1
        elif type(self) == Negacion:
            return 0 + self.subf.num_letras()
        elif type(self) == Binario:
            return 0 + self.left.num_letras() + self.right.num_letras()

    #setattr(Formula, "num_letras", num_letras)

    def num_bin(self):
        if type(self)==Letra:
            return 0
        elif type(self) == Negacion:
            return 0 + self.subf.num_bin()
        elif type(self) == Binario:
            return 1 + self.left.num_bin() + self.right.num_bin()

    #setattr(Formula, "num_bin", num_bin)

    def num_neg(self):
        if type(self)==Letra:
            return 0
        elif type(self) == Negacion:
            return 1 + self.subf.num_neg()
        elif type(self) == Binario:
            return 0 + self.left.num_neg() + self.right.num_neg()

    #setattr(Formula, "num_neg", num_neg)
    
    
    
    
    
  

class Letra(Formula) :
    def __init__ (self, letra:str) :
        self.letra = letra

class Negacion(Formula) :    
    def __init__(self, subf:Formula) : 
        self.subf = subf

class Binario(Formula) :
    def __init__(self, conectivo:str, left:Formula, right:Formula) :
        assert(conectivo in ['Y','O','>','='])
        self.conectivo = conectivo
        self.left = left
        self.right = right

def __str__(self) :
    if type(self) == Letra:
        return self.letra
    elif type(self) == Negacion:
        return '-' + str(self.subf)
    elif type(self) == Binario:
        return "(" + str(self.left) + self.conectivo + str(self.right) + ")"
    
setattr(Formula, "__str__", __str__)


f=Binario('Y',Letra('p'),Negacion(Letra('q')))
print(f.sust(Binario('Y',Letra('p'),Negacion(Letra('q'))),Letra('q')))

#