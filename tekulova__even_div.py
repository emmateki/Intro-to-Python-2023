#funkcia na zistenie vsetkych prvocisiel pomocou erastotenovho sita
def Erastotenove_sito(x):
    #seznam kde sa budu ukladat nasobky prvocisiel
    noprime_list=[]
    #seznam kde sa budu ukaldat prvocisla do naseho cisla
    prime_list=[]
    #cyklus kde prechadzame prvky od 2 po x+1-kebyze je aj x prvocislo
    for i in range(2, x+1):
        if i not in noprime_list:
            prime_list.append(i)
            for j in range (i*i, x+1,i):
                noprime_list.append(j)
    #ked sa zavola funkcia tak toto je to co zavolame          
    return prime_list

#prime_list je p_list
p_list =Erastotenove_sito(30)
i=1
max_nasobok1=[]
q=1

#funkcia na pocitanie najmensieho spolocenho nasobku (berie vsetky prvocicla a hlada 
# vsetky ich nasobky do 30 a zoberie a ulozi najvacsie mozne)
def max_nasobok ():
    j = 0
    for i in range (0,10):
        h=1
        #cyklus ktory h;ada vsetky nasobky
        while h*p_list[j]<30:
            h*=p_list[j]
        #nasobky sa ukladaju do tohoto seznamu nakoniec
        max_nasobok1.append(h)
        j += 1      
    return max_nasobok1


m_list=max_nasobok()
#cyklus na vynasobenie vsetkych ziskanych cisiel
for i in range (0,10):
    q*=m_list[i]

print ("Najmenší spoločný násobok čísiel od 1-30 je :",q)



