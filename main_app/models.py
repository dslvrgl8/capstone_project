from django.db import models

# Create your models here.
class Character(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    race = models.CharField(max_length=100)
    class_level = models.CharField(max_length=250)
    alignment = models.CharField(max_length=100)
    strength = models.CharField(max_length=100)
    dexterity = models.CharField(max_length=100)
    constitution = models.CharField(max_length=100)
    intelligence = models.CharField(max_length=100)
    wisdom = models.CharField(max_length=100)
    charisma = models.CharField(max_length=100)
    armor_class = models.CharField(max_length=100)
    initiative = models.CharField(max_length=100)
    speed = models.CharField(max_length=100)
    hitpoints = models.CharField(max_length=100)
    bio = models.TextField(max_length=500)
    current_campaign = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']