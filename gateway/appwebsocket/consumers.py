import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Aceitar a conexão do WebSocket
        await self.accept()

    async def disconnect(self, close_code):
        # Limpar a conexão, se necessário
        pass

    async def receive(self, text_data):
        # Receber dados do WebSocket
        data = json.loads(text_data)
        message = data.get('message', '')

        # Enviar a mensagem de volta pelo WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
