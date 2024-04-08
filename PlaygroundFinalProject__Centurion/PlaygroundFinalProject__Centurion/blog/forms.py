from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) > 200:
            raise forms.ValidationError("El contenido del posteo no puede exceder los 200 caracteres.")
        return content
