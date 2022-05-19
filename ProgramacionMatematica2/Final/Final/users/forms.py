from django import forms

class formularioIngreso(forms.Form): # creacion del html, en base a 'signin.html'
    estados = forms.CharField(label="Estados", widget=forms.TextInput(attrs={'size':'200'}))
    transicion = forms.CharField(widget=forms.TextInput(attrs={'size':'200'}))
