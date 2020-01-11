from django.shortcuts import render
from django.http import HttpResponse
import pokebase as pb
from django.views import generic

# Create your views here.

def speed_checker(request):
    return HttpResponse("Hello")

class IndexView(generic.TemplateView):
    template_name = 'PokemonSpeedCheckerApp\pokedex.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pikachu = pb.pokemon(25)
        print(pikachu)
        context['pikachu'] = pikachu
        return context