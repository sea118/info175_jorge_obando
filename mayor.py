def mayor(x, y):
    if x < y:
      print ("El mayor es ",y)
      print ("El menor es ",x)
    elif  x > y:
      print ("El mayor es ",x)
      print ("El menor es ",y)
    else:

        print ("Son iguales ")
    
if __name__== "__main__":
    a = int(input("ingrese un numero: "))
    b = int(input("ingrese un numero: "))

mayor(a, b)
