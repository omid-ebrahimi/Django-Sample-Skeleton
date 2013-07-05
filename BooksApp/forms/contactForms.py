from django import forms

class SignupForm(forms.Form):
    subject = forms.CharField(max_length=100, label='Subject: ')
    email = forms.EmailField(required=False, label='Your e-mail address: ')
    message = forms.CharField(widget=forms.Textarea, label='Message: ')

    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("Not enough words!")
        return message
