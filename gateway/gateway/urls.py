from django.contrib import admin
from django.urls import path
from appgateway.api import api as appgateway
from appendpoint.api import api as appendpoint
from appwebsocket.routing import websocket_urlpatterns
from django.urls import path, re_path
from appgateway.api import api as appgateway
from appendpoint.api import api as appendpoint
from appwebsocket.consumers import ChatConsumer  # Importar o consumidor do WebSocket
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/gateway/', appgateway.urls),
    path('api/endpoint/', appendpoint.urls),
    re_path(r'ws/chat/$', ChatConsumer.as_asgi()),
]

# WebSocket routing
websocket_urlpatterns = [
    re_path(r'ws/chat/$', ChatConsumer.as_asgi()),  # Adicionar rota WebSocket
]

# Configurar o ASGI application para lidar com WebSockets e HTTP
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns  # Adicionar as rotas de WebSocket
        )
    ),
})