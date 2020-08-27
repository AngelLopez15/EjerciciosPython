bloques = int(input("Ingrese el número de bloques:"))

contador=0
altura=0
contAux=0
aux=0
while(contador!=bloques):
    if(aux==contador):
        contAux+=1
        aux = aux + contAux
    contador+=1
    if(aux%contador==0):
        altura+=1
print('La altura de la piramide es', altura)     
              
    

