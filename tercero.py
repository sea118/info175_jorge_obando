list=[]
lista = raw_input("Ingresa frase: ")
while (lista!=" "  ):
    list += [lista] 
    lista = raw_input("Ingresa frase: ")
    
print ("las frases ingresadas fueron: ")
print list
nueva_lista=' '.join(list)
print nueva_lista.upper()



