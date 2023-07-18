from django.db import models

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
# Create your models here.
class Gear(models.Model):

    weapon = models.CharField(max_length=150, blank=True)
    spell = models.TextField(max_length=500, blank=True)
    money = models.CharField(max_length=100, blank=True)
    equipment = models.TextField(max_length=500, blank=True)
    class_ability = models.TextField(max_length=500, blank=True)
    hit_dice = models.CharField(max_length=100, blank=True)
    language = models.CharField(max_length=100, blank=True)
    acrobatics_dex = models.CharField(max_length=100, blank=True)
    animal_handling_wis = models.CharField(max_length=100, blank=True)
    arcana_int = models.CharField(max_length=100, blank=True)
    athletics_str = models.CharField(max_length=100, blank=True)
    deception_cha = models.CharField(max_length=100, blank=True)
    history_int = models.CharField(max_length=100, blank=True)
    insight_wis = models.CharField(max_length=100, blank=True)
    intimidation_cha = models.CharField(max_length=100, blank=True)
    investigation_int = models.CharField(max_length=100, blank=True)
    medicine_wis = models.CharField(max_length=100, blank=True)
    nature_int = models.CharField(max_length=100, blank=True)
    perception_wis = models.CharField(max_length=100, blank=True)
    performance_cha = models.CharField(max_length=100, blank=True)
    persuasion_cha = models.CharField(max_length=100, blank=True)
    religion_int = models.CharField(max_length=100, blank=True)
    sleight_of_hand_dex = models.CharField(max_length=100, blank=True)
    stealth_dex = models.CharField(max_length=100, blank=True)
    survival_wis = models.CharField(max_length=100, blank=True)
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name="gears")

    def __str__(self):
        return str(self.character)
class Campaign(models.Model):
    title = models.CharField(max_length=150)
    characters = models.ManyToManyField(Character)

    def __str__(self):
        return self.title