from django.shortcuts import render
from django.views.generic import (View, TemplateView, ListView)
from . import models
# Create your views here.

class NflIndexView(TemplateView):
    # context_object_name = 'passing_yards'
    model = models.Player
    template_name = 'nfl_stats/nfl_index.html'
    # def get_context_data(self,**kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['tag'] = Player.passing_yards
