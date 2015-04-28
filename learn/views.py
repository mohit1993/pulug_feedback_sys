from django.shortcuts import render
from django.core.urlresolvers import reverse
from learn.models import Sample
from django.views.generic import CreateView,ListView


class SampleView(CreateView):

   model = Sample
   template_name = 'sample.html'

   def get_sucess_url(self):
      return reverse('suc')

class SuccessView(ListView):
   model = Sample
   template_name = 'successt.html'
