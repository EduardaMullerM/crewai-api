import requests
from crewai.tools import BaseTool
import os
    
class FetchCountryInfo(BaseTool):
    name: str = 'Consultor de info de países'
    description: str = 'Obtém info de um determinado país'
    
    def _run(self, pais: str) -> str:
        response = requests.get(f'https://restcountries.com/v3.1/name/{pais}')
        return response.json()        
    
class FetchRecipeTool(BaseTool):
    name: str = 'Consultor de receitas culinárias'
    description: str = 'Obtém a culinária local de determinada região'
    
    def _run(self, gentilico: str) -> str:
        response = requests.get(f'https://www.themealdb.com/api/json/v1/1/filter.php?a={gentilico}')
        return response.json()
    
class FetchWeatherTool(BaseTool):
    name: str = 'Meteorologista'
    description: str = 'Obtém a previsão do tempo para uma cidade.'
    
    def _run(self, cidade: str) -> str:
        ac_key = os.getenv('WEATHER_API_KEY')
        response = requests.get(f'http://api.weatherstack.com/current?access_key={ac_key}&query={cidade}')
        return response.json()