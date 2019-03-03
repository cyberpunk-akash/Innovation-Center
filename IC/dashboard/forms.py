from django import forms
from dashboard.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('admin_name','dept','description')

        def __init__(self,*args,**kwargs):
            self.startup_name=kwargs.pop("user",None)
            super().__init__(*args,**kwargs)
