from random import randint
from time import sleep
from os import system
import colorama

def main(v):
    '''

    :param v:
    -versión 0: genera un dibujo con 2 carácteres random. No hace ninguna forma en específico.
    -versión 1: te pide una frase y la camufla en carácteres (40 es el número de carácteres por línea). Para que se vea, están en mayúsculas.
    '''
    while True:
        m = generar_matriz(40, v)
        sleep(2)
        system('cls')
        mostrar_matriz(m, v)

'''def generar_matriz(n):
    m = [[chr(randint(31,100000)) for x in range(n)] for x in range(n)]
    return m'''

def generar_matriz(n, v, hack = True):
    '''
    :param n: numero de caracteres por línea.
    :param v: versión.
    :param hack: cuando está activado, muestra en mayúsculas las palabras escondidas.
    :return: devuelve la matriz
    '''
    if v == 0:
        ch = randint(31,99999)
        m = [[chr(randint(ch, ch+1)) for x in range(n)] for x in range(n)]
    elif v == 1:
        width = 80
        m = ""
        if hack == True:
            frase = input('frase: ').upper().split()
        else:
            frase = input('frase: ').lower().split()
        for i in frase:
            if len(i) == 1:
                m += i
                for j in range(width):
                    if randint(0,1):
                        try:
                            m += chr(randint(97, 122-j)+j)
                        except:
                            m += chr(randint(97, 122))
                    else:
                        m += str(randint(0, 9))
            else:
                pos = randint(0, 32 - len(i))
                for j in range(width):
                    if j in range(pos, pos+len(i)):
                        m += i[j-pos]
                    else:
                        if randint(0, 1):
                            try:
                                m += chr(randint(97, 122 - j) + j)
                            except:
                                m += chr(randint(97, 122))
                        else:
                            m += str(randint(0, 9))
            m += '\n'
    return m



def mostrar_matriz(m, v):
    if v == 0:
        for a in m:
            for x in a:
                try:
                    print(x, end='')
                except:
                    print('x', end='')
            print()
    elif v == 1:
        print(m)

if __name__ == '__main__':
    main(0)
