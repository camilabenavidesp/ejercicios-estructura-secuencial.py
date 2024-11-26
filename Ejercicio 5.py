#Hacer un algoritmo que permita determinar las horas a las que equivale una cantidad de
#minutos ingresados por el usuario.


#Solicictar el cliente que ingrese los numeros 
Horas=int(input("Ingrese la cantidad de horas: "))

#calcular las horas y minutos restantes 
#division entera para obetenr las horas
Minutos=Horas//60 
#resto de la division para obtener los minutos restantes 
Minutos_restantes=Minutos % 60

#mostrar resultado
print(f"{Horas} horas es igual a {Minutos} Minutos y {Minutos_restantes} minutos.")