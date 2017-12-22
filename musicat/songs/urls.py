from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.SongIndexView.as_view(), name='index'),
    url(r'^newsong/$', views.RegisterSongView.as_view(), name='register'),
    url(r'^update/(?P<request_key>\w+)/$', views.update_register, name='update_register'),
    url(r'^group/(?P<sign>\w)/$', views.update_register, name='update_register'),
    url(r'^(?P<slug>[-\w]*)/post/$', views.poster, name='poster'),
    url(r'^(?P<slug>[-\w]*)/deletesong/$', views.delete_song, name='delete_song'),
    url(r'^(?P<slug>[-\w]*)/registrado/$', views.registered, name='registered'),

    url(r'^(?P<pk_or_slug>[-\w]*)/$', views.song_detail_view, name='detail'),
    url(r'^(?P<pk>[0-9]+)/$', views.song_detail_view, name='detail_by_pk'),
]