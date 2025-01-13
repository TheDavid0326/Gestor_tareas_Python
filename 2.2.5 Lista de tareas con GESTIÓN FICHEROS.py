#Lista de tareas

import os

#"r+"" es leer y escribir


#print(txt_file.read())


#Menú de lista de tareas
orden= int(input('¿Qué deseas hacer, 1: Ver lista de tareas, 2:Añadir tarea, 3: Marcar tarea completada, 4:Eliminar tarea'))

if orden==1:
    txt_tareas=open("Python/Ejercicios/lista_tareas.txt", "r")
    for line in txt_tareas.readlines():
        print (line)

elif orden==2:
    txt_tareas=open("Python/Ejercicios/lista_tareas.txt", "a")
    nueva_tarea=input ('Dime qué tarea nueva quieres añadir')
    txt_tareas.write("\n"+nueva_tarea)

#txt_tareas=open("Python/Ejercicios/lista_tareas.txt", "r")
#print (txt_tareas.readlines[1])


elif orden==3:
    lista_tareas=[]
    
    #Imprimimos por pantalla la lista de tareas actual
    txt_tareas=open("Python/Ejercicios/lista_tareas.txt", "r")
    for line in txt_tareas.readlines():
        print (line)
        lista_tareas.append(line.strip())
    txt_tareas.close()

    #Pedimos a usuario qué tarea quiere borrar
    linea_tarea_completada= int(input('Dime qué tarea/línea está completada'))-1
    
    #Guardamos la tarea que vamos a marcar como completada porque la borraremos de la lista de tareas
    tarea_a_borrar= lista_tareas[linea_tarea_completada]
    lista_tareas.pop(linea_tarea_completada)

    #Añadimos la tarea a la lista de tareas completadas
    txt_tareas_completadas=open("Python/Ejercicios/lista_tareas_completadas.txt", "a")
    txt_tareas_completadas.write(tarea_a_borrar+"\n")
    txt_tareas_completadas.close()
    
    #Creamos un nuevo documento txt "lista_tareas" sin la tarea completada y reemplazamos la anterior
    txt_tareas=open("Python/Ejercicios/lista_tareas.txt", "w")
    for line in lista_tareas:
        txt_tareas.write(line+"\n")
    txt_tareas.close()

elif orden==4:
    lista_tareas=[]
    txt_tareas= open("Python/Ejercicios/lista_tareas.txt", "r")
    for line in txt_tareas.readlines():
        print(line)
        lista_tareas.append(line.strip())
    txt_tareas.close()

    #print(lista_tareas)

    
    linea_tarea_a_borrar=int(input('Dime qué tarea quieres eliminar'))-1
    
    #print(linea_tarea_a_borrar)

    lista_tareas.pop(linea_tarea_a_borrar)

    txt_tareas=open("Python/Ejercicios/lista_tareas.txt", "w")
    for line in lista_tareas:
        txt_tareas.write(line+"\n")
    
    txt_tareas.close()

