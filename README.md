


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
<br><br>
**Funciones:**
Las Funciones se definen con def junto a un nombre y unos paréntesis que reciben los parámetros a usar.  Terminas con dos puntos.
	
	def nombreDeLafuncion(parámetros):
 Después por indentación colocas los datos que se ejecutarán desde la función:
 

    >>>def my_first_function():
    ...return "Hello World!!1!"
    ...
    >>>my_first_function()+
    
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

<br>

**Ordenadores Comunes:**
Longitud de una cadena,lista,tupla,etc.:
   >>> len("hey :D")
   6

Tipo de dato:
   >>> type (4)
   < class int >

Aplicar una conversion a un conjunto como una lista:

   >>>map(str,[1,2,3,4])
   <map object at 0x7f5573fbcb00>

   *Si lo queremos mostrar en forma de lista tiene que ser así:*
   >>>print(list(map(str,[1,2,3,4])))
   ['1','2','3','4']

Redondear un Float con x número de decimales:

   >>>round(6.12234234253, 2)
   6.12

Generar un rango en una lista:
   >>>range(5)
   [0,1,2,3,4]

Sumar un conjunto:
   >>>sum([1,2,4])
   7

Organizar un conjunto:
   >>> sorted([5,2,1])

Conocer los comandos que le puedes aplicar a x tipo de datos:
   >>>Li = [1,2,8,5]
   >>>dir(Li)
   >>>[ 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

Información sobre una función o librería:
   >>help(sorted)

<br>

**Clases:**

Clases es uno de los conceptos con más definiciones en la programación, pero en resumen sólo son la representación de un objeto. Para definir la clase usas_ class_ y el nombre. En caso de tener parámetros los pones entre paréntesis.

Para crear un constructor haces una función dentro de la clase con el nombre init y de parámetros self (significa su clase misma), nombre_r y edad_r:

<br>

**Métodos especiales:**

cmp(self,otro)
Método llamado cuando utilizas los operadores de comparación para comprobar si tu objeto es menor, mayor o igual al objeto pasado como parámetro.

len(self)
Método llamado para comprobar la longitud del objeto. Lo usas, por ejemplo, cuando llamas la función len(obj) sobre nuestro código. Como es de suponer el método te debe devolver la longitud del objeto.

init(self,otro)
Es un constructor de nuestra clase, es decir, es un “método especial” que se llama automáticamente cuando creas un objeto.

<br>

**Condicional if**:

Los condicionales tienen la siguente estructura. Ten en cuenta que lo que contiene los paréntesis es la comparación que debe cumplir para que os elementos se cumplan.
   
   if( a > b):
      elementos
   elif ( a == b):
      elementos
   else:
      elementos

**Blucle for**:
El bucle de for lo puedes usar de la siguiente forma: recorres una cadena o lista a la cual va a tomar el elemento en cuestión con la siguiente estructura:

   for i in ___:
      elementos
   
Ejemplo:

   >>>for i in range(5):
   ...   print(i)

**Bucle while:**

En este caso while tienen una condición que determina hasta cuándo se ejecutará. O sea que dejará de ejecutarse en el momento en el que la condición deje de ser cierta. La estructura de un while es la siguiente:

   while(condición):
      elementos

Ejemplos:
   >>>x = 0
   >>>while x <10:
   ...   print x
   ... x += 1