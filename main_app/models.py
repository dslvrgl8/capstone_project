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
    appearance = models.TextField(max_length=500)
    backstory = models.TextField(max_length=500)
    current_campaign = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

# below Artist Model

class Gear(models.Model):

    weapon = models.CharField(max_length=150)
    spell = models.TextField(max_length=500)
    money = models.CharField(max_length=100)
    equipment = models.TextField(max_length=500)
    class_ability = models.TextField(max_length=500)
    hit_dice = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    acrobatics_dex = models.CharField(max_length=100)
    animal_handling_wis = models.CharField(max_length=100)
    arcana_int = models.CharField(max_length=100)
    athletics_str = models.CharField(max_length=100)
    deception_cha = models.CharField(max_length=100)
    history_int = models.CharField(max_length=100)
    insight_wis = models.CharField(max_length=100)
    intimidation_cha = models.CharField(max_length=100)
    investigation_int = models.CharField(max_length=100)
    medicine_wis = models.CharField(max_length=100)
    nature_int = models.CharField(max_length=100)
    perception_wis = models.CharField(max_length=100)
    performance_cha = models.CharField(max_length=100)
    persuasion_cha = models.CharField(max_length=100)
    religion_int = models.CharField(max_length=100)
    sleight_of_hand_dex = models.CharField(max_length=100)
    stealth_dex = models.CharField(max_length=100)
    survival_wis = models.CharField(max_length=100)
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name="gears")

    def __str__(self):
        return str(self.character)
    
class Campaign(models.Model):
    title = models.CharField(max_length=150)
    characters = models.ManyToManyField(Character)

    def __str__(self):
        return self.title
