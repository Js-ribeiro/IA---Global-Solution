
def ciclos ():
    import random as rd
    ciclos = [[], [], []]
    
    aux = 0 
    while aux < 3:
    
        dados_ciclo = {
            "temperatura": rd.randrange(10, 101, 10),
            "saude": rd.randrange(10, 101, 10),
            "armazenamento": rd.randrange(10, 101, 10),
            "estabilidade": rd.randrange(10, 101, 10),
            "janela_downlink": rd.randrange(10, 101, 10),
            "Identificacao": rd.randrange(10, 31, 10)
        }
    
        ciclos[aux].append(dados_ciclo)
        
        aux += 1
    return ciclos
        