import sympy as sy
import numpy as np
#matrix=([[4,-3,1,8,3],[2,5,3,-1,2]])#Para infinitas soluciones
#m=2;n=5
matrix=([[1,0,3,4,3,4],[0,1,3,-1,2,3],[0,0,1,-1,2,6]])#Para infinitas soluciones
m=3;n=6
#matrix=([[2,1,-1,-6],[3,0,1,-5],[4,2,-2,-1],[2,8,5,-7]])#sin solucion
#m=4;n=4
#matrix=([[2,1,-1,-6,3],[3,0,2,1,-5],[4,1,2,-2,-1],[2,8,-8,5,-7]])#con solucion
#m=4;n=5
#matrix=([[1,1,2],[2,1,3],[4,1,2]])#Sin solucion
#m=3;n=3
#matrix=([[-1,2,5],[3,1,7],[2,3,12]])#
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
#Ciclo para ver si la matriz tiene solucion infinita o no tiene solucion
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

if(t[0][n-2] !=0 and t[1][n-2] !=0):
    print("Tiene infinitas solucionessss")
elif(d==0):
    print("OK")
    d=3
#condicion para cuando tiene soluciones infinitas
if(d==0):
    if(n-m<2):
        last=[]#almacena los datos de la diagonal superior excepto los ceros
        sol=[]#almacena los datos de los resultados
        #ciclo para guardar los datos en last y sol
        for i in range(0,m):
             if(t[i][n-1]!=0):
                 sol.append(t[i][n-1])
                 for j in range(i+1,n-1):
                     if(t[i][j]!=0):
                         last.append(t[i][j])
        total=[]#almacena los resultados de las variables
        z=-float(input("Introduzca un valor para la variable: "))
        for i in range(0,len(last)):#ciclo para hacer la ecuacion 
            total.append(last[i]*z+sol[i])
        total.append(-z)
        #print(last)
        #print(sol)
        print("Para z = ",-z)
        print(total)
    elif(n-m==3):
        k=n-m-1;
        res=[]#va a guardar los numeros de las variables libres
        var=[]##va a guardar las varibles al momento de introducirlas
        sol=[]#va a guardar la ultima columna que son los resultados
        for i in range(0,m):
             if(t[i][n-1]!=0):
                 sol.append(t[i][n-1])
        for i in range(0,m):
            if(n%2==0):#condicion para cuando el numero de columnas es par
                for j  in range(n-2,k,-1):
                    res.append(t[i][j])
            else:
                for j  in range(n-2,k-1,-1):
                    res.append(t[i][j])
        
        total = []#Guarda los totales de las sumas
        cont=0#Para cambiar cuando llegue a dos por que cada dos estan los numeros
        pas=0#para saber la posicion del vector sol
        otro=1#para cambiar entre 0 y 1 para las dos variables
        sum=0#suma para luego guardar cada dos iteraciones
        for i in range(0,k):
            var.append(float(input("Introduzca un valor para la variable: ")))
        for j in range(0,len(res)):
            sum=res[j]*var[otro]+sum
            cont = cont + 1
            if(cont == 2):#cada dos iteraciones va ha guardar en total
                total.append(sum)
                sum=0
                cont = 0
            if(otro==1):#cambia para multiplicar por la respectiva variable
                otro=0
            else:
                otro=1
        finish=[]   
        for i in range(0,len(sol)):#ciclo para restar los valores de la solucion y el total de las variables libres
            finish.append(sol[i]-total[i])     
        for i in range(0,len(var)):#Ciclo para guardar las varibles que se metieron manualmente
            finish.append(var[i])
        print(finish)