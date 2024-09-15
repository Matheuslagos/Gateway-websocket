import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from appwebsocket.routing import websocket_urlpatterns as ws_patterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gateway.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            ws_patterns  # As rotas WebSocket serão roteadas pelo gateway
        )
    ),
})
