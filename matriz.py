class restricciones(Exception):
    def __init__(self, mensaje):
        self.message = mensaje

def calcularMatriz(r,c,z,x,y):
    # Restricciones
    if (r <= 0) or (c <= 0):
        raise restricciones('Los valores de R y C deben ser mayores a cero')
    if (x < 0) or (y < 0):
        raise restricciones('Los valores de X y Y deben ser valores enteros positivos')
    if not(0 < z <= 1000000):
        raise restricciones('El valor de Z debe ser mayor a cero y menor o igual a 1000000')

    aux = []
    matriz = []
    for i in range(r):
        for j in range(c):
            if j == 0:
                aux.clear()
            if i == 0:
                aux.append(z)
            else:
                aux.append(z+i) # Se simplifica la expresión z+(i+1)-1 siendo (i+1) Rn, pero como las posiciones en la matriz inician en 0 se omite el +1-1
        matriz.append(aux.copy())
    #print(matriz)

    resultado = 0 
    for i in range(y+1):
        for j in range(x+1):
            resultado += matriz[i][j]
    return resultado

if __name__ == '__main__':
    resultado = calcularMatriz(4,3,2,1,2)
    print(resultado)