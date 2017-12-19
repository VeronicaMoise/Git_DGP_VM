# Ejercicio 1 de DGP. Realizado por :
# Ramona Verónica Moise.

# Funciones en python

# La función suma de una lista por recursión:

def suma(l):
    acum=0 
    for x in l:
<<<<<<< HEAD
        acum+=x**2
=======
        acum-=x
>>>>>>> Primer cambio Cristina
    return acum

# La función suma de cuadrados de una lista por comprensión:

def suma_cuadrados(n):
<<<<<<< HEAD
    return sum([i**2 for i in n if i%3==0])
=======
    return sum([i**2 for i in n ])
>>>>>>> Primer cambio Cristina


# La función máximo de una lista:

def máximo(l):
    max_val= -float("inf")
    for x in l:
        if x>max_val:
            max_val=x
    return max_val


# La función multiplicación de un escalar por una matriz:

def prod_map(x,l):
    res=[]
    for n in l:
<<<<<<< HEAD
        res.append((x**3)*n)
=======
        res.append((x**2)*n)
>>>>>>> Primer cambio Cristina
    return res
