from ninja import NinjaAPI

api = NinjaAPI(urls_namespace='appendpoint')


@api.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}


@api.get("/sub")
def sub(request, a: int, b: int):
    return {"result": a - b}