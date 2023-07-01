from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
#...
from django.views.generic.base import TemplateView

# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
    template_name = "home.html"

class Character:
    def __init__(self, name, image, character_class):
        self.name = name
        self.image = image
        self.character_class = character_class

characters = [
    Character('Bojan', 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Tanuki_in_Higashiyama_Zoo_-_2.jpg/640px-Tanuki_in_Higashiyama_Zoo_-_2.jpg', 'Monk'), Character('Stalker', 'https://static.wikia.nocookie.net/dnd4/images/5/5a/Elf_ranger.jpg/revision/latest/scale-to-width-down/780?cb=20130708222756', 'Ranger'),
]

class CharacterList(TemplateView):
    template_name = "character_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["characters"] = characters # this is where we add the key into our context object for the view to use
        return context
