João Ribeiro — RM: 570562 — Turma: 1CCPH-
Gabriel de Paula - rm : 573195 – Turma: 1CCPH-
Enzo Ribeiro - rm : 569429 - Turma: 1CCPH-

 

Sistema de monitoramento inteligente para subsistemas críticos terrestres e aeroespaciais com integração a modelos de IA via Ollama.



Como a ia  é usada ?

A IA recebe um snapshot da telemetria atual, as diretrizes definidas no system_prompt.md e a pergunta do operador. Com esse contexto, o modelo processa os dados via Ollama e retorna análises, interpretações e recomendações operacionais em tempo real.


Requisitos
Antes de executar o projeto, certifique-se de possuir:
Python 3.x
matplotlib
ollama
python-dotenv
prompt_toolkit
pyfiglet
rich


Configuração
O sistema pode se conectar a uma infraestrutura Ollama local ou remota.
Crie um arquivo .env na raiz do projeto e configure sua chave de autenticação:
Configurações de Credenciais do Mission Red
OLLAMA_API_KEY="sua_chave_de_api_aqui"

Observação
Certifique-se de que o modelo gpt-oss:120b esteja disponível ou corretamente configurado no endpoint padrão do host Ollama utilizado.

Estrutura do Projeto
mission-control-ai/
├── src/
│ ├── telemetria.py
│ │ Simulação de dados (ciclos) e plotagem com Matplotlib
│ └── alertas.py
│ Lógica do motor de contingência e formatação de alertas
├── prompts/
│ └── system_prompt.md
│ Diretrizes e engenharia de prompt para o comportamento da IA
├── .env
│ Chaves de ambiente e tokens de autenticação
├── main.py
│ Loop principal da CLI e gerenciamento de estados
└── README.md
Documentação oficial do projeto

Como Executar
Clone ou baixe os arquivos do projeto.
Abra um terminal na pasta raiz.
Execute o programa principal:
```bash
  python main.py
   ```


Comandos Disponíveis

Durante a execução da CLI do Mission Control, será exibido o prompt interativo:
❯❯❯
Você pode realizar perguntas em linguagem natural para a IA ou utilizar os comandos operacionais:
/status — Exibe o relatório sumário em tempo real.
/help — Lista todos os comandos disponíveis.
/clear — Limpa a tela e renderiza novamente o banner principal.
/exit — Finaliza a sessão de monitoramento com segurança.


Funcionamento do Sistema
Geração e Avaliação
O módulo ciclos() gera dados pseudoaleatórios simulando:

Condições meteorológicas:
Chuva
Neve
Sem previsão significativa
Parâmetros internos de hardware:
Temperatura
Integridade do dispositivo
Uso de armazenamento
Estabilidade
Downlink
Essas métricas são atualizadas continuamente durante a execução.

Interceptação e Alertas
A rotina alertas() intercepta os dados gerados e verifica se todos os parâmetros permanecem dentro das faixas operacionais seguras.
Quando uma anomalia é detectada:
Ações de contingência são geradas automaticamente.
Alertas são adicionados ao relatório operacional.

O operador pode visualizar gráficos de diagnóstico utilizando Matplotlib.
Engenharia de Prompt Dinâmica
Ao interagir com a IA, a classe Mission Engine constrói um payload contendo:
Diretrizes do arquivo system_prompt.md
Snapshot consolidado da telemetria atual
Pergunta enviada pelo operador
Esse contexto é enviado ao modelo Ollama para análise especializada.
Interface Rica
As respostas retornadas pela IA são apresentadas em painéis semânticos utilizando a biblioteca Rich, incluindo:
Horário exato da análise
Contexto operacional
Resultado consolidado da interpretação do modelo

Fluxo de Engenharia
1. Coleta e Simulação
A telemetria é gerada continuamente por uma rotina estocástica baseada em números pseudo aleatórios.
2. Validação Operacional
Os dados passam pelo motor de alertas responsável por identificar falhas e desvios operacionais.
3. Construção de Contexto
A telemetria consolidada é combinada com as instruções do sistema e a consulta do operador.
4. Processamento por IA
O payload é enviado ao servidor Ollama para inferência.
5. Apresentação
O resultado é exibido ao operador por meio de uma interface de terminal enriquecida.

Cenários de Teste Cobertos
Operação Normal
Todos os parâmetros permanecem dentro dos limites operacionais esperados.
Resultado:
Sistemas estáveis
Nenhuma ação corretiva necessária
Temperatura Crítica
Condição:
Temperatura superior a 80°C
Ação automática:
Sistema de resfriamento térmico ativado
Saúde Crítica do Dispositivo
Condição:
Integridade inferior a 30%
Ação automática:
Ativação do Modo de Segurança
Armazenamento Quase Lotado
Condição:
Utilização superior a 85%
Ação automática:
Limpeza de cache
Descarte de dados voláteis
Instabilidade de Atitude
Condição:
Estabilidade inferior a 50%
Ação automática:
Reequilibrar a aeronave
Perda de Comunicação (Downlink)
Condição:
Janela de downlink inferior a 50%
Ação automática:
Preservação de dados
Mitigação de tráfego
Priorização de comunicação crítica

Limitações Conhecidas
Simulação Estocástica Local
A telemetria é gerada por uma rotina baseada em random.randrange, o que impede a persistência histórica real sem a integração de um banco de dados.
Dependência de Conectividade
As análises realizadas pela IA dependem de uma conexão ativa com o host Ollama.
Possíveis impactos:
Atraso nas respostas
Falhas temporárias de inferência
Interrupções causadas por instabilidades de rede
Gráficos Bloqueantes
As janelas do Matplotlib interrompem temporariamente o fluxo principal da CLI até que o usuário feche manualmente o gráfico exibido.

Objetivo
O Mission Control AI foi desenvolvido para monitoramento inteligente de subsistemas críticos terrestres e aeroespaciais, combinando telemetria simulada, motores de contingência e modelos avançados de linguagem para suporte operacional em tempo real.


Persona da IA: Analista de Dados Geoespaciais para o Agronegócio, especializado em transformar dados de satélite e sensoriamento remoto em insights práticos para produtores rurais. Interpreta índices de vegetação, umidade do solo e condições climáticas para apoiar o monitoramento e a tomada de decisões no campo.
 

Prompt usado em : prompts/system_prompt.md  

prints de estado de alerta e estado normal 

dentro de assets :
assets/screenshot_normal.png
assets/screenshot_alerta.png



respostas da pergunta : 
Qual o problema real terrestre que esta missão resolve?

O projeto resolve a baixa capacidade de interpretação veloz de dados obtidos por satélites focados em agricultura, onde produtores e analistas recebem os diferentes tipos de dados, mas não conseguem interpretar e transformar em decisões reais.

Quem paga pela solução? Setor público (governo, INPE, ANATEL)? Setor privado (operadora, cooperativa, frota)? Híbrido?
O setor privado, pois se trata de uma solução que impactaria grandes fazendas, agronegócio e empresas agrotechs que necessitam desses serviços de monitoramento, pois eles têm a responsabilidade de administrar diferentes safras em enormes quantidades.

Métrica de impacto: se o satélite operar 100% saudável por 1 ano, o que muda concretamente no mundo? (Ex: X hectares monitorados, Y toneladas de CO ₂ evitadas, Z escolas conectadas)

Monitoramento contínuo de enormes hectares de terra Redução de perdas por estresse hídrico, pragas ou clima extremo graças a alertas antecipados Melhor uso efetivo de insumos (água, fertilizantes), reduzindo custo e impacto ambiental Maior previsibilidade de safra e produtividade


Modelo de negócio: SaaS? Dado-como-serviço? Concessão pública? Assinatura?

O modelo mais coerente com seu projeto é: SaaS: acesso à plataforma de análise e IA (dashboard/CLI/alertas) DaaS: venda de relatórios geoespaciais, análises de NDVI e monitoramento contínuo por área agrícola



link do video do Youtube : https://youtu.be/mMqfYAuUr3Y