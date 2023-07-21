from django.urls import path
from . import views
from main_app.views import testFight

urlpatterns = [
    path('', views.Home.as_view(), name="home"), # <- here we have added the new path
    path('characters/', views.CharacterList.as_view(), name="character_list"),
    path('characters/new/', views.CharacterCreate.as_view(), name="character_create"),
    path('characters/<int:pk>/', views.CharacterDetail.as_view(), name="character_detail"),
    path('characters/<int:pk>/update',views.CharacterUpdate.as_view(), name="character_update"),
    path('characters/<int:pk>/delete',views.CharacterDelete.as_view(), name="character_delete"),
    path('characters/<int:pk>/gear', views.GearCreate.as_view(), name="gear_create"),
    path('campaign_character_assoc/<int:campaign_pk>/add/', views.CampaignCharacterAssoc.as_view(), name='add_character_to_campaign'),
    path('campaigns/<int:campaign_pk>/characters/<int:character_pk>/add/', views.CampaignCharacterAssoc.as_view(), name="campaign_character_assoc"),
]