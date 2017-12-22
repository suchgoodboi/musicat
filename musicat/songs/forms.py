from django import forms
from django.utils.translation import ugettext as _


from songs import models

# class SongForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         initial = kwargs.pop('initial', {})
#         kwargs['initial'] = initial
#         super(SongForm, self).__init__(*args, **kwargs)
#
#     class Meta:
#         model = models.Song
#         fields = ('name', 'group', 'description',
#                   'owner',)
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Выхода нет')}),
#             'group': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Сплин')}),
#             'description': forms.Textarea(attrs={'class': 'form-control',
#                                                  'placeholder': _(
#                                                      "Скоро рассвет,\n"
#                                                      "Выхода нет. \n"
#                                                      "Ключ поверни...")}),
#         }


class SongForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SongForm, self).__init__(*args, **kwargs)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Выхода нет')}),
            'group': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Сплин')}),
            'description': forms.Textarea(attrs={'class': 'form-control',
                                                 'placeholder': _(
                                                     "Скоро рассвет,\n"
                                                     "Выхода нет. \n"
                                                     "Ключ поверни...")}),
        }
        self.fields['name'].widget = widgets['name']
        self.fields['group'].widget = widgets['group']
        # self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget = widgets['description']
    class Meta:
        model = models.Song
        fields = ('name', 'group', 'description',)

    def save(self, commit=True):
        song = super(SongForm, self).save(commit=False)
        if commit:
            song.save()
        return song


    def clean_name(self):
        return self.cleaned_data['name'].title()


class SearchForm(forms.Form):
    
    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)

    def clean(self):

        cleaned_data = super(SearchForm, self).clean()

        if not any([cleaned_data['name'],
                    cleaned_data['group'],
                    cleaned_data['description']]):
            raise forms.ValidationError(_('You must select at least one filter'))
