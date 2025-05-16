from crewai import Task

def buscar_comidas(agent, destino):
    return Task(
        description=f'''Analise a culinária de {destino} (use gentílico em inglês):
        1. Liste os 5 pratos mais representativos
        2. Para cada prato: nome, ingredientes principais e ocasião típica
        3. Se for cidade, use gentílico do país em inglês''',
        agent=agent,
        expected_output="Lista de pratos típicos com descrições básicas",
        output_file="output/resultado_comida.txt",
        verbose=True
    )

def buscar_clima(agent, destino, context):
    return Task(
        description=f'''Forneça análise meteorológica de {destino} (localidade em inglês):
        1. Condições atuais: temperatura, umidade, condições do céu
        2. Previsão para 24h
        3. Recomendações práticas
        
        Para países, use a capital.''',
        agent=agent,
        expected_output="Análise meteorológica com condições atuais e previsões",
        output_file="output/previsao_tempo.txt",
        context=context
    )
    

def buscar_informacoes(agent,destino, context):
    return Task(
        description=f'''Analise a localidade de {destino}(em inglês):
        1. Básico: localização, população, idioma
        2. Cultural: tradições principais
        3. Econômico: atividades principais
        4. Geográfico: clima e relevo
        
        Para cidades, use o país em inglês.''',
        agent=agent,
        expected_output="Resumo das informações essenciais sobre o local",
        output_file="output/infos_pais.txt",
        context=context
    )