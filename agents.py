from crewai import Agent
from tools import FetchCountryInfo, FetchWeatherTool, FetchRecipeTool
from config import get_llm

def create_geografo():
    return Agent(
        role='Geógrafo meticuloso',
        goal='Falar informações ',
        backstory='Você é um geógrafo com especialidade em saber informações sobre países',
        tools=[FetchCountryInfo()],
        verbose=True,
        allow_delegation=False,
        llm=get_llm()
    )

def create_cozinheiro():
    return Agent(
        role='Cozinheiro genial',
        goal='Sugerir comidas típicas de certo país',
        backstory='Você é um cozinheiro com vasto conhecimento em culinária típica',
        tools=[FetchRecipeTool()],
        verbose=True,
        allow_delegation=False,
        llm=get_llm()
    )

def create_meteorologista():
    return Agent(
        role="Meteorologista",
        goal="Fornecer previsões climáticas precisas",
        backstory="Especialista em análise atmosférica.",
        tools=[FetchWeatherTool()],
        verbose=True,
        llm=get_llm()
    )