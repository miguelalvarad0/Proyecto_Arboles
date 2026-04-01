import os 
import time
import tkinter as tk
import json


def arbol (centro, hijoizquierdo, hijoderecho):
    if hijoizquierdo == [] and hijoderecho == []:
        return centro
    else:
        return [centro] + [hijoizquierdo] + [hijoderecho]

def atomo(x):
   
    return not type(x) == list

def raiz (arbol):
    if atomo(arbol):
        return arbol
    else:
        return arbol[0]

def hijoizq (arbol):
    if atomo(arbol):
        return []
    else:
        return arbol[1]

def hijoder (arbol):
    if atomo(arbol):
        return []
    else:
        return arbol[2]

def hoja(nodo):
    if nodo == []:
        return False
    elif atomo(nodo):
        return True #[10,[],[]]
    elif hijoizq(nodo) == [] and hijoder(nodo) == []:
        return True
    else:
        return False

def crear_raiz (centro):   
    return centro
    
def insertar_izq_en_nodo(a, objetivo, nuevo):
    nuevo_arbol, estado = insertar_izq_en_nodo_aux(a, objetivo, nuevo)
    
    if estado == "no_encontrado":
        print("Nodo no encontrado")
    elif estado == "ocupado":
        print("El nodo", objetivo, "ya tiene hijo izquierdo ocupado")
    
    return nuevo_arbol

def insertar_izq_en_nodo_aux(a, objetivo, nuevo):
    if a == []:
        return [], "no_encontrado"
    
    if raiz(a) == objetivo:
        if hijoizq(a) == []:
            return arbol(raiz(a), [nuevo, [], []], hijoder(a)), "insertado"
        else:
            return a, "ocupado"
    
    # Buscar izquierda
    nuevo_izq, estado = insertar_izq_en_nodo_aux(hijoizq(a), objetivo, nuevo)
    
    if estado != "no_encontrado":
        return arbol(raiz(a), nuevo_izq, hijoder(a)), estado
    
    # Buscar derecha
    nuevo_der, estado = insertar_izq_en_nodo_aux(hijoder(a), objetivo, nuevo)
    
    return arbol(raiz(a), hijoizq(a), nuevo_der), estado

def insertar_der_en_nodo(a, objetivo, nuevo):
    nuevo_arbol, estado = insertar_der_en_nodo_aux(a, objetivo, nuevo)
    
    if estado == "no_encontrado":
        print("Nodo no encontrado")
    elif estado == "ocupado":
        print("El nodo", objetivo, "ya tiene hijo derecho ocupado")
    
    return nuevo_arbol

def insertar_der_en_nodo_aux(a, objetivo, nuevo):
    if a == []:
        return [], "no_encontrado"
    
    if raiz(a) == objetivo:
        if hijoder(a) == []:
            return arbol(raiz(a), hijoizq(a), [nuevo, [], []]), "insertado"
        else:
            return a, "ocupado"
    
    # Buscar izquierda
    nuevo_izq, estado = insertar_der_en_nodo_aux(hijoizq(a), objetivo, nuevo)
    
    if estado != "no_encontrado":
        return arbol(raiz(a), nuevo_izq, hijoder(a)), estado
    
    # Buscar derecha
    nuevo_der, estado = insertar_der_en_nodo_aux(hijoder(a), objetivo, nuevo)
    
    return arbol(raiz(a), hijoizq(a), nuevo_der), estado

def buscar_ab(elemento, arb):
    if arb == []:
        return False
    elif elemento == raiz(arb):
        print(elemento)
        return True
    else:
        return buscar_ab(elemento, hijoizq(arb))  or  buscar_ab(elemento, hijoder(arb))

def in_orden(arb):
    if arb == []:
        return []
    else:
        return in_orden(hijoizq(arb)) + [raiz(arb)] + in_orden(hijoder(arb))

def pre_orden(arb):
    if arb == []:
        return[]
    else:
        return [raiz(arb)] + pre_orden(hijoizq(arb)) + pre_orden(hijoder(arb))

def pos_orden(arb):
    if arb == []:
        return[]
    else:
        return pre_orden(hijoizq(arb)) + pre_orden(hijoder(arb)) + [raiz(arb)]

def altura(arbol):
    if arbol == []:
        return 0
    else:
        return 1 + max(altura(hijoizq(arbol)), altura(hijoder(arbol)))
    
def imprimir_nivel(arbol, nivel):
    if arbol == []:
        return
    
    if nivel == 1:
        print(raiz(arbol), end=" ")
    else:
        imprimir_nivel(hijoizq(arbol), nivel - 1)
        imprimir_nivel(hijoder(arbol), nivel - 1)

def recorrido_por_niveles(arbol):
    h = altura(arbol)
    
    for i in range(1, h + 1):
        imprimir_nivel(arbol, i)

def contar_nodos (arbol):
    if arbol == []:
        return 0
    elif hoja(arbol):
        return 1
    #haga algo con la raiz y recursivamente con los hijos el mismo problema
    else:
        return 1 + contar_nodos (hijoizq(arbol)) + contar_nodos (hijoder(arbol))
    
def contar_hojas (arbol):
    if arbol == []:
        return 0
    elif hoja(arbol):
        return 1
    else:
        return contar_hojas (hijoizq(arbol)) + contar_hojas (hijoder(arbol))

def eliminar_hoja(ele, a):
    if a == []:
        return []
    
  
    if raiz(a) == ele:
        
      
        if hijoizq(a) == [] and hijoder(a) == []:
            return []
        
        print("No es posible eliminar:", ele, "(no es una hoja)")
        return a
    
    return arbol(
        raiz(a),
        eliminar_hoja(ele, hijoizq(a)),
        eliminar_hoja(ele, hijoder(a))
    )

def raiz_v2(a):
    return a if not isinstance(a, list) else a[0]

def izq(a):
    return [] if not isinstance(a, list) else a[1]

def der(a):
    return [] if not isinstance(a, list) else a[2]

def dibujar(canvas, a, x, y, dx):
    if a == []:
        return
    
    # nodo
    canvas.create_oval(x-15, y-15, x+15, y+15)
    canvas.create_text(x, y, text=str(raiz_v2(a)))
    
    # hijo izquierdo
    if izq(a) != []:
        canvas.create_line(x, y, x-dx, y+60)
        dibujar(canvas, izq(a), x-dx, y+60, dx//2)
    
    # hijo derecho
    if der(a) != []:
        canvas.create_line(x, y, x+dx, y+60)
        dibujar(canvas, der(a), x+dx, y+60, dx//2)

def guardar_archivo(file_path, arbol):
    with open(file_path, 'w') as archivo:
        json.dump(arbol, archivo)

def cargar_archivo(file_path):
    import json
    with open(file_path, 'r') as archivo:
        return json.load(archivo)

def buscar_nodo(a, objetivo):
    if a == []:
        return []
    
    if raiz(a) == objetivo:
        return a
    
    # buscar en izquierda
    res = buscar_nodo(hijoizq(a), objetivo)
    if res != []:
        return res
    
    # buscar en derecha
    return buscar_nodo(hijoder(a), objetivo)

def mostrar_hijos(a, objetivo):
    nodo = buscar_nodo(a, objetivo)
    
    if nodo == []:
        print("Nodo no encontrado")
        return
    
    izq = hijoizq(nodo)
    der = hijoder(nodo)
    
    print("Hijo izquierdo:", raiz(izq) if izq != [] else "None")
    print("Hijo derecho:", raiz(der) if der != [] else "None")

def buscar_padre(a, objetivo):
    if a == []:
        return None
    
    # Verificar si este nodo es el padre
    if (hijoizq(a) != [] and raiz(hijoizq(a)) == objetivo) or \
       (hijoder(a) != [] and raiz(hijoder(a)) == objetivo):
        return a
    
    # Buscar en subárbol izquierdo
    res = buscar_padre(hijoizq(a), objetivo)
    if res is not None:
        return res
    
    # Buscar en subárbol derecho
    return buscar_padre(hijoder(a), objetivo)

def mostrar_padre(a, objetivo):
    padre = buscar_padre(a, objetivo)
    
    if padre is None:
        return 0
    else:
        return raiz(padre)
        
def mayor_ab(arb):
    if arb == []:
        return float('-inf')
    
    return max(
        int(raiz(arb)),
        mayor_ab(hijoizq(arb)),
        mayor_ab(hijoder(arb))
    )

def menor_ab(arb):
    if arb == []:
        return float('+inf')
    
    return min(
        int(raiz(arb)),
        menor_ab(hijoizq(arb)),
        menor_ab(hijoder(arb))
    )

def imprimir_menu(): #Imprime menu de opciones en pantalla.
    print("            ARBOL")
    print("Digite 1 para Crear Raiz")
    print("Digite 2 para Insertar Hijo Izquierdo")
    print("Digite 3 para Insertar Hijo Derecho")
    print("Digite 4 para Buscar un Numero")
    print("Digite 5 para Recorrer In orden")
    print("Digite 6 para Recorrer Pre orden")
    print("Digite 7 para Recorrer Pos orden") 
    print("Digite 8 para Recorrer Por Niveles")
    print("Digite 9 para Conocer la Cantidad de Nodos")
    print("Digite 10 para Conocer la Cantidad de Hojas") 
    print("Digite 11 para Conocer la altura del arbol")  
    print("Digite 12 para Eliminar una Hoja")
    print("Digite 13 para Ver el Arbol")
    print("Digite 14 para Guardar el Progreso")
    print("Digite 15 para Cargar el Arbol Guardado en Memoria") 
    print("Digite 16 para Mostrar una Generacion") 
    print("Digite 17 para Mostrar Hijos de una Persona") 
    print("Digite 18 para Mostrar el Padre de una Persona") 
    print("Digite 19 para Mostrar el Abuelo de una Persona") 
    print("Digite 20 para Mostrar el Mayor Nodo") 
    print("Digite 21 para Mostrar el Menor Nodo") 
    print("Digite 22 para salir del programa\n")

def main(arbol1): 
    imprimir_menu()
    select = int(input(" "))
    if select == 1:
        os.system('clear')  #limpia la terminal para imprimir desde cero en ella
        print("\nCrear Raiz")
        raiz = input("Ingrese la raiz:")
        arbol1 = crear_raiz(raiz)
        print(arbol1)
        input("Presiona Enter para continuar...")
        #time.sleep(2.5) #detiene la ejecucion del codigo por unos instantes 
        os.system('clear')
        main(arbol1)

    elif select == 2:
        os.system('clear')
        print("\nInsertar Hijo Izquierdo")
        nodo = input("A cual nodo quiere agregar un hijo:")
        hijo = input("Ingrese el hijo:")
        arbol1 = insertar_izq_en_nodo(arbol1,nodo,hijo)
        print(arbol1)
        input("Presiona Enter para continuar...")
        #time.sleep(2.5)
        os.system('clear')
        main(arbol1)

    elif select == 3:
        os.system('clear')
        print("\nInsertar Hijo Derecho")
        nodo = input("A cual nodo quiere agregar un hijo:")
        hijo = input("Ingrese el hijo:")
        arbol1 = insertar_der_en_nodo(arbol1,nodo,hijo)
        print(arbol1)
        input("Presiona Enter para continuar...")
        #time.sleep(2.5)
        os.system('clear')
        main(arbol1)

    elif select == 4:
        os.system('clear')
        print("\nBuscar numero")
        elemento = input("Ingrese el numero:")
        print(buscar_ab(elemento,arbol1))
        input("Presiona Enter para continuar...")
        #time.sleep(2.5)
        os.system('clear')
        main(arbol1)

    elif select == 5:
        os.system('clear')
        print("\nRecorrer In Orden")
        print(in_orden(arbol1))
        input("Presiona Enter para continuar...")
        #time.sleep(2.5)
        os.system('clear')
        main(arbol1)

    elif select == 6:
        os.system('clear')
        print("\nRecorrer Pre Orden")
        print(pre_orden(arbol1))
        input("Presiona Enter para continuar...")
        #time.sleep(2.5)
        os.system('clear')
        main(arbol1)

    elif select == 7:
        os.system('clear')
        print("\nRecorrer Pos Orden")
        print(pos_orden(arbol1))
        input("Presiona Enter para continuar...")
        #time.sleep(2.5)
        os.system('clear')
        main(arbol1)

    elif select == 8:
        os.system('clear')
        print("\nRecorrer Por Niveles")
        recorrido_por_niveles(arbol1)
        input("\nPresiona Enter para continuar...")
        #time.sleep(2.5)
        os.system('clear')
        main(arbol1)

    elif select == 9:
        os.system('clear')
        print("\nTotal de nodos")
        print(contar_nodos(arbol1))
        input("\nPresiona Enter para continuar...")
        #time.sleep(2.5)
        os.system('clear')
        main(arbol1)

    elif select == 10:
        os.system('clear')
        print("\nTotal de hojas")
        print(contar_hojas(arbol1))
        input("\nPresiona Enter para continuar...")
        #time.sleep(2.5)
        os.system('clear')
        main(arbol1)

    elif select == 11:
        os.system('clear')
        print("\nAltura del Arbol")
        print(altura(arbol1))
        input("\nPresiona Enter para continuar...")
        #time.sleep(2.5)
        os.system('clear')
        main(arbol1)

    elif select == 12:
        os.system('clear')
        print("\nEliminar Hoja")
        ele = input("Ingrese la hoja que desea eliminar:")
        arbol1 = eliminar_hoja(ele, arbol1)
        print(arbol1)
        input("\nPresiona Enter para continuar...")
        #time.sleep(2.5)
        os.system('clear')
        main(arbol1)

    elif select == 13:
        os.system('clear')
        print("\nMostrar Arbol")
        ventana = tk.Tk()
        canvas = tk.Canvas(ventana, width=600, height=400)
        canvas.pack()
        dibujar(canvas, arbol1, 300, 40, 120)
        ventana.after(4000, ventana.destroy)
        ventana.mainloop()
        input("\nPresiona Enter para continuar...")
        #time.sleep(2.5)
        os.system('clear')
        main(arbol1)

    elif select == 14:
        guardar_archivo("Arbol_Genealogico.txt",arbol1)
        os.system('clear')
        print("\nProgreso Guardado")
        input("\nPresiona Enter para continuar...")
        #time.sleep(2.5)
        os.system('clear')
        main(arbol1)
    
    elif select == 15:
        arbol1 = cargar_archivo("Arbol_Genealogico.txt")
        os.system('clear')
        print("\nArchivo en Memoria Recuperado!")
        input("\nPresiona Enter para continuar...")
        #time.sleep(2.5)
        os.system('clear')
        main(arbol1)

    elif select == 16:       
        os.system('clear')
        print("\nMostrar una Generacion")
        gen = input("Ingrese el numero de generacion que desea mostrar:")
        imprimir_nivel(arbol1,int(gen))
        input("\nPresiona Enter para continuar...")
        #time.sleep(2.5)
        os.system('clear')
        main(arbol1)

    elif select == 17:       
        os.system('clear')
        print("\nMostrar Hijos")
        objetivo = input("Mostrar hijos de:")
        mostrar_hijos(arbol1,objetivo)
        input("\nPresiona Enter para continuar...")
        #time.sleep(2.5)
        os.system('clear')
        main(arbol1)

    elif select == 18:       
        os.system('clear')
        print("\nMostrar Padre")
        objetivo = input("Mostrar Padre de:")
        x = mostrar_padre(arbol1,objetivo)
        if x == 0:
            print("No tiene padre (puede ser la raíz o no existe)")
        else:
            print("Padre:", x)

        input("\nPresiona Enter para continuar...")
        #time.sleep(2.5)
        os.system('clear')
        main(arbol1)

    elif select == 19:       
        os.system('clear')
        print("\nMostrar Abuelo")
        objetivo = input("Mostrar Abuelo de:")
        x = mostrar_padre(arbol1,mostrar_padre(arbol1,objetivo))
        if x == 0:
            print("No tiene abuelo o la persona no existe")
        else:
            print("Abuelo:", x)
        input("\nPresiona Enter para continuar...")
        #time.sleep(2.5)
        os.system('clear')
        main(arbol1)

    elif select == 20:       
        os.system('clear')
        print("\nMostrar Nodo Mayor")
        x = mayor_ab(arbol1)
        if x < -1000000000000 :
            print("Arbol vacio.")
        else:
            print(x)

        input("\nPresiona Enter para continuar...")
        #time.sleep(2.5)
        os.system('clear')
        main(arbol1)

    elif select == 21:       
        os.system('clear')
        print("\nMostrar Nodo Menor")
        x = menor_ab(arbol1)
        if x > 1000000000000 :
            print("Arbol vacio.")
        else:
            print(x)
        input("\nPresiona Enter para continuar...")
        #time.sleep(2.5)
        os.system('clear')
        main(arbol1)

    else:
        return""   #fin del programa

arbol1 = []
main(arbol1)
