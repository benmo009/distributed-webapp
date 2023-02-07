# counter/consumers.py
import json

from channels.generic.websocket import AsyncWebsocketConsumer

class CountConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.counter_name = self.scope['url_route']['kwargs']['counter_id']
        self.counter_group = f'counter_{self.counter_name}'

        await self.channel_layer.group_add(self.counter_group, self.channel_name)
        
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.counter_group, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)

        if text_data_json["type"] == "start":
            response = { "type": "start_ack" }
        elif text_data_json["type"] == "pause":
            response = { "type": "pause_ack" }        

        await self.channel_layer.group_send(
            self.counter_group, response
        )

    async def start_ack(self, event):
        event["message"] = "starting count"

        await self.send(text_data=json.dumps(event))

    async def pause_ack(self, event):
        event["message"] = "pausing count"

        await self.send(text_data=json.dumps(event))

    async def test(self, event):
        await self.send(text_data=json.dumps(event))