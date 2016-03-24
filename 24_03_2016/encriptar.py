from string import ascii_lowercase as al
from string import ascii_uppercase as au
def encrypt(p,j):
        return "".join(al[(al.index(i)+j)%len(al)] if i in al else au[(au.index(i)+j)%len(au)]if i in au else i for i in p)

if __name__=="__main__":
        
        x=raw_input("ingrese palabra a encriptar: ")
        y=int(input("ingrese numero de posiciones para correr: "))
        print("***la palabra se engripto ***")
        print encrypt (x,y)
	
       
        
