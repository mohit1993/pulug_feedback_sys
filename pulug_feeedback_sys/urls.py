from django.conf.urls import patterns, include, url
from django.contrib import admin
import feedback.views
import learn.views
urlpatterns = patterns('',
    # Examples:
    url(r'^$', feedback.views.WelcomeView.as_view(), name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^form$',feedback.views.WebDevFeedbackFormView.as_view(),name = "webdevform"),
    url(r'^success$',feedback.views.SuccessView.as_view(),name = "success"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^learnform$',learn.views.SampleView.as_view(),name='sampleform'),
    url(r'^successed$',learn.views.SuccessView.as_view(),name='suc'),
)
