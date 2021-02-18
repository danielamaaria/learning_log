from django import forms
from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


# We update the import statement to include Entry as well as Topic.
# We make a new class called EntryForm that inherits from forms.ModelForm.
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Entry:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
# A widget is an HTML form element, such as a single-line text box, multi-line text area, or drop-down list.
