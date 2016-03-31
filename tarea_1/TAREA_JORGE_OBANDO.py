from Tkinter import*
import string
import sys

#****DECLARACION DE FUNCIONES
#ESTA SERA MI FUNCION DE INCRIPTACION CENIT!

def cenit_polar(palabra):
    
    p = "polarPOLAR"    #primera comparacion
    c = "cenitCENIT"    #segunda comparacion(string)
         
    lista = list(palabra)
    listaf = list()      #my_lista=[]

    for letra in lista:
        try:
            listaf.append(p[c.index(letra)])
        except:
            try:
                listaf.append(c[p.index(letra)])
            except:
                listaf.append(letra)
    estasi="".join(listaf)
    #return "".join(listaf)
    exitt.insert(INSERT,estasi+"\n")

#ESTA SERA MI FUNCION DE INCRIPTACION CESAR!
def encrypt(palabra,recu): 

    p = palabra
    n = int(recu)  # se pasa a entero
    au = string.ascii_lowercase 
    palabrita = ""  #palabra final
    #si la palabra hubiera sido mayuscula
    #am=string.ascii_uppercase
    
    for i in p:
        c = 0
        if i == " ":
            palabrita = palabrita + " "
        for j in au:
            if i == j:
                if c + n <26:
                    palabrita = palabrita + (au[c+n])
                else:
                    auxi = (c+n) - 25
                    palabrita = palabrita + (au[25-auxi])
            c = c + 1

    #return palabrita                
    exitt.insert(INSERT, palabrita +"\n")
#***



def selec():
    if valor.get() == 1:
        cenit_polar(entrada.get())
    elif valor.get() == 2:
        encrypt(entrada.get(),entrada2.get())

def activar():
    entrada2.configure(state=NORMAL)
    entrada2.update()
    

        
ventana = Tk()
#ventprin=Toplevel(ventana)

ventana.title("Encriptador")
ventana.geometry("400x490") #Dimencion
ventana.config(bg="orange") #color

valor = IntVar() 

#frame
frame = Frame(ventana)  
frame.pack()
frame.config(bg="orange")

bottomframe = Frame(ventana)
bottomframe.pack(side=BOTTOM)
bottomframe.config(bg="orange")

label1 = Label(frame, text="Ingresa palabra o frase ah encriptar:")
label1.pack()
label1.config(padx=50)#funciono!!
label1.config(bg="orange",bd=3)#borde y color

#entrada texto encriptar
entrada = Entry(frame,width=40)
entrada.pack()
entrada.config(bg="White",relief=GROOVE,bd=3)#blancoo!
#fin

label2 = Label(frame, text="Selecciona encriptacion!:")
label2.pack()
label2.config(bg="orange")


#***botones seleccionar
botoncesar = Radiobutton(frame,text="Cesar", variable=valor, value=2, command=activar)
botoncesar.pack(side=LEFT)
botoncesar.config(bg="orange")

botoncepol = Radiobutton(frame,text="Cenit Polar", variable=valor, value=1)
botoncepol.pack(side=RIGHT)
botoncepol.config(bg="orange")
#fin

label3 = Label(bottomframe, text="Lecciona numero de salto:")
label3.pack()
label3.config(bg="orange")

#entrada de numero saltos
entrada2 = Entry(bottomframe,width=10, state=DISABLED,bg="Light Goldenrod")
entrada2.pack()

#configurar boton encriptar
botonencrypt = Button(bottomframe, text="Encriptar*",command=selec)
botonencrypt.pack()
botonencrypt.config(width=30)
botonencrypt.config(relief=GROOVE,bd=6)
#botonencrypt.grid(row=4, column=3)


exitt = Text(bottomframe)
exitt.pack(side=BOTTOM)

#ventprin.withdraw()
ventana.mainloop()






