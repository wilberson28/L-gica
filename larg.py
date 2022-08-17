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
    
    def letras(self):
        if type(self) == Letra:
            return set(self.letra)
        elif type(self) == Negacion:
            return self.subf.letras()
        elif type(self) == Binario:
            return self.left.letras().union(self.right.letras())

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
        
#
#evalua el valor dependiendo un diciionario que le demos
def valor(self, I) :
    if type(self) == Letra:
        return I[self.letra]
    elif type(self) == Negacion:
        return not self.subf.valor(I)
    elif type(self) == Binario:
        if self.conectivo == 'Y':
            return self.left.valor(I) and self.right.valor(I)
        if self.conectivo == 'O':
            return self.left.valor(I) or self.right.valor(I)
        if self.conectivo == '>':
            return not self.left.valor(I) or self.right.valor(I)
        if self.conectivo == '=':
            return (self.left.valor(I) and self.right.valor(I)) or (not self.left.valor(I) and not self.right.valor(I)) 

setattr(Formula, "valor", valor)


####
#toma una cadena y devuelve un objeto formula
def inorder_to_tree(cadena:str):
    conectivos = ['Y', 'O', '>', '=']
    if len(cadena) == 1:
        return Letra(cadena)
    elif cadena[0] == '-':
        return Negacion(inorder_to_tree(cadena[1:]))
    elif cadena[0] == "(":
        counter = 0 #Contador de parentesis
        for i in range(1, len(cadena)):
            if cadena[i] == "(":
                counter += 1
            elif cadena[i] == ")":
                counter -=1
            elif cadena[i] in conectivos and counter == 0:
                return Binario(cadena[i], inorder_to_tree(cadena[1:i]),inorder_to_tree(cadena[i + 1:-1]))
    else:
        raise Exception('¡Cadena inválida!')

##
##interpretaciones
from itertools import product

interpretaciones = list(product([True,False], [True,False]))
interpretaciones

interpretaciones = list(product([True,False], [True,False]))
interpretaciones
print('Dando prioridad a and')
print('-'*36)
print('p     q       not (p and q) ')
print('-'*36)
for I in interpretaciones:
    p = I[0]
    q = I[1]
    espacio1 = '  ' if p else ' '
    espacio2 = '    ' if q else '   '
    
    print(f'{p}{espacio1}{q}{espacio2}{not (p and q)}')

print('')
print('Dando prioridad a not')
print('-'*36)
print('p     q      (not p) and q')
print('-'*36)
for I in interpretaciones:
    p = I[0]
    q = I[1]
    espacio1 = '  ' if p else ' '
    espacio2 = '    ' if q else '   '
    print(f'{p}{espacio1}{q}{espacio2}{(not p) and q}')

print('')
print('Prioridad de Python')
print('-'*36)
print('p     q     not p and q')
print('-'*36)
for I in interpretaciones:
    p = I[0]
    q = I[1]
    espacio1 = '  ' if p else ' '
    espacio2 = '    ' if q else '   '
    print(f'{p}{espacio1}{q}{espacio2}{not p and q}')


print("\n\n")




p = Letra('p')
q = Letra('q')
A1 = Negacion(p)
A2 = Binario('>', p, q)
A3 = Negacion(A2)
A4 = Binario('=', Negacion(q), A3)

I = {'p':True, 'q':False}
print(f'{p} tiene el valor {p.valor(I)}')
print(f'{q} tiene el valor {q.valor(I)}')
print(f'{A1} tiene el valor {A1.valor(I)}')
print(f'{A2} tiene el valor {A2.valor(I)}')
print(f'{A3} tiene el valor {A3.valor(I)}')
print(f'{A4} tiene el valor {A4.valor(I)}')
print("\n")


prueba1 = "(-p>((pY-q)>(pYq)))"
prueba2 = "(-pOq)"
prueba3 = "(pY-q)"

Tree = inorder_to_tree(prueba1)
Tree2 = inorder_to_tree(prueba2)
Tree3 = inorder_to_tree(prueba3)

print(Tree)
print(Tree2)
print(Tree3)


