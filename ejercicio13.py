#El terreno comprado por un influencers tuvo la siguiente destinación: 40% para cultivos,25% Para construir vivienda, 
#15% para zonas verdes. Leer el área total del terreno en
#metros cuadrados e imprimir el área para cada destino, y el área que queda disponible para otros proyectos.

Area_Total = float(input("Ingrese el area total del terreno: "))
Area_Cultivos = Area_Total * 0.40
Area_Vivienda = Area_Total * 0.25
Areas_Zonas_Verdes = Area_Total * 0.15

Area_Disponible = Area_Total - (Area_Cultivos + Area_Vivienda + Areas_Zonas_Verdes)

print(f"Area destinada a cultivos: {Area_Cultivos} metros cuadrados")
print(f"Area destinada a vivienda: {Area_Vivienda} metros cuadrados")
print(f"Area destinada a zonas verdes: {Areas_Zonas_Verdes} metros cuadrados")
print(f"Area disponible para otros proyectos: {Area_Disponible} metros cuadrados")
