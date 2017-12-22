from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.utils.translation import pgettext, ugettext as _
from django.views.decorators.http import require_POST
from django.views.generic import ListView, CreateView, \
    UpdateView, View

from songs import forms, models


class SongIndexView(ListView):
    template_name = 'songs/index.html'
    context_object_name = 'songs'

    def get_queryset(self):
        return models.Song.objects.select_related('group').order_by('-id')[:12]


def song_detail_view(request, pk_or_slug):
    song = models.Song.objects.filter(slug=pk_or_slug).first()

    if not song:
        try:
            song = models.Song.objects.get(pk=pk_or_slug)
        except ValueError:
            raise Http404()

    context = {
        'song': song,
        'current_url': request.build_absolute_uri(request.get_full_path()),
    }
    return render(request, 'songs/song_detail.html', context)


def paginate_songs(queryset, page, paginate_by=12):
    """Returns the Songs for the current requested page and the page number"""
    paginator = Paginator(queryset, paginate_by)

    try:
        songs = paginator.page(page)
        page = int(page)
    except PageNotAnInteger:
        songs = paginator.page(1)
        page = 1
    except EmptyPage:
        songs = paginator.page(paginator.num_pages)
        page = paginator.num_pages

    return songs, page


def render_song_list(request, queryset):
    songs, page = paginate_songs(queryset, request.GET.get('page'))

    return render(request, 'songs/song_list.html', {
        'songs': songs,
        'current_page': page
    })


class RegisterSongView(LoginRequiredMixin, CreateView):
    template_name = 'songs/addSong.html'
    model = models.Song
    form_class = forms.SongForm

    def get_success_url(self):
        return reverse('songs:registered', args=[self.object.id])

    def get(self, request, *args, **kwargs):
        if not request.user.is_information_confirmed:
            messages.warning(request, _('Please confirm your informations before registering a new song.'))
            return HttpResponseRedirect(reverse('users:edit'))
        else:
            print('здеся')
            return super(RegisterSongView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        #form.instance.owner = self.request.user
        return super(RegisterSongView, self).form_valid(form)


@require_POST
def delete_song(request, slug):
    song = get_object_or_404(models.Song, slug=slug)

    if request.user == song.owner:
        song.delete()
        return HttpResponseRedirect(reverse('songs:index'))

    return HttpResponseRedirect(song.get_absolute_url())


class SearchView(View):

    def get(self, request):
        return render(request, 'songs/search.html', {'form': SearchForm()})

    def post(self, request):
        form = SearchForm(request.POST)

        if not form.is_valid():
            return render(request, 'songs/search.html', {'form': form})

        query = self._build_query(form.cleaned_data)

        songs = models.Song.objects.actives().filter(query)
        return render(request, 'songs/search.html', {'form': form, 'songs': songs})

    @staticmethod
    def _build_query(cleaned_data):
        query = Q()

        for key, value in cleaned_data.items():
            if value:
                query &= Q(**{key: value})

        return query


def registered(request, slug):
    context = {
        'song_slug': slug,
    }
    return render(request, 'songs/registered.html', context)


def poster(request, slug):
    song = get_object_or_404(models.Song, slug=slug)
    return render(request, 'songs/post.html', {'song': song})


def update_register(request, request_key):
    song = get_object_or_404(models.Song, request_key=request_key)
    song.activate()
    return HttpResponseRedirect(song.get_absolute_url())
