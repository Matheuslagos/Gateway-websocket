from django.contrib import admin
from django.urls import path
from appgateway.api import api as appgateway
from appendpoint.api import api as appendpoint
from appwebsocket.routing import websocket_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/gateway/', appgateway.urls),
    path('api/endpoint/', appendpoint.urls),
]
urlpatterns += websocket_urlpatterns