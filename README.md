


**Tipos de datos en Python**:
    *Enteros(int)*: En este grupo están todos los números, Enteros, long, etc:
    ejemplo: 1,2,3,2121,21,12654567,-858.

    *Booleanos(bool): Son los valores falso o verdadero, compatibles con todas las operacipones boobleanas (and,not,or):
    ejemplo: True, False.

    *Cadenas(string): Son las cadenas de texto:
    ejemplo: "Hola", "¿como estás?"

    *Listas: Son un grupo de array de datos, puede contener cualquiera de los datos anteriores:
    ejemplo: ["Hola",1,2,3,[1,2,3]]

    *Diccionarios: Son un grupo de datos que se acceden a partir de una clave:
    ejemplo:{"clave":"valor"}, {"nombre":"Axel"}

    *tuplas: Tambien son un grupo de datos igual que una lista con la diferencia que una tupla después de creada no se puede modificar

Nota: En Python trabajamos con módulos y ficheros que se usan para importar librerías.
<br>
**Funciones:**
Las Funciones se definen con def junto a un nombre y unos paréntesis que reciben los parámetros a usar.  Terminas con dos puntos.
	
	def nombreDeLafuncion(parámetros):
 Después por indentación colocas los datos que se ejecutarán desde la función:
 

    >>>def my_first_function():
    ...return "Hello World!!1!"
    ...
    >>>my_first_function()
   <br>
   **Variables:**
   Las variables, a diferencia de los demás lenguajes de programación, no debes definirlas, no tampoco su tipo de dato, ya que al momento de iterarlas se identificará su tipo. Recuerda que en Python todo es un objeto. <br>
   

    a = 3
    b = a
   
   <br> 
   
   **Listas (array)**:
   Las listas las declaras con corchetes. Estas pueden tener una lista dentro o cualquier tipo de dato. Siempre se empiezan a contar desde cero "0".

    >>> Lista= [22,,True,"Esto es una lista",[1,2]]
    >>> Lista=[0]
	22
   <br>

**Tuplas**:
Las tuplas se declaran con paréntesis, recuerda que no puedes editar los datos de una tupla después de que la has creado. 

    >>> Tupla: (22,True,"Una tupla we", (1,2))


   
**Diccionarios:**
En los diccionarios tienes un grupo de datos con un formato: la primera cadena o número será la clave para acceder al segundo dato, el segundo dato será el dato al cual accederás con la llave. Recuerda que los diccionarios son listas de llave:valor.

     >>> D = {"Kill Bill": "Tamarino", "Amelie": "Jean-Pierre Jeunet"}  
     >>> D["Kill Bill"]
		"Tamarino"

<br>

***CONVERSIONES:***
De flotante a entero:

    >>> int(4.3)
    4
 De entero a flotante:
 
    >>> float (4)
    4.0
 De entero/flotante a string:
 

    >>> str (4.3)
    '4.3'
De tupla a lista:

    >>>list ((4,5,2))
    [4,5,2]

