from channels.routing import ProtocolTypeRouter, URLRouter
from appwebsocket.routing import websocket_urlpatterns as ws_patterns

application = ProtocolTypeRouter({
    "websocket": URLRouter(ws_patterns)  # Roteia os WebSocket para o appwebsocket
})