#Demana quants números volem introduir. A continuació, demana’ls per teclat.Finalment, mostra el número major i el menor. 

introduits= int(input("Dis-me quants numeros vols introduir "))
cmajor=0
cmenor=0

for i in range (1, introduits+1):
    demanem= int(input("Dis-me uns quants numerets "))
    major=demanem
    menor=demanem
    if demanem>major:
        major=demanem
        cmajor+=1
    elif demanem<menor:
        menor = demanem
        cmenor+=1



print("El major es ",major," i el menor es ",menor," i tambe shan introudit el major ", cmajor,"voltes i menors ",cmenor)















