from .models import Post
from django import forms


class AddPost(forms.ModelForm):

    image = forms.ImageField()
    class Meta:
        model = Post
        fields = ['body', 'image',]

        widget = {
            'body': forms.Textarea(attrs={"placeholder": "Message", "class": "form-control",})
        }
