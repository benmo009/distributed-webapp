# counter/urls.py
from django.urls import path

from . import views

app_name = "counter"
urlpatterns = [
    path("", views.index, name="index"),
    path('<int:counter_id>', views.counter_log, name='counter-log'),
    path("new-counter", views.new_counter, name="new-counter"),
]