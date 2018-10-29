#Todas as cartas que temos
lista_cartas = ["1P", "1C", "1O","1E", "2P", "2C", "2O", "2E", "3P", "3C", "3O", 
     "3E", "4P", "4C", "4O", "4E", "5P", "5C", "5O", "5E", "6P", "6C", "6O", 
     "6E", "7P", "7C", "7O", "7E", "8P", "8C", "8O", "8E", "9P", "9C", "9O", "9E", "DP", 
     "DC", "DO", "DE", "JP", "JC", "JO", "JE", "VP", "VC", "VO", "VE", "RP", "RC", "RO", "RE", 
     "1P", "1C", "1O", "1E", "2P", "2C", "2O", "2E", "3P", "3C", "3O", "3E", 
     "4P", "4C", "4O", "4E", "5P", "5C", "5O", "5E", "6P", "6C", "6O", "6E", "7P", "7C", 
     "7O", "7E", "8P", "8C", "8O", "8E", "9P", "9C", "9O", "9E", "DP", "DC", "DO", "DE", 
     "JP", "JC", "JO", "JE", "VP", "VC", "VO", "VE", "RP", "RC", "RO", "RE", "1P", "1C", 
     "1O", "1E", "2P", "2C", "2O", "2E", "3P", "3C", "3O", "3E", "4P", "4C", "4O", "4E", 
     "5P", "5C", "5O", "5E", "6P", "6C", "6O", "6E", "7P", "7C", "7O", "7E", "8P", "8C", 
     "8O", "8E", "9P", "9C", "9O", "9E", "DP", "DC", "DO", "DE", "JP", "JC", "JO", "JE", 
     "VP", "VC", "VO", "VE", "RP", "RC", "RO", "RE"]

#Cartas que constituem um baralho
cartas_baralho = ["1P", "1C", "1O", "1E", "2P", "2C", "2O", "2E", "3P", "3C", "3O", 
     "3E", "4P", "4C", "4O", "4E", "5P", "5C", "5O", "5E", "6P", "6C", "6O", 
     "6E", "7P", "7C", "7O", "7E", "8P", "8C", "8O", "8E", "9P", "9C", "9O", "9E", "DP", 
     "DC", "DO", "DE", "JP", "JC", "JO", "JE", "VP", "VC", "VO", "VE", "RP", "RC", "RO", "RE"]


print("Numero Total de Cartas:",len(lista_cartas))
print("Numero Total de cartas num deck:",len(cartas_baralho))

for carta in cartas_baralho:
    if carta in lista_cartas:
        del lista_cartas[lista_cartas.index(carta)]

print("Apos remover as cartas para formar um deck, sobram:" ,len(lista_cartas))
#Imprimir as cartas que sobram
cartas_finais = lista_cartas
print(cartas_finais)

for carta in cartas_baralho:
    if carta in lista_cartas:
        del lista_cartas[lista_cartas.index(carta)]

print("Apos remover as cartas para formar um deck, sobram:" ,len(lista_cartas))
#Imprimir as cartas que sobram
cartas_finais = lista_cartas
print(cartas_finais)

for carta in cartas_baralho:
    if carta in lista_cartas:
        del lista_cartas[lista_cartas.index(carta)]

print("Apos remover as cartas para formar um deck, sobram:" ,len(lista_cartas))
#Imprimir as cartas que sobram
cartas_finais = lista_cartas
print(cartas_finais)