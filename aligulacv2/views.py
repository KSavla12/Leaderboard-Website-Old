from django.shortcuts import render
from django.http import HttpResponse
from .models import Player_stats, Match_history
import operator


def index(request):
    return render(request, 'index.html')


def home(request):
    players = Player_stats.objects.order_by('-rating')[:10]

    context = {
        'players': players,
    }
    return render(request, 'aligulacv2/home.html', context)


def player_list(request):
    countries = Player_stats.objects.all()
    countries_list = []
        
    for country in countries:
        countries_list.append(country.player_country)
    countries_list = list(dict.fromkeys(countries_list))

    if 'filter' in request.POST:
        race = request.POST['race']
        country = request.POST['country']

        filter = (Player_stats.objects.filter(player_race__contains=race)) & (Player_stats.objects.filter(player_country__contains=country)).order_by('-rating')

        context = {
            'title': 'Rankings',
            'countries_list': countries_list,
            'filter': filter,
        }
        return render(request, 'aligulacv2/player_list.html', context)

    else:    
        players = Player_stats.objects.order_by('-rating')

        context = {
            'title': 'Rankings',
            'players': players,
            'countries_list': countries_list,
        }
        return render(request, 'aligulacv2/player_list.html', context)


def player_page(request, player):
    matches = Match_history.objects.filter(player_a=player).order_by('-date') | Match_history.objects.filter(player_b=player).order_by('-date')
    name = Player_stats.objects.get(id=player)

    # Chart data:
    player1 = []
    rating = []
    player_data = Match_history.objects.filter(player_a__id=player).order_by('date') | Match_history.objects.filter(player_b__id=player).order_by('date')

    # Limit chart data to 12 entries
    if len(player_data) > 12:
        player_data1 = player_data[len(player_data)-12:len(player_data)]
    else:
        player_data1 = player_data

    # Remove same day dates
    for i in player_data1:
        if i.date not in player1:
            player1.append(i.date)
            rating.append(i.player_a_rating)

    context = {
        'title': 'Match History',
        'matches': matches,
        'player1' : player1,
        'rating' : rating,
        'player_data1': player_data1,
        'name': name,
    }
    return render(request, 'aligulacv2/player_page.html', context)


def search(request):

    if request.method == "POST":
        player = request.POST.get('player')
        fromdate = request.POST['fromdate']
        todate = request.POST['todate']

        search = ( (Match_history.objects.filter(player_a__player_name__contains=player) | Match_history.objects.filter(player_b__player_name__contains=player)) &
        Match_history.objects.filter(date__range=[fromdate, todate]) )

        context = {
            'title': 'Search',
            'search': search,
        }
        return render(request, 'aligulacv2/search.html', context)

    else:    
        players = Player_stats.objects.all()
        

        context = {
            'title': 'Search',
            'players': players,
        }
        return render(request, 'aligulacv2/search.html', context)
