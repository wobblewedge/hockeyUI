from models import Team
from rest_framework import serializers

class TeamSerializer(serializers.ModelSerializer):
   class Meta:
       model = Team
       fields = ["teams", "shots", "Shots On Goal", "Scoring Chances", "Dump Chance%", "5v4 Carry%", 
       "5v4 Setup%", "5v4 Chance%"]