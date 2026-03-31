import os 
import time
import tkinter as tk

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
    

def insertar (ele, arb):
    #print (ele, arb)
    if arb == []:
        return ele
    elif ele <= raiz(arb):
        return arbol(raiz(arb), insertar(ele, hijoizq(arb)),
                      hijoder(arb))
    else:
        return arbol (raiz(arb), hijoizq(arb), insertar(ele,hijoder(arb)))

def insertar_hijo_izq (ele, arb):
    #print (ele, arb)
    if arb == []:
        return ele
    else:
        return arbol(raiz(arb), insertar(ele, hijoizq(arb)),hijoder(arb))

def insertar_hijo_der (ele, arb):
    #print (ele, arb)
    if arb == []:
        return ele   
    else:
        return arbol (raiz(arb), hijoizq(arb), insertar(ele,hijoder(arb)))

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
    print("Digite 14 para salir del programa\n")
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
        hijo = input("Ingrese el hijo:")
        arbol1 = insertar_hijo_izq(hijo,arbol1)
        print(arbol1)
        input("Presiona Enter para continuar...")
        #time.sleep(2.5)
        os.system('clear')
        main(arbol1)

    elif select == 3:
        os.system('clear')
        print("\nInsertar Hijo Derecho")
        hijo = input("Ingrese el hijo:")
        arbol1 = insertar_hijo_der(hijo,arbol1)
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

    else:
        return""   #fin del programa

arbol1 = []
main(arbol1)

# a = arbol(8,4,[12,9,15])
# a = insertar(2,a)
# a = insertar(10,a)
# b = crear_raiz(50)
# b = insertar(2,b)
# b = insertar(60,b)
# b = insertar(62,b)
# print (b) 
