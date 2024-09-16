from ninja import NinjaAPI
import requests

api = NinjaAPI(urls_namespace='appgetway')

@api.get("/add/")
def get_add(request, a: int, b: int):
    api_url = f"http://127.0.0.1:8000/api/endpoint/add?a={a}&b={b}"
    response = requests.get(api_url)
    
    return response.json()

@api.get("/sub/")
def get_sub(request, a: int, b: int):
    api_url = f"http://127.0.0.1:8000/api/endpoint/sub?a={a}&b={b}"
    response = requests.get(api_url)
    
    return response.json()

@api.get("/cep/")
def get_cep(request, cep:int):
    api_url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(api_url)
    
    return response.json()
