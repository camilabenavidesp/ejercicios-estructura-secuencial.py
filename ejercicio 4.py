# Calcular el área total de un terreno en metros sabiendo que esta fue reducida en un 10%,
# y posteriormente, le fue adicionado un 50% con relación al área después de la reducción

Area_Inicial=int(input("Ingrese la cntidad del area inicial: "))
Area_Reduccion=Area_Inicial*-0.10
Area_Total=Area_Reduccion*+0.50
print(f"El Area total es de {Area_Total} metro.")