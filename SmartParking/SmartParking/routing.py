from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator
from django.urls import path
from parking import consumers
websocket_urlPattern = [
	path('ws/home/', consumers.parkingConsumer),
]

application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    'websocket':AuthMiddlewareStack(URLRouter(websocket_urlPattern))

})