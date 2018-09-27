from django import forms  

class formulario(forms.Form):
    title=forms.CharField(label='Your name',required=True, min_length=5)
    description=forms.CharField(label='Your description', required=True, widget=forms.Textarea(), min_length=10)
    link = forms.URLField(label='Your website', required=True)
    image = forms.ImageField(label='Image:',required=True)

