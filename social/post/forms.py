from .models import Post
from django import forms


class AddPost(forms.ModelForm):

    image = forms.ImageField(label="Enter a Snap", required=False)
    body = forms.CharField(widget=forms.Textarea(attrs={"placeholder": 'Message...',"class": "form-control", 'rows': 5, 'cols': 10}))
    class Meta:
        model = Post
        fields = ['body', 'image', ]
