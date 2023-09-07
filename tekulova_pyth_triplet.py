def pyth_find ():
    b=1
    podmienky=False
    #loop na prechádzanie čísiel od 1 po b, ktoré sa každý cyklus zväčší až pokým podmienky nie su true
    while (podmienky==False):
        #for cyklus na prejdenie všetkých dvojíc
        for a in range (1,b,1) :  
            #c je domocnina z a^2+b^2  
            c=int((a*a+b*b)**(1/2))
            left=(a*a)+(b*b)
            right=(c*c)
            sucet=(a+b+c)
            #podmienka 1 
            if sucet == 1000:
                #podmienka 2 - overenie, či a**2 +b**2=c**2
                if left==right:
                    sucin=(a*b*c)
                    bb=b
                    podmienky=True
                    break               
        b=b+1
        
    return sucin,a,bb,c

sucin,a,b,c=pyth_find()          
print (f"Pythagorejská trojica, ktorú hľadáme je {a},{b},{c} a ich súčin je {sucin}.")





            
        
