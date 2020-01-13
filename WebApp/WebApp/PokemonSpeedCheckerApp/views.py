from django.shortcuts import render
from django.http import HttpResponse
import pokebase as pb
from django.views import generic
import PokemonSpeedCheckerApp.models

# Create your views here.

def speed_checker(request):
    return HttpResponse("Hello")

class IndexView(generic.TemplateView):
    template_name = 'PokemonSpeedCheckerApp\pokedex.html'

    def set_param(self, context, name):
        pokemon = PokemonSpeedCheckerApp.models.Pokemon()
        pokemon.speed = context[name].name
        print(pokemon.speed)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pikachu = pb.pokemon(25)
        print(pikachu)
        context['pikachu'] = pikachu
        self.set_param(context, 'pikachu')
        return context

