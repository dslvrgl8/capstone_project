from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"), # <- here we have added the new path
    path('characters/', views.CharacterList.as_view(), name="character_list"),
    path('characters/new/', views.CharacterCreate.as_view(), name="character_create"),
    path('characters/<int:pk>/', views.CharacterDetail.as_view(), name="character_detail"),
    path('characters/<int:pk>/update',views.CharacterUpdate.as_view(), name="character_update"),
    path('characters/<int:pk>/delete',views.CharacterDelete.as_view(), name="character_delete"),
    path('characters/<int:pk>/gear', views.GearCreate.as_view(), name="gear_create"),
    path('characters/<int:pk>/gear/<int:pk2>/update', views.GearUpdate.as_view(), name="gear_update"),
    path('campaigns/<int:pk>/characters/<int:character_pk>/', views.CampaignCharacterAssoc.as_view(), name="campaign_character_assoc"),
]
