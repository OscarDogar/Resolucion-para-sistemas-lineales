import sympy as sy
import numpy as np
#matrix=([[4,-3,1,8],[2,5,3,-1]])#Para infinitas soluciones
#m=2;n=4
#matrix=([[2,1,-1,-6],[3,0,1,-5],[4,2,-2,-1],[2,8,5,-7]])#sin solucion
#m=4;n=4
matrix=([[2,1,-1,-6,3],[3,0,2,1,-5],[4,1,2,-2,-1],[2,8,-8,5,-7]])#con solucion
m=4;n=5
#matrix=([[-1,2,5],[3,1,7],[2,3,12]])#infinitas soluciones  y 0=0
#m=3;n=3
#matrix=([[1,0,3,-2],[0,1,2,1],[0,0,0,0]])#infinitas soluciones  y 0=0
#m=3;n=4
#matrix=([[2,1,-1,-6],[3,-1,1,-5],[4,2,-2,-1]])#Sin solucion
#m=3;n=4
#matrix=([[2,4,6,18],[4,5,6,24],[2,7,12,30]])#infinitas
#m=3;n=4

#Para llenar la matrix de forma manual
'''matrix=([[2,-3,1],[1,5,4],[3,4,2]])#Sin solucion
m=3;n=3
m=int(input('cantidad de filas:')) #filas
n=int(input('cantidad de columnas:')) #columnas
matrix = np.zeros((m,n)) 
q

print ('Ingrese la matriz de coeficientes')
for r in range(0,m):
    for c in range(0,n):
        matrix[(r),(c)]=float(input("Elemento a["+str(r+1)+str(c+1)+"] "))'''

M = sy.Matrix(matrix)
t =np.array(M.rref()[0])
print(t)
d=0
for i in range(0,m):
    for j in range(0,n):
        if(i==j):
            if(t[i][j]==0 and t[i][n-1]!=0):
                print("No tiene solucion")
                d=1
                break
            elif(t[i][j]==0 and t[i][n-1]==0):
                if(t[m-1][n-2]==0 and t[m-1][n-1]==0):
                    print("")
                else:
                    print("Tiene infinitas soluciones")
if(t[m-1][n-2]==0 and t[m-1][n-1]!=0 and d==0):
    print("No tiene solucion")
    d=1

if(n-m>2):
    print("Tiene infinitas soluciones y tiene mas de una variable")
if(t[0][n-2] !=0 and t[1][n-2] !=0):
    print("Tiene infinitas solucionessss")
elif(d==0):
    print("OK")
    d=3

if(d==0):
    last=[]
    sol=[]
    for i in range(0,m):
         if(t[i][n-1]!=0):
             sol.append(t[i][n-1])
             for j in range(i+1,n-1):
                 if(t[i][j]!=0):
                     last.append(t[i][j])
    total=[]
    print(last)
    z=-float(input("Introduzca un valor para la variable: "))
    for i in range(0,len(last)):
        total.append(last[i]*z+sol[i])
    total.append(-z)
    #print(last)
    #print(sol)
    print("Para z = ",z)
    print(total)