palabraSinVocal = ""

# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable userWord
userWord=input('Ingrrese una palabra: \n')
userWord = userWord.upper()

for letra in userWord:
    if(letra=='A'):
        continue
    elif(letra=='E'):
        continue
    elif(letra=='I'):
        continue
    elif(letra=='O'):
        continue
    elif(letra=='U'):
        continue
    else:
        palabraSinVocal+=letra
print(palabraSinVocal)


