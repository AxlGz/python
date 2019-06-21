# Operadores lógicos.

# and: se cumple cuando los dos es true
# or: se cumple cuando uno de los dos es true 
# not:Sirve para devolver un valor opuesto al booleano 
x = True
y = False


def operadorOr():
    global x,y
    if (x != True) or (y == False):
        print('uno de los dos es verdadero')




def operadorAnd():
    global x,y
    if x == True and y == False:
        print('Los dos son verdaderos')

 

def operadorNot():
    print(not x)


def printWelcome():
    print('Bienvenidos a platzi ventas')
    print('*' * 50)



if __name__ == '__main__':
    operadorOr()
    operadorAnd()
    operadorNot()
    pass


# ----___----___----___----___----___----___----___----___----___----___----___----___----___----___----___----___----___----___


# operadores de comparación:
#igual que: ==

#diferente que: !=

# mayor: >

# mayor o igual: >=

# menor: <

# menor o igual:<=

