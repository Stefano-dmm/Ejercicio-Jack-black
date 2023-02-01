import random

nums = [

'A',
'2',
'3',
'4',
'5',
'6',
'7',
'8',
'9',
'J',
'Q',
'K',
]

Carta = []
Carta_mano = []
carta_mano2 = []
cartapc = []
dame = []
resultado = []
resultado2 = []
j = []
q = []
k = []

dame = (input("paso o dame "))
Carta = (random.choice(nums))
Carta_mano.append (Carta)

while dame == ("dame"): 

    Carta = (random.choice(nums))
    Carta_mano.append (Carta)   
    print (Carta_mano)
    print (resultado)
    dame = (input("paso o dame "))

    if dame == ("paso"):

        if "J" in Carta_mano:
            j = Carta_mano.count('J')

            for j in range (j):
                resultado.append ("10")
                j = [] 

    if "Q" in Carta_mano:
        q = Carta_mano.count('Q')

        for q in range (q):
            resultado.append ("10")
            q = [] 
    else:
        0
    
    if "K" in Carta_mano:
        k = Carta_mano.count('K')

        for k in range (k):
            resultado.append ("10")
            k = [] 
    else:   
        0
    
    # generar una mano de cartas mallor a 16 menor a 23 de manera random
    # for 
    # cartapc =(random.choice(nums))

print (Carta_mano)

while "J" in Carta_mano or "Q" in Carta_mano or "K" in Carta_mano:

    if "J" in Carta_mano:
        Carta_mano.remove("J")

    if "Q" in Carta_mano:
        Carta_mano.remove("Q")

    if "K" in Carta_mano:
        Carta_mano.remove("K")

carta_mano2 = str(Carta_mano)
resultado2.append (carta_mano2) 
resultado2.append (resultado)
print(resultado2)
print('Cacartas de la pc son', cartapc)

sum22 = sum (resultado2)
print (sum22)


