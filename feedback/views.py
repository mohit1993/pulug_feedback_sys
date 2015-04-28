from django.shortcuts import render
from django.http import request
from django.core.urlresolvers import reverse
from django.views.generic import CreateView,TemplateView,View
from feedback.models import WebDevSeminar2Feedback
from django.contrib import sessions
#import urllib2
#import urllib
import feedback.feedback_form 

class WebDevFeedbackFormView(CreateView):
   
   model = WebDevSeminar2Feedback;
   template_name = "webdevfeedbackform.html"
   form_class = feedback.feedback_form.FeedbackForm 
   #name = object.name   
   def get_success_url(self):
      return reverse("success")
   
   #def post(self,request):
    #  return render(request,"success.html",{'name':request.POST['name']})
 
    
      
class SuccessView(TemplateView):
   model = WebDevSeminar2Feedback
   template_name = "success.html"

class WelcomeView(View):
   def get(self,request):
      return render(request,"welcome.html")
     
