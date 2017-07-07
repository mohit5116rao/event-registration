from django.conf.urls import url

from .views import register_new,register_list

urlpatterns = [
    url(r'^new/', register_new, name='new'),
    url(r'^list/', register_list, name='list'),

]
