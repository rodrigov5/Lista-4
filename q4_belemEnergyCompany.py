gearNwatts = {
    'ar-condicionado': 1600,
    'computador': 350,
    'chuveiro': 5000,
    'ferro': 1000,
    'lampada': 32,
    'lavadora-roupas': 600,
    'refrigerador': 350,
    'tv': 200
}

flagNCost_KWH = {
    'verde': 0.50,
    'amarela': 0.53,
    'vermelha': 0.56
}

gearUse = {}

def flag(flags):
    if flags == 'verde':
        return flagNCost_KWH[flags]
    elif flags == 'amarela':
        return flagNCost_KWH[flags]
    elif flags == 'vermelha':
        return flagNCost_KWH[flags]

def final(gear, flags, icmsValue):
    final = (gearUse[gear] * flag(flags)) + (icmsValue / 100)
    return final


flags = input('Bandeira Utilizada no Mês (Verde, Amarela, Vermelha): ')
icmsValue = float(input('Valor do ICMS cobrado em porcentagem: '))
qtd_gear = int(input('Quantidade de equipamentos usados: '))

tot = 0
for i in range(qtd_gear):
    gear_data = input('Equipamento usado e tempo de uso em horas: ').split()
    gearUse[gear_data[0]] = ((float(gear_data[1]) * gearNwatts[gear_data[0]])) / 1000
    tot =+ tot + final(gear_data[0], flags, icmsValue)

print(f'Valor estimado da conta de energia = {tot}')


