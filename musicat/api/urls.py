from django.conf.urls import url

from api import views

urlpatterns = [
    url(r'^songs/$', views.ListSongs.as_view(), name='list_songs'),
    url(r'^groups/$', views.GroupList.as_view(), name='list_groups'),
]
