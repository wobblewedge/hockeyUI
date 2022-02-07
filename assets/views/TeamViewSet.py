from rest_framework import viewsets
from models.Team import Team, TeamSerializer

class TeamViewSet(viewsets.ModelViewSet):
   queryset = Team.objects.all()
   serializer_class = TeamSerializer