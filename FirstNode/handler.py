import json

def hello(event, context):
    numero = 20
    arbol_al_derecho = []
    arbol_al_reves = []
    tronco = []
    
    for i in range(1, numero + 1):
        fila = " " * (numero - i) + "*" * (2 * i - 1)
        arbol_al_derecho.append(fila)
    
    tronco_fila = " " * (numero - 2) + "***"
    for i in range(numero // 2):
        tronco.append(tronco_fila)
    
    for i in range(numero, 0, -1):
        fila = " " * (numero - i) + "*" * (2 * i - 1)
        arbol_al_reves.append(fila)

    response = {
        "statusCode": 200,
        "body": "\n".join(arbol_al_derecho + tronco + ["\n"] + tronco + arbol_al_reves)
    }

    return response
