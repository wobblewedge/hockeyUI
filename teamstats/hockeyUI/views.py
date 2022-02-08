from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from models import Team, TeamSerializer
# Create your views here.

class TeamViewSet(viewsets.ModelViewSet):
   queryset = Team.objects.all()
   serializer_class = TeamSerializer
   permission_classes = [permissions.IsAuthenticated]