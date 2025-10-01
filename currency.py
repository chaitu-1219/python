pesos = float(input("What do you have left in pesos? "))
soles = float(input("What do you have left in soles? "))
reais = float(input("What do you have left in reais? "))
usd_pesos = pesos * 0.00026   
usd_soles = soles * 0.29
usd_reais = reais * 0.19   
total_usd = usd_pesos + usd_soles + usd_reais
print(round(total_usd, 1))
