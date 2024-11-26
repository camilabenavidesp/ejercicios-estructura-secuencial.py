#A un empleado le aplican una retención del 18% sobre su salario básico, y le entregan una
#Bonificación de 1.3% sobre el salario. Desarrolle un algoritmo que permita calcular e
#imprimir el salario neto y los valores de sus respectivos porcentajes.
salario=int(input("Digite el salario: "))
retencion=salario*0.18
#salarioRetencion=salario-retencion
bonificacion=salario*0.013
#salarioBonificacion=salario+bonificacion 
salarioNeto=(salario-retencion)+bonificacion
print("El salario neto es: ",salarioNeto)
print("El valor de la retencion es:",retencion)
print("el valor de la bonificacion es:",bonificacion)