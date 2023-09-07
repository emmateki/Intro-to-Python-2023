#funkce na vloženie vsetkych 13tic do listu 
def najdi_trinastice (cislo):
    y=13
    x=0
    trinsatice_list=[]
    #cyklus, ktorý vytvorí 13-tice a dá ich do spoločného listu-trinastice
    for x in range (0,len(cislo)):
        #funkcia ktora zoberie len string od x do y prvku
        cislo2=(cislo [x:y])
        y+=1
        trinsatice_list.append(cislo2)   
     
    return trinsatice_list 

#funkce na vyansobenie všetkých 13-tic a ich vloženie do listu vynasobene
def vynasob_trinsatice ():
    trinsatice_list=najdi_trinastice("7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450")
    vynasobene =[] 
    #cyklus ktory postupne prejde všetky prvky v našom liste
    for i in range (len(trinsatice_list)):
        #prevedenie string na int
        trinsatice_list [i]= int(trinsatice_list[i])
        cislo3=trinsatice_list[i]
        x1=1
        #cyklus ktorý zoberie modus daného čisla-vynásobí to číslo x1 a naše číslo 3 sa zmenší o //10 (delenie bezo zvyšku)
        while cislo3>=1:
            x=(cislo3%10)
            cislo3=cislo3//10
            x1*=x         
        #naše nájdené násobky sa uložia do čísla x1
        vynasobene.append(x1)
        
    return vynasobene

vynasobene=vynasob_trinsatice()
#hladanie najväčšieho čísla v liste
najvacsie=max(vynasobene)

print (f"Najväčší násobok 13-tich čísiel po sebe je :{najvacsie}")
