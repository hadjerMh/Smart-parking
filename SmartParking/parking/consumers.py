from channels.generic.websocket import AsyncWebsocketConsumer

from .models import smartParking, Reservation, State
import json


class parkingConsumer(AsyncWebsocketConsumer):
	async def connect(self):
		await self.accept()
	async def disconnect(self,close_code):
		await self.disconnect()
	async def receive(self, text_data):
		print('!!!!',text_data)
		pass