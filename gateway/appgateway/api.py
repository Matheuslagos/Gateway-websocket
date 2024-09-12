from ninja import NinjaAPI
import requests

api = NinjaAPI(urls_namespace='appgetway')

# Exemplo de endpoint no API Gateway que orquestra as chamadas para outra API
@api.get("/")
def get_getway(request, a: int, b: int):
    # URL da outra API (que está sendo orquestrada)
    api_url = f"http://127.0.0.1:8000/api/endpoint/add?a={a}&b={b}"
    response = requests.get(api_url)
    
    # Retorna a resposta da outra API
    return response.json()