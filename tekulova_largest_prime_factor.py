#funkcia na zistenie všetkých deliteľov daného čísla
def delitele (x):
    delitele_list=[]
    #do zoznamu deliteľov dáme aj dané číslo ak by zadané číslo bolo prvočíslo
    x_original=x
    i = 2
    #cyklus, ktorý ide do odmocniny z n lebo potom zvyšok sú rovnaké deliteôe
    while i * i <= x:
        #cyklus, ktorý nachádza delitele
        if x % i ==0:
        #celočíselné delenie
            x //= i
            delitele_list.append(x)     
        else:
            i+=1
    delitele_list.append(x_original)
    return delitele_list

delitele2_list=delitele(70616204741131)

#cyklus, ktorý kontroluje či je deliteľ prvočíslo alebo nie
for i in range (len(delitele2_list) ):
    cislo=delitele2_list[-i-1]
    print(i)
    #bool na to či je prvočíslo alebo nie
    je_prvocislo=True
    #delíme deliteľ číslami od 2 do daného čísla (bez daného čisla)- kontrolujeme zvysok
    for h in range (2,cislo):
        if delitele2_list[i]%h==0:
            je_prvocislo=False
            break
    #ak je deliteľ prvočíslo tak sa nám vypíše
    if je_prvocislo:
        print("Najväčší prvočíselný deliteľ čísla 70616204741131 je:{}".format(cislo))
        break


        

        
          
