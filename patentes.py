LETRAS = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
NUMEROS = ['0','1','2','3','4','5','6','7','8','9']

class mostrarError(Exception):
    def __init__(self, mensaje):
        self.message = mensaje

def consultarPatente(valor):
    idConsulta = 0
    patenteConsulta = ''

    if type(valor) == int:
        idConsulta = valor
        if idConsulta < 1:
            raise mostrarError('El Id a consultar debe ser mayor a cero')
    elif type(valor) == str:
        patenteConsulta = valor
    else:
        raise mostrarError('El tipo de dato no corresponde')

    consultaxId = False
    consultaxPatente = False

    if idConsulta != 0:
        consultaxId = True
    elif len(patenteConsulta) > 0:
        consultaxPatente = True

    '''
    diccionario = {
        0: 'PATENTE'
    }
    '''

    try:
        # Para optimizar la consulta de la patente se generan 2 rangos

        # Se recorre la primera mitad, del primero al último
        if (consultaxId and (0 < idConsulta <= 228488000)) or (consultaxPatente and (patenteConsulta <= 'MZZZ999')):
            consecutivoId = 0
            for letra1 in LETRAS:
                for letra2 in LETRAS:
                    for letra3 in LETRAS:
                        for letra4 in LETRAS:
                            for numero1 in NUMEROS:
                                for numero2 in NUMEROS:
                                    for numero3 in NUMEROS:
                                        consecutivoId += 1
                                        # Almacenar en un diccionario los 456'976.000 de registros requeriría de muchos recursos
                                        '''
                                        diccionario[consecutivoId] = letra1 + letra2 + letra3 + letra4 + numero1 + numero2 + numero3
                                        '''
                                        if (consultaxId and consecutivoId == idConsulta):
                                            return letra1 + letra2 + letra3 + letra4 + numero1 + numero2 + numero3
                                        if (consultaxPatente and patenteConsulta == letra1+letra2+letra3+letra4+numero1+numero2+numero3):
                                            return consecutivoId
        # Se recorre la segunda mitad, del último al primero
        else:
            consecutivoId = 456976001
            for letra1 in reversed(LETRAS):
                for letra2 in reversed(LETRAS):
                    for letra3 in reversed(LETRAS):
                        for letra4 in reversed(LETRAS):
                            for numero1 in reversed(NUMEROS):
                                for numero2 in reversed(NUMEROS):
                                    for numero3 in reversed(NUMEROS):
                                        consecutivoId -= 1
                                        if (consultaxId and consecutivoId == idConsulta):
                                            return letra1 + letra2 + letra3 + letra4 + numero1 + numero2 + numero3
                                        if (consultaxPatente and patenteConsulta == letra1+letra2+letra3+letra4+numero1+numero2+numero3):
                                            return consecutivoId
    except Exception as e:
        print(f'Ocurrio un error al consultar la patente, Error: {e}')

if __name__ == '__main__':
    resultado = consultarPatente('AAAA000')
    print(resultado)