from crewai import Task

def buscar_comidas(agent, destino):
    return Task(
        description=f"Usando o gentílico do país {destino} EM INGLES, consulte as comidas típicas desse lugar, caso seja uma cidade, use o gentílico EM INGLES do país em que se localiza",
        agent=agent,
        expected_output="Lista de comidas típicas",
        output_file="output/resultado_comida.txt",
        verbose=True,
        
    )

def buscar_clima(agent, context):
    return Task(
        description="Obtenha a previsão do tempo para a localidade EM INGLES, caso seja informado um país, escolha a capital EM INGLES.",
        agent=agent,
        expected_output="Descrição do clima e temperatura em °C",
        output_file="output/previsao_tempo.txt",
        context=context
    )
    

def buscar_informacoes(agent, context):
    return Task(
        description="Obtenha a previsão do tempo para a localidade EM INGLES, caso seja informado uma cidade, escolha o país dela EM INGLES.",
        agent=agent,
        expected_output="Informações sobre determinado país",
        output_file="output/infos_pais.txt",
        context=context
    )