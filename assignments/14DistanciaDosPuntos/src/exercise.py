import math
def main():
    #escribe tu código abajo de esta línea
    x1=int(input('x1= '))
    y1=int(input('y1= '))
    x2=int(input('x2= '))
    y2=int(input('y2= '))
    Distancia=math.sqrt(((x1-x2)**2)+((y1-y2)**2))
    DistanciaFormateada= "{:.2f}".format(Distancia)
    print('distancia= ' + str(DistanciaFormateada))

if __name__ == '__main__':
    main()
