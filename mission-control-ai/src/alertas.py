from src.telemetria import *
import matplotlib.pyplot as plt
import time
def alertas():
    ambiente= "" 
    dados_ciclos = ciclos()
    lista_alertas = []
    
    ambiente = dados_ciclos[0][0]["Identificacao"]

    for i in range(3):
        dados = dados_ciclos[i][0]
        num_cilco = i + 1 
        
        
        if dados["temperatura"] > 80:
            lista_alertas.append(f"C{num_cilco} - Temperatura: {dados['temperatura']}°C | critica ")
            lista_alertas.append(f"Ajuste de contingência: Sistema de resfriamento térmico ativado.")
     
     
     
        if dados["saude"] < 30:
            lista_alertas.append(f"C{num_cilco} - A saude do dispositivo: {dados['saude']}% | critica ")
            lista_alertas.append(f"Ajuste de contingência: Modo de segurancao ativado.")



        # 3. Armazenamento
        if dados["armazenamento"] > 85:
            lista_alertas.append(f"C{num_cilco} - Armazenamento esta quase lotado : {dados['armazenamento']}% | critica ")
            lista_alertas.append(f"Ajuste de contingência:Limpando a memoria , descartando cache ")


        # 4. Estabilidade
        if dados["estabilidade"] < 50:
            lista_alertas.append(f"C{num_cilco} - Estamos com um problema grave de estabilidade : {dados['estabilidade']}% | critica ")
            lista_alertas.append(f"Ajuste de contingência: requilibrando a aeronave  ")


        # 5. Janela Downlink
        if dados["janela_downlink"] < 50:
            lista_alertas.append(f"C{num_cilco} - Estamos com um problema grave na comunicacao com o satelite  : {dados['janela_downlink']}% | critica ")
            lista_alertas.append(f"Ajuste de contingência: Preservando janela de downlink ")
        
        
        
        
    if ambiente == 10 :
            ambiente = "chuva"
    elif ambiente ==20 :
            ambiente = "Neve "
    elif ambiente == 30 :
            ambiente = "Sem previsao significativa"
            
    lista_alertas.append(f"Ambiente detectado: {ambiente}")    
        
            
            
    def graficos ():
        
        lista_temp = ["C1","C2","C3"]
        saude_y = [c1["saude"], c2["saude"], c3["saude"]]
        temp_y = [c1["temperatura"], c2["temperatura"], c3["temperatura"]]
        arm_y = [c1["armazenamento"], c2["armazenamento"], c3["armazenamento"]]
        est_y = [c1["estabilidade"], c2["estabilidade"], c3["estabilidade"]]
        down_y = [c1["janela_downlink"], c2["janela_downlink"], c3["janela_downlink"]]
        
        
        
        plt.plot(lista_temp, saude_y, color='darkred', linestyle='--', marker='o', label='Saude')
        plt.title("Desempenho da Saude")  
        plt.xlabel("Turnos(ciclos)")
        plt.ylabel("Graus / Valores")
        plt.grid(True)
        plt.legend()
        plt.show()
        
        
        plt.plot(lista_temp, temp_y, color='seagreen', linestyle='--', marker='o', label='Temperatura')
        plt.title("Desempenho da Temperatura")  
        plt.xlabel("Turnos(ciclos)")
        plt.ylabel("Graus / Valores")
        plt.grid(True)
        plt.legend()
        plt.show()
        
        
        plt.plot(lista_temp, arm_y, color='steelblue', linestyle='--', marker='o', label='Armazenamento')
        plt.title("Desempenho do armazenamento ")  
        plt.xlabel("Turnos(ciclos)")
        plt.ylabel("Graus / Valores")
        plt.grid(True)
        plt.legend()
        plt.show()
        
        plt.plot(lista_temp, est_y, color='chocolate', linestyle='--', marker='o', label='Estabilidade ')
        plt.title("Desempenho da estabilidade ")  
        plt.xlabel("Turnos(ciclos)")
        plt.ylabel("Graus / Valores")
        plt.grid(True)
        plt.legend()
        plt.show()
        
        
        plt.plot(lista_temp, down_y, color='red', linestyle='--', marker='o', label='janela downlink ')
        plt.title("Desempenho da janela  de downlink")  
        plt.xlabel("Turnos(ciclos)")
        plt.ylabel("Graus / Valores")
        plt.grid(True)
        plt.legend()
        plt.show()
        
     
            
    
        
    alertas_texto = " | ".join(lista_alertas) if lista_alertas else "Todos os Sistemas Estáveis"

    dados_ultimo = dados_ciclos[2][0]
    c1 = dados_ciclos[0][0]
    c2 = dados_ciclos[1][0]
    c3 = dados_ciclos[2][0]
    time.sleep(1)
    
    def teste  ():
        titulo = "Relatório de Dados obtidos em três Ciclos"
        print(titulo.upper().center(120))
        print("")
        print("")
        print("==="*50)
        print(f"C1 -temperatura:{c1['temperatura']}°C | saude do dispositivo: {c1['saude']}% | Armazenamento: {c1['armazenamento']}% | Estabilidade: {c1['estabilidade']}% | janela downlink:{c1['janela_downlink']} % ")
        print("==="*50)
        print(f"C2 -temperatura:{c2['temperatura']}°C | saude do dispositivo: {c2['saude']}% | Armazenamento: {c2['armazenamento']}% | Estabilidade: {c2['estabilidade']}% | janela downlink:{c2['janela_downlink']} % ")
        print("==="*50)
        print(f"C3 -temperatura:{c3['temperatura']}°C | saude do dispositivo: {c3['saude']}% | Armazenamento: {c3['armazenamento']}% | Estabilidade: {c3['estabilidade']}% | janela downlink:{c3['janela_downlink']} % ")
        print("==="*50)
        print(" RELATÓRIO DE CONTINGÊNCIAS:")
        print("==="*50)
        print()
        if lista_alertas:
            for alerta in lista_alertas:
                print(alerta)
        else:
            print("Todos os Sistemas Estáveis - Nenhuma ação necessária.")
        print()
        time.sleep(0.70)    
        print("==="*50)
        print() 
        print("==="*50)
        print(f"Previsao Identificada pelo Satelite: {ambiente}")
        print("==="*50)
        print("Graficos ")
        time.sleep(2)
        resposta = input("Deseja ver os graficos de desempennho (S/N):  ").upper().strip()
        
        if resposta == "S": 
            graficos()
        elif resposta =="N":
            print("Visualizacao de graficos cancelada ")
        else:
            print("Parece que voce nao selecionou nenhuma das opcoes a cima ou digitou errado , vamos entender que voce nao deseja visualizar os graficos ")
     
    teste()
    print("")
    print("---"*50 )
    print("Passando dados para central de inteligencia ")
    print("---"*50 )
    
           
    
    return f"Status: {alertas_texto} | Bateria: {dados_ultimo['saude']}% | Janela: {dados_ultimo['janela_downlink']}"








