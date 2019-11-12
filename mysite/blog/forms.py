from django import forms
from .models import Comment

# We still need to build a form to let our users comment on blog posts. \
# Remember that Django has two base classes to build forms: Form and ModelForm.
# You used the first one previously to let your users share posts by e-mail.
# In the present case, you will need to use ModelForm because you have to
# build a form dynamically from your Comment model.

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()#限定email格式
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)#可不填

#引用Model.Comment當表單,ModelForm.
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')#只留3個欄位
