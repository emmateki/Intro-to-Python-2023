#funkcia na zistenie vsetkych prvocisiel pomocou erastotenovho 
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
                
    return prime_list
print (70616204741131/103608299)


p_list =Erastotenove_sito(900000)
x=70616204741131
i=0

def prvocislo_detection(x):
    for i in range(2, round(x**(1/2))):
        if x % i != 0:  
            break; 

while True:
    print(p_list[i])
    while x % p_list[i] == 0:
        x=x/p_list[i]

    if prvocislo_detection(x): break
    
    i+=1
print (x)
