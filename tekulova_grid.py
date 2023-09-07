#nacitanie obsahu txt suboru do listu stringov
def txt_to_array ():
    f = "matrix.txt"
    #array pre matricu
    m = []
    with open(f, 'r') as file:
        cisla = file.readlines()
    # ide po každom riadku a meni to na int a ked pride ku koncu tak to uloží na koniec 
    for riadok in cisla:
        #rozdeluje riadky
        riadok1 = [int(num) for num in riadok.split()]
        m.append(riadok1)
    return m
m=txt_to_array()

def find_four ():
    #definovanie 4 polí pre nájdenie všetkých štvoríc
    sucin_r=[]
    sucin_s=[]
    sucin_d=[]
    sucin_d2=[]

    #kontrola na riadky
    for i in range (20):
        for j in range (20-3):
            #sucin 4 susednych
            riadky=(m[i][j]*m[i][j+1]*m[i][j+2]*m[i][j+3])
            #zapisovanie každej 4-ice na koniec
            sucin_r.append(riadky)

    #kontrola na stlpce
    for i in range (20-3):
        for j in range (20):
            #sucin 4 susednych
            stlpce=(m[i][j]*m[i+1][j]*m[i+2][j]*m[i+3][j])
            sucin_s.append(stlpce)

    #kontrola na diagonaly prva polka (zlava do prava)
    for i in range (20-3):
        for j in range (20-3):
            #sucin 4 susednych
            diagonaly=(m[i][j]*m[i+1][j+1]*m[i+2][j+2]*m[i+3][j+3])
            sucin_d.append(diagonaly)

    #kontrola na diagonaly druha polka (zprava dolava)
    for i in range (20-3):
        for j in range (3,20):
            #sucin 4 susednych
            diagonaly2=(m[i][j]*m[i+1][j-1]*m[i+2][j-2]*m[i+3][j-3])
            sucin_d2.append(diagonaly2)
    #spojenie všetkých polí do jedného veľkého
    all = sucin_r
    all.extend(sucin_s)
    all.extend(sucin_d)
    all.extend(sucin_d2)
    return all

all=find_four()
maximum =0
#funkcia na zistenie najväčšieho prvku zo všetkých štvoríc
for cislo in all:
    if cislo > maximum:
        maximum = cislo

print(f"Najväčší súčin zo všetkých štvoríc je {maximum}.")

      
      

