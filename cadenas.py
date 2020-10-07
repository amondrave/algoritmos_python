## @autor angel mondragon
## metodo de invertir cadenas
def invertir(palabra):
    invertida = ''
    for carac in range(len(palabra)-1,-1,-1):
        invertida= invertida + palabra[carac]
    return invertida
## metodo para saber si una cadena es palindrome
def palindrome(palabra):
     invertido = invertir(palabra)
     if(invertido==palabra):
         return True
     else:
         return False


x = 'tengo'
y = 'aaa'
z = 'tenet'
v = 'banana'

print(palindrome(x))
print(palindrome(y))
print(palindrome(z))
print(palindrome(v))

##Otro método para comparación de cadenas
f = open("asd.txt")

aux = ""

aux = f.readline()
aux = f.readline()

if aux == "asdf":
    print("Iguales")

print(aux)
#Sustituir
mensaje9 = "Hola Mundo"
startLoc = 2
endLoc = 8
mensaje9b = mensaje9[startLoc: endLoc]
print(mensaje9b)
-> la Mun
