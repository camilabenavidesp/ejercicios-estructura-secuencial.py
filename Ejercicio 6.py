#Hacer un algoritmo que permita determinar la cantidad de minutos a los que equivale una
#cantidad de horas ingresadas por el usuario.

#Solicictar el cliente que ingrese los numeros 
Minutos=int(input("Ingrese la cantidad de horas: "))

#calcular las horas y minutos restantes 
#division entera para obetenr las horas
Horas=Minutos//60 
#resto de la division para obtener los minutos restantes 
Minutos_restantes=Minutos % 60

#mostrar resultado
print(f"{Minutos} minutos es igual a {Horas} horas y {Minutos_restantes} minutos.")
