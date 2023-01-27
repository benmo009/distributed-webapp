# chat/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/counter/(?P<counter_id>\w+)/$", consumers.CountConsumer.as_asgi()),
]