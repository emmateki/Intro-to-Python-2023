#funkcia na nájdenie palyndormu
def najdi_palyndrom ():
    nasobok_list=[]
    i_list=[]
    j_list=[]
    #najdu sa všetky možné kombinácie 4-ciferných čisiel od 1000 do 10000 s krokom 1
    for i in range (1000,10000,1):
        #ide po i aby sme zbytočne nerobili veľa iteracii
        for j in range (1000,i,1):
            cislo_string=str(i*j)
            #skúška čí číslo spredu a zozadu sa rovná-ak áno-palyndrom
            if cislo_string==cislo_string[::-1]:
                cislo=(i*j)
                nasobok_list.append(cislo)
                j_list.append(j)
                i_list.append(i)
                
    #funkcia na nájdenie najväčšieho prvku
    najvacsie=max(nasobok_list)
    #zistenie pozície našeho najväčšiho násobku
    pozicia = nasobok_list.index(max(nasobok_list))
    #nájdenie podľa pozície/indexu čísla i a j pre náš najvačší násobok
    k=j_list[pozicia]
    l=i_list[pozicia]
                
    return najvacsie, k, l

najvacsie, k, l =najdi_palyndrom()
print (f"Najväčší násobok dvoch 4-ciferných čísiel,ktorý je zároven aj palindrom:{najvacsie}. A je to násobok čísiel: {k} a {l}")