class Team(models.Model):
    client = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    proposal_text = models.TextField(blank=True)

class TeamSerializer(serializers.ModelSerializer):
   class Meta:
       model = Quote
       fields = ["teams", "shots", "Shots On Goal", "Scoring Chances", "Dump Chance%", "5v4 Carry%", 
       "5v4 Setup%", "5v4 Chance%"]