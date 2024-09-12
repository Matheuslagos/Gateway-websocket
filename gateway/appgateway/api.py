from ninja import NinjaAPI
import requests

api = NinjaAPI(urls_namespace='appgetway')

# Orquestra chamada para o endpoint "add" da API "appendpoint"
@api.get("/add/")
def get_add(request, a: int, b: int):
    api_url = f"http://127.0.0.1:8000/api/endpoint/add?a={a}&b={b}"
    response = requests.get(api_url)
    
    # Retorna a resposta da API "appendpoint"
    return response.json()

# Orquestra chamada para o endpoint "sub" da API "appendpoint"
@api.get("/sub/")
def get_sub(request, a: int, b: int):
    api_url = f"http://127.0.0.1:8000/api/endpoint/sub?a={a}&b={b}"
    response = requests.get(api_url)
    
    # Retorna a resposta da API "appendpoint"
    return response.json()
