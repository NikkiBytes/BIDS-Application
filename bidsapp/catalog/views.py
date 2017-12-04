from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView, FormView

# created views below 


class HomeView(TemplateView):
    template_name = 'index.html'

class OsirixView(FormView):

    template_name = 'osiripage.html'
    form_class OsirixForm
    success_url = '/success/'

    def form_valid(self, form):
        form.get_data()
        return super(OsirixView, self).form_valid(form)

