def busquedaBinaria(unaLista, item):
	   primero = 0
     ultimo = len(unaLista)-1
     encontrado = False
     while primero<=ultimo and not encontrado:
         puntoMedio = (primero + ultimo)//2
         if unaLista[puntoMedio] == item:
            encontrado = True
         else:
             if item < unaLista[puntoMedio]:
                ultimo = puntoMedio-1
             else:
	                primero = puntoMedio+1

	    return encontrado

#Otro
def busqueda_binaria(lista, x):
    izq = 0 
    der = len(lista) -1 
    while izq <= der:
        medio = (izq+der)/2
        if lista[medio] == x:
            return medio

        elif lista[medio] > x:
            der = medio-1        
        else:
            izq = medio+1
    return -1
