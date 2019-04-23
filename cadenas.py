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
