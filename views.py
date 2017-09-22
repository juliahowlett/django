from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		#"leagues": League.objects.all(),
		#"leagues": League.objects.filter(sport__contains="baseball"),
		#"leagues": League.objects.filter(sport__contains="women"),
		"leagues": League.objects.filter(sport__contains="hockey"),
		#"leagues": League.objects.exclude(sport__contains="football"),
		#"leagues": League.objects.filter(name__contains="conferences"),
		#"leagues": League.objects.filter(name__startswith="Atlantic"),
		#"teams": Team.objects.all(),
		#"teams": Team.objects.filter(location__contains="Dallas"),
		#"teams": Team.objects.filter(team_name__contains="Raptors"),
		"teams": Team.objects.filter(location__contains="City"),
		#"teams": Team.objects.filter(team_name__startswith="T"),
		#all teams, ordered alphabetically by location
		#"teams": Team.objects.order_by("location"),
		#all teams, ordered by team name in reverse alphabetical order
		#"teams": Team.objects.order_by("-team_name"),
		#"players": Player.objects.all(),
		#every player with last name "Cooper"
		#"players": Player.objects.filter(last_name__contains="Cooper"),
		#every player with first name "Joshua"
		#"players": Player.objects.filter(first_name__contains="Joshua"),
		#every player with last name "Cooper" EXCEPT those with "Joshua" as the first name
		#"players": Player.objects.filter(last_name__contains="Cooper").exclude(first_name__contains="Joshua"),
		#all players with first name "Alexander" OR first name "Wyatt",
		"players": Player.objects.filter(first_name__contains="Alexander")|Player.objects.filter(first_name__contains="Wyatt"),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")