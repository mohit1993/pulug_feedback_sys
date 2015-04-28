from django.contrib import admin
from feedback.models import WebDevSeminar2Feedback

class WebDev2FormAuthor(admin.ModelAdmin):
   list_display = ('name','email','college','branch','degree_year','contact','feedback')  

admin.site.register(WebDevSeminar2Feedback,WebDev2FormAuthor)
