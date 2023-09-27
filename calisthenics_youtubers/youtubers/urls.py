from django.urls import path
from . import views

urlpatterns = [
    path("", views.youtuber_basic, name="youtuber_basic"),
    path("<int:pk>/", views.youtuber_expanded, name="youtuber_expanded"),
    path("add_youtuber", views.add_youtuber, name='add_youtuber'),
]