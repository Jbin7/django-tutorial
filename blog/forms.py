from django import forms

from .models import Post

# form
# class PostForm(forms.Form):
# 	title = forms.CharField(widget=forms.TextInput(
#         attrs={
#             'placeholder': '제목 입력'
#         }
#     ))
#
# 	text = forms.CharField(widget=forms.Textarea(
#         attrs={
#             'placeholder': '내용 입력'
#         }
#     ))


# model form
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')
        widgets = {
            'text': forms.Textarea(
                attrs={'placeholder': '내용입력'}
            )
        }