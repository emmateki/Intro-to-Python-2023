"""Finding the sum of all multiples of 3 and 5 less than 1234."""
X=3
Y=5
Z=15
I=1
SUMY=0
SUMX=0
SUMZ=0
#cycle for counting multiples 5 to 1234-5
while Y<(1234-5):
    Y=5*I
    SUMY+=Y
    I+=1
#null of I
I=1
# cycle for counting multiples 3 to 1234-3
while X<(1234-3):
    X=3*I
    SUMX+=X
    I+=1
I=1
# cycle for counting multiples 15 to 1234-15
while Z<(1234-15):
    Z=15*I
    SUMZ+=Z
    I+=1
#SUM of all sumx,y,z
SUM=SUMX+SUMY-SUMZ
print("The sum of multiples of 3 and 5 less than 1234 is:",SUM)
