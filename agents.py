from crewai import Agent
from tools import FetchCountryInfo, FetchWeatherTool, FetchRecipeTool
from config import get_llm

def create_geografo():
    return Agent(
        role='Geógrafo Especialista',
        goal='Fornecer análises precisas sobre países e suas características principais',
        backstory='Especialista em geografia com foco em aspectos culturais, políticos e socioeconômicos. Habilidade em sintetizar informações complexas de forma clara.',
        tools=[FetchCountryInfo()],
        verbose=True,
        allow_delegation=False,
        llm=get_llm()
    )

def create_cozinheiro():
    return Agent(
        role='Chef Internacional',
        goal='Identificar e analisar pratos típicos e tradições culinárias regionais',
        backstory='Chef especializado em gastronomia global, com expertise em identificar pratos tradicionais, ingredientes locais e técnicas culinárias regionais.',
        tools=[FetchRecipeTool()],
        verbose=True,
        allow_delegation=False,
        llm=get_llm()
    )

def create_meteorologista():
    return Agent(
        role="Meteorologista Climatologista",
        goal="Fornecer análises meteorológicas precisas e recomendações práticas",
        backstory="Especialista em climatologia com foco em previsão meteorológica, análise de padrões climáticos e impactos em atividades humanas.",
        tools=[FetchWeatherTool()],
        verbose=True,
        llm=get_llm()
    )