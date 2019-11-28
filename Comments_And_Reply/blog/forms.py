from django import forms
from . models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('message',)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['message'].widget.attrs.update({'class':'form-control','rows':'3','cols':'10','placeholder':'Message'})