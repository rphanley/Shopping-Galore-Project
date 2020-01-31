from django.conf.urls import url
from .views import feedback_form

 
urlpatterns = [
      url(r'^(?P<id>)', feedback_form, name='feedback_form'),
]
