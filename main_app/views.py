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
from .models import Character, Gear

from django.urls import reverse

# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
    template_name = "home.html"

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

class GearCreate(View):

    def post(self, request, pk):
        acrobatics_dex = request.POST.get("acrobatics")
        animal_handling_wis = request.POST.get("animal handling")
        arcana_int = request.POST.get("arcana")
        athletics_str = request.POST.get("strength")
        deception_cha = request.POST.get("deception")
        history_int = request.POST.get("history")
        insight_wis = request.POST.get("insight")
        intimidation_cha = request.POST.get("intimidation")
        investigation_int = request.POST.get("investigation")
        medicine_wis = request.POST.get("medicine")
        insight_wis = request.POST.get("insight")
        intimidation_cha = request.POST.get("intimidation")
        character = Character.objects.get(pk=pk)
        Gear.objects.create(title=title, length=length, character=character)
        return redirect('character_detail', pk=pk)