from django import forms
from django.core.exceptions import ValidationError
from .models import Note, Comment


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = [
            'title',
            'body',
        ]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'body'
        ]        


class ContactForm(forms.Form):
    email = forms.EmailField(required=True)
    title = forms.CharField(required=True, max_length=255)
    body = forms.CharField(label="Your message", widget=forms.Textarea(attrs={'required': True}))


class SearchForm(forms.Form):
    ORDER_CHOICES = (
        ("title", "title"),
        ("body", "body"),
    )

    # Form fields
    title = forms.CharField(max_length=255, required=True)
    order_by = forms.ChoiceField(choices=ORDER_CHOICES, widget=forms.RadioSelect, required=True)