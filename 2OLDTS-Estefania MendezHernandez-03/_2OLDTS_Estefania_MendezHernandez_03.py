###Enabezado de script 
numero_global=3
arreglo_numero=[0]*numero_global
###[0][0][0][0][0][0][0][0]


### funciones secundarias 
def sumatoria(numero_local):
    resultado_sumatoria=0
    resultado_sumatoria_2=0
    for i in range(numero_local):
        arreglo_numero[i]=int(input("ingrese el valor de la posicion del arreglo:\n"))
        resultado_sumatoria=resultado_sumatoria+arreglo_numero[i]
        resultado_sumatoria=arreglo_numero[i]
        return resultado_sumatoria

### funcion principal 
def main():
    resultado_main=0
    resultado_main_2=0
    print("actividad 03 - sumatoria acumulativa - espacio de memoria estaticon:\n")
    resultado_main=sumatoria(numero_global)
    print ("el resultado de la sumatoria es igual : ", resultado_main)

if __name__=="__main__":
    main()
    

