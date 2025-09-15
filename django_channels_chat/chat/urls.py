from django.urls import path

from .views import group_chat_view, home_view

urlpatterns = [
    path('', home_view, name='home'),
    path("gruops/<uuid:uuid>/", group_chat_view, name="group"),
]