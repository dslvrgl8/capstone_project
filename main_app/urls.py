from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"), # <- here we have added the new path
    path('characters/', views.CharacterList.as_view(), name="character_list")
]
