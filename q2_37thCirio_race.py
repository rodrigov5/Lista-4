runners = {}
runnersAvg = {}
bestLap = {}

qtd_runner = int(input('Quantidade de corredores: '))

def addNewRunner(name):
        print(name.capitalize())
        metrics = input(f'Tempo de cada volta: ').split(' ')
        convTime = [float(x) for x in metrics]
        runners[name] = convTime
        runnersAvg[name] = calcAvg(name)
        bestLap[name] =  getBestLap(name)


def calcAvg(name):
    value = runners[name]
    avg = sum(value) / len(value)
    return avg


def getBestLap(name):
    laps = runners[name]
    minpos = laps.index(min(laps))
    return minpos + 1
    
def rank():
    return 0
        


for i in range(qtd_runner):
    name = input(f'Nome do corredor: ')
    addNewRunner(name)
    
