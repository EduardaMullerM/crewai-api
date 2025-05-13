from crewai import Crew
from agents import *
from tasks import *
from dotenv import load_dotenv

load_dotenv()

# Cria agentes

destino = input('Insira seu destino: ')

cozinheiro = create_cozinheiro()
meteorologista = create_meteorologista()
geografo = create_geografo()

# Cria tarefas
task1 = buscar_comidas(cozinheiro, destino)
task2 = buscar_clima(meteorologista, [task1])
task3 = buscar_informacoes(geografo, [task1])

# Configura Crew
crew = Crew(
    agents=[cozinheiro, meteorologista, geografo],
    tasks=[task1, task2, task3],
    verbose=True,
    memory=True
)

# Execução
print("## Iniciado ##")
resultado = crew.kickoff()

print("\n=== RESULTADOS ===")
print(resultado)