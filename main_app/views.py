from typing import Any, Dict
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View# <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
#...
from django.views.generic.base import TemplateView

# This will import the class we are extending 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# after our other imports 
from django.views.generic import DetailView
# import models
from .models import Character, Gear, Campaign

from django.urls import reverse

from django.shortcuts import get_object_or_404

# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
    template_name = "home.html"
    # Here we have added the playlists as context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["campaigns"] = Campaign.objects.all()
        return context

# class Character:
#     def __init__(self, name, image, character_class):
#         self.name = name
#         self.image = image
#         self.character_class = character_class

# characters = [
#     Character('Bojan', 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Tanuki_in_Higashiyama_Zoo_-_2.jpg/640px-Tanuki_in_Higashiyama_Zoo_-_2.jpg', 'Monk'), Character('Stalker', 'https://static.wikia.nocookie.net/dnd4/images/5/5a/Elf_ranger.jpg/revision/latest/scale-to-width-down/780?cb=20130708222756', 'Ranger'),
# ]

class CharacterList(TemplateView):
    template_name = "character_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["characters"] = Character.objects.filter(name__icontains=name)
            # We add a header context that includes the search param
            context["header"] = f"Searching for {name}"
        else:
            context["characters"] = Character.objects.all()
            context["gears"] = Gear.objects.all()
            # default header for not searching 
            context["header"] = "All Characters"
        return context

class CharacterCreate(CreateView):
    model = Character
    fields = ['name', 'img', 'race', 'class_level', 'alignment', 'strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma', 'armor_class', 'initiative', 'speed', 'hitpoints', 'bio', 'appearance', 'backstory', 'current_campaign']
    template_name = "character_create.html"
    # this will get the pk from the route and redirect to artist view
    def get_success_url(self):
        return reverse('character_detail', kwargs={'pk': self.object.pk})

class CharacterDetail(DetailView):
    model = Character
    template_name = "character_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gear'] = self.object.gears.all()
        return context
        
class CharacterUpdate(UpdateView):
    model = Character
    fields = ['name', 'img', 'race', 'class_level', 'alignment', 'strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma', 'armor_class', 'initiative', 'speed', 'hitpoints', 'bio', 'appearance', 'backstory', 'current_campaign']
    template_name = "character_update.html"

    def get_success_url(self):
        return reverse('character_detail', kwargs={'pk': self.object.pk})
    
class CharacterDelete(DeleteView):
    model = Character
    template_name = "character_delete_confirmation.html"
    success_url = "/characters/"


class GearCreate(CreateView):
    model = Gear
    fields = ['weapon', 'spell', 'money', 'equipment', 'class_ability', 'hit_dice', 'language', 'acrobatics_dex', 'animal_handling_wis', 'arcana_int', 'athletics_str', 'deception_cha', 'history_int', 'insight_wis', 'intimidation_cha', 'investigation_int', 'medicine_wis', 'nature_int', 'perception_wis', 'performance_cha', 'persuasion_cha', 'persuasion_cha', 'religion_int', 'sleight_of_hand_dex', 'stealth_dex', 'survival_wis']
    template_name = "gear_create.html"
    # this will get the pk from the route and redirect to artist view
    
    def form_valid(self, form):
        character_pk = self.kwargs['pk']
        character = get_object_or_404(Character, pk=character_pk)
        form.instance.character = character
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('character_update', kwargs={'pk': self.object.pk})
    
class GearUpdate(UpdateView):
    model = Gear
    fields = ['weapon', 'spell', 'money', 'equipment', 'class_ability', 'hit_dice', 'language', 'acrobatics_dex', 'animal_handling_wis', 'arcana_int', 'athletics_str', 'deception_cha', 'history_int', 'insight_wis', 'intimidation_cha', 'investigation_int', 'medicine_wis', 'nature_int', 'perception_wis', 'performance_cha', 'persuasion_cha', 'persuasion_cha', 'religion_int', 'sleight_of_hand_dex', 'stealth_dex', 'survival_wis']
    template_name = "gear_update.html"
    # this will get the pk from the route and redirect to artist view
    def get_success_url(self):
        return reverse('character_detail', kwargs={'pk': self.object.pk})
    

class CampaignCharacterAssoc(View):

    def get(self, request, pk, character_pk):
        # get the query param from the url
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            # get the playlist by the id and
            # remove from the join table the given song_id
            Campaign.objects.get(pk=pk).characters.remove(character_pk)
        if assoc == "add":
            # get the playlist by the id and
            # add to the join table the given song_id
            Campaign.objects.get(pk=pk).characters.add(character_pk)
        return redirect('home')