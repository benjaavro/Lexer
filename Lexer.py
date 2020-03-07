from globalTypes import TokenType

with open('matrix.txt') as f:
    fil, col = [int(x) for x in next(f).split()]
    simbolos = next(f).split('|')
    M = [[int(x) for x in line.split()] for line in f]

mapa = {}
for i in range(len(simbolos)):
    for c in simbolos[i]:
        mapa[c]=i

#f = open('example.txt', 'r')
#programa = f.read() 		# lee todo el archivo a tokenizar
#programa += '$'             # agregamos $ para representar EOF
#progLong = len(programa)    # longitud del archivo
#estado = 0                  # estado inicial
#token = ''                  # token inicial
#posicion = 0                # Lleva la posicion en la que se encuentra

def globales(prog, pos, long):
    global programa
    global posicion
    global progLong
    programa = prog
    posicion = pos
    progLong = long

imprime = True

def getToken(imprime):
    global posicion
    global estado

    token = ''
    estado = 0

    while (posicion < progLong):
        c = programa[posicion]
        if (c != ' ' or c != '\n'):
            estado = M[estado][mapa[c]]

            # EOF
            if (estado == 100):
                print("Tipo: ", tipo, "Valor: ", token)
                return tipo, token

            ## COMMENTS
            if (estado == 3):
                token += c
                n2 = programa[posicion + 1]
                estAux2 = M[estado][mapa[n2]]

                if (estAux2 == 4):
                    posicion += 1
                    c = programa[posicion]
                    token += c
                    posicion += 1
                    c = programa[posicion]
                    token += c
                    estadoComment = 4

                    #FORMA EL TOKEN CON UN WHILE QUE VA SUMANDO CHARS WHILE estado != 7 (NO SE CIERRE EL COMENTARIO)
                    while(estadoComment != 7):
                        posicion += 1
                        c = programa[posicion]
                        token += c
                        estadoComment = M[estadoComment][mapa[c]]

                    tipo = getTokenType(7)
                    print("Tipo: ", tipo, "Valor: ", token)
                    posicion += 1
                    return tipo, token

                else:
                    tipo = getTokenType(estado)
                    posicion += 1
                    print("Tipo: ", tipo, "Valor: ", token)
                    return tipo, token


            ## ID, NUMS & DOUBLECHARS
            if (estado == 1 or estado == 2 or estado == 8 or estado == 9 or estado == 11 or estado == 13 or estado == 15):
                token += c
                n = programa[posicion + 1]
                posicion += 1
                estAux = M[estado][mapa[n]]

                if (estAux != estado):
                    if(token == "else"):
                        tipo = getTokenType(101)
                        print("Tipo: ", tipo, "Valor: ", token)
                        return tipo, token
                    elif (token == "if"):
                        tipo = getTokenType(102)
                        print("Tipo: ", tipo, "Valor: ", token)
                        return tipo, token
                    elif(token == "int"):
                        tipo = getTokenType(103)
                        print("Tipo: ", tipo, "Valor: ", token)
                        return tipo, token
                    elif (token == "return"):
                        tipo = getTokenType(104)
                        print("Tipo: ", tipo, "Valor: ", token)
                        return tipo, token
                    elif (token == "void"):
                        tipo = getTokenType(105)
                        print("Tipo: ", tipo, "Valor: ", token)
                        return tipo, token
                    elif (token == "while"):
                        tipo = getTokenType(106)
                        print("Tipo: ", tipo, "Valor: ", token)
                        return tipo, token
                    else:
                        tipo = getTokenType(estado)
                        print("Tipo: ", tipo, "Valor: ", token)
                        return tipo, token

            ## SINGLE CHARS
            else:
                if(c == ' ' or c == '\n'):
                    posicion += 1
                else:
                    if(estado != 3 or estado != 4 or estado != 5 or estado != 6 or estado != 7):
                        token = c
                        tipo = getTokenType(estado)
                        posicion += 1
                        print("Tipo: ", tipo, "Valor: ", token)
                        return tipo, token


def getTokenType(estado):
    global respuesta
    respuesta = TokenType(estado).name
    return respuesta


#while(posicion < progLong):
    #getToken(True)