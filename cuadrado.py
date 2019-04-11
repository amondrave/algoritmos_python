#!/usr/bin/env python
# -*- coding: utf-8 -*-
def cuadradoMagico(vector,n):
   magico=None
   x= sumaDiago(vector,n)
   y=sumaDiagoSecun(vector,n)
   z=suma(vector,n)//n
   if(x==y):
     if(x==z):
       magico=True
   else:
      magico=False
   return magico


def sumaDiago(matriz,n):
   suma = 0
   for i in range(n):
     for j in range(n):
       if(i==j):
         suma = suma + matriz[i][j]
   return suma

def sumaDiagoSecun(matriz,n):
   suma=0
   for i in range(n):
     for j in range(n):
        if(i+j==n-1):
          suma = suma + matriz[i][j]
   return suma


def suma(matriz,n):
  sumaMa = 0
  for i in range(n):
     for j in range(n):
       sumaMa = sumaMa+matriz[i][j]
  return sumaMa


n = int(input('Digite el tamaño de la matriz: '))
vector = []
for f in range(n):
   vector.append([0]*n)

for i in range(n):
  for j in range(n):
    vector[i][j] = int(input('Digite: '))


rta = cuadradoMagico(vector,n)
if(rta==True):
  print("Es magico")
else:
  print("No es magico")
