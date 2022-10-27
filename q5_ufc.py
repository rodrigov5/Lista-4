
def categoryLimits():
    enter = input('Limite inferior e Limite superior: ').split()
    limInf = float(enter[0])
    limSup = float(enter[1])

    if limSup > limInf:
        return limSup
    else:
        print('Error, Limite inferior maior que limite superior!')
        

def checkIn(limSup, name):
    aux = limSup * 0.08

    value = fighters[name][0]

    if value <= round(aux + limSup):
        return 'Approved'
    else:
        return 'Reproved'

lim = categoryLimits()
fighters = {}

qtd_fighter = int(input('Digite a quantidade de lutadores que irão participar: '))
for i in range(qtd_fighter):
    enter = input('Nome e peso do lutador: ').split()
    fighters[enter[0]] = [float(enter[1])]
    aux = checkIn(lim, enter[0])
    fighters[enter[0]].append(aux)

print(fighters)