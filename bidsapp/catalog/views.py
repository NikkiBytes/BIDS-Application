
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView, FormView

# created views below 


class HomeView(TemplateView):
    template_name = 'base.html'

class OsirixView(TemplateView):

    template_name = "osirixpage.html"



