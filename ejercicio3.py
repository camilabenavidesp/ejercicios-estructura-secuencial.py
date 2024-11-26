#El valor del desempleo en Ibagué aumentó en el primer trimestre un 9.5% y en el segundo
#trimestre cayó en un 1.5%. Calcular el valor del desempleo actual.

Desempleo_Inicial=int(input("Dijite la cantidad de desempleo: "))
Aumento_Desempleo=Desempleo_Inicial*+0.095
Disminucion_Desempleo=Aumento_Desempleo*-0.015
print(f"El desempleo actual es de {Disminucion_Desempleo} porciento.")