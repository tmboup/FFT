
####################################################################################################
####################################################   Fenix  #########################################
############################################ god's computer science #####################################
##########################################################################################################


from tkinter import *
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageTk,Image
from scipy import fftpack,signal
import math,re

windows = Tk()
windows.title("Fast Fourier Transform")
windows.geometry("1300x700")
windows.config(background="#15A2A2")
windows.resizable(0,0)   
    
    
#####################################################################################
####################### Cette partie gere les fonctions #########################
###################################################################################
    
def graphe2(x,sr):
    X=FFT(x)
    # calculate the frequency
    N = len(X)
    n = np.arange(N)
    T = N/sr
    freq = n/T 

    plt.figure(figsize = (12, 6))
    plt.subplot(121)
    plt.stem(freq, abs(X),'b',markerfmt=" ",basefmt="-b")
    plt.xlabel('Frequence en Hz')
    plt.ylabel('Amplitude FFT |X(freq)|')
    
    filtered_signal = fftpack.ifft(X)
    plt.figure(figsize=(12,6))
    #new = signal.detrend(filtered_signal) #permet d'eliminer toute tendance lineaire
    plt.plot(n,filtered_signal)
    plt.show()

    

def wN(n,k,N):
    #cette fonctin definie l'expression de wn
    return np.exp((-2j*np.pi*n*k)/N)

def DFT(x):
    x = np.asarray(x, dtype=float)
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = wN(n,k,N)
    #print(f"n = {n} et k = {k} ")
    #print(np.dot(M,x))
    return np.dot(M, x)



def FFT(x):
    """A recursive implementation of the 1D Cooley-Tukey FFT"""
    x = np.asarray(x, dtype=float)
    N = x.shape[0]
    
    if N % 2 > 0:
        raise ValueError("size of x must be a power of 2")
    elif N <= 32:  # this cutoff should be optimized
        return DFT(x)
    else:
        X_even = FFT(x[::2])
        X_odd = FFT(x[1::2])
        factor = np.exp(-2j * np.pi * np.arange(N) / N)
        return np.concatenate([X_even + factor[:int(N / 2)] * X_odd,X_even + factor[int(N / 2):] * X_odd])

def verif(N):
    VeriN = str(math.log(N)/math.log(2))
    print("la valeur est : ",VeriN)
    expression = "^[0-9]+(.0)$"
    return re.search(expression,VeriN)

def result():
    np.random.seed(0)
    N = int(varEntryN.get())
     
    #verifie si la valeur entree est une puissance de 2 ou n'est pas nulle 
    if((verif(N) is None) or (varEntryN.get())==0):
        messagebox.showwarning("error","La valeur entree doit etre une puissance de 2")
        varEntryN.set('')
        valeurEntry.delete(0,END)
        varListe.set('')
        
    else :
        x = np.random.random(N)
        valeurEntry.delete(0,END)
        valeurEntry.insert(0,x)
        count =0

        #print("voici les donnees : ",x)
        listeResult = []
        for line in FFT(x):
            listeResult.append(f"X({count}) = "+str(line)[1:-1]+"\n")
            count +=1 

        varListe.set(listeResult)
        graphe2(x,128)


def fCancel():
    varEntryN.set('')
    valeurEntry.delete(0,END)
    varListe.set('')

##definition des gos frames:en bas,a droite et gauche
frameC=Frame(windows, bg="#15A2A2",relief=SUNKEN,bd=3)
#frameC.pack(side=BOTTOM,padx=10,pady=20)
frameA=Frame(windows, bg="#15A2A2",relief=SUNKEN,bd=3)
frameA.pack(padx=10,pady=20)
frameB=Frame(windows, bg="#15A2A2",relief=SUNKEN,bd=3)
#frameB.pack(side=LEFT,padx=10,pady=20)



####################################################################################################
########################################## Partie Droite ###########################################
#####################################################################################################

#sous frame du frame de droite
frameA3=Frame(frameA, bg="#15A2A2",relief=SUNKEN,bd=1)
frameA3.pack(side=TOP,padx=20,pady=25)
frameA2=Frame(frameA, bg="#15A2A2",relief=SUNKEN,bd=1)
frameA2.pack(side=BOTTOM,padx=20,pady=25)
frameA0=Frame(frameA, bg="#15A2A2",relief=SUNKEN,bd=1)
frameA0.pack(side=RIGHT,padx=20,pady=25)
frameA1=Frame(frameA, bg="#15A2A2",relief=SUNKEN,bd=1)
frameA1.pack(side=LEFT,padx=20,pady=25)



#Message de Bienvenue des frames general
welcomeLabel = Label(frameA3,bg="#15A2A2",fg="white",text="Fast Transform Fourier",font=("Courrier",20))
welcomeLabel.pack(padx=5,pady=5)


frame11=Frame(frameA1, bg="#15A2A2",relief=SUNKEN,bd=1)
frame11.pack(side=TOP,padx=20,pady=20)
NLabel = Label(frame11,bg="#15A2A2",fg="white",text="valeur de N",font=("Courrier",20))
NLabel.pack(padx=5,pady=5)

varEntryN = IntVar()
N = Entry(frame11,bg="white",fg="black",font=("Courrier",20),width=10,textvariable=varEntryN)
N.pack(padx=5,pady=5)

frame12=Frame(frameA1, bg="#15A2A2",relief=SUNKEN,bd=1)
frame12.pack(side=BOTTOM,padx=20,pady=20)
frame122=Frame(frame12, bg="#15A2A2",relief=SUNKEN,bd=1)
frame122.pack(side=TOP,padx=10,pady=20)
valeurLabel = Label(frame122,bg="#15A2A2",fg="white",text="valeur initiale",font=("Courrier",20))
valeurLabel.pack(side=LEFT,padx=5,pady=5)
var = IntVar()
R1 = Radiobutton(frame122, text="Generer", variable=var, value=1,bg="#15A2A2")
R1.pack(side=RIGHT,padx=5,pady=5)
R2 = Radiobutton(frame122, text="Entrer ", variable=var, value=2,bg="#15A2A2",highlightcolor="red") #command=sel)
R2.pack(side=RIGHT,padx=5,pady=5)

valeurEntry = Entry(frame12,bg="white",fg="black",font=("Courrier",20),width=30)  #,state=DISABLED)
valeurEntry.pack(padx=5,pady=5)

varState = StringVar
infLabel = Label(frameA0,bg="#15A2A2",fg="white",text="Resultat transforme de fourier",font=("Courrier",10),textvariable=varState)
infLabel.pack(side=TOP,padx=5,pady=5)

#cette partie presente certains problemes 
scrollbar = Scrollbar(frameA0,bg="#15A2A2",width=20,highlightcolor="yellow")
scrollbar.pack(side = LEFT, fill = Y )
varListe = StringVar()
mylist = Listbox(frameA0, yscrollcommand=scrollbar.set,bg="white",height=9,width=40,font=("courier",20),listvariable=varListe)   #,activestyle='dotbox')

mylist.pack(side=LEFT,fill=BOTH)
scrollbar.config(command = mylist.yview)

boutonValide = Button(frameA2,text="Calculer",height=3,width=10,bg="#15A2A2",bd=5,fg="white",font=("Helvetiva",10),command=result)
boutonValide.pack(side=LEFT,padx=5,pady=5)
boutonCancel = Button(frameA2,text="Reinitialiser",height=3,width=10,bg="#15A2A2",bd=5,fg="white",font=("Helvetiva",10),command=fCancel)
boutonCancel.pack(side=LEFT,padx=5,pady=5)





####################################################################################################
########################################## Partie Gauche ###########################################
#####################################################################################################

#sous frame du frame a gauche
frameB3=Frame(frameB, bg="#15A2A2",relief=SUNKEN,bd=3)
frameB3.pack(side=TOP,padx=20,pady=25)

frameB2=Frame(frameB, bg="#15A2A2",relief=SUNKEN,bd=3)
frameB2.pack(side=BOTTOM,padx=20,pady=25)
frameB0=Frame(frameB, bg="#15A2A2",relief=SUNKEN,bd=3)
frameB0.pack(side=RIGHT,padx=20,pady=25)
frameB1=Frame(frameB, bg="#15A2A2",relief=SUNKEN,bd=3)
frameB1.pack(side=LEFT,padx=20,pady=25)

welcomeLabel = Label(frameB3,bg="#15A2A2",fg="white",text="Transforme de Fourier Discret Inverse",font=("Courrier",20))
welcomeLabel.pack(padx=5,pady=5)




infLabel = Label(frameB0,bg="#15A2A2",fg="white",text="Resultat transforme de fourier",font=("Courrier",10))
infLabel.pack(side=TOP,padx=5,pady=5)
scrollbar = Scrollbar(frameB0,bg="#15A2A2",width=20,highlightcolor="yellow")
scrollbar.pack(side = LEFT, fill = Y )
mylist = Listbox(frameB0, yscrollcommand=scrollbar.set,bg="white",height=10,font=("courier",20))

for line in range(50):
   mylist.insert(END, "line number " + str(line))

mylist.pack(side=LEFT,fill=BOTH)
scrollbar.config(command = mylist.yview)


boutonValide2 = Button(frameB2,text="Calculer",height=3,width=10,bg="#15A2A2",bd=5,fg="white",font=("Helvetiva",10))
boutonValide2.pack(side=LEFT,padx=5,pady=5)
boutonCancel2 = Button(frameB2,text="Reinitialiser",height=3,width=10,bg="#15A2A2",bd=5,fg="white",font=("Helvetiva",10))
boutonCancel2.pack(side=LEFT,padx=5,pady=5)


####################################################################################################
################################## Partie Gauche termine ###########################################
#####################################################################################################



windows.mainloop()