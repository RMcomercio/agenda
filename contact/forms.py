from django import forms
from django.core.exceptions import ValidationError
from . import models
from django.contrib.auth.forms import UserCreationForm

class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget = forms.FileInput(
            attrs={
                'accept': 'image/*', 
            }
        )
    )
    #pegou o campo do models e personalizou ele.
    # first_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'class':'classe-a classe-b',
    #             'placeholder':'campo novo no formulario',
    #         }
    #     ),
    #     label='Primeiro Nome',
    #     help_text='um texto de ajuda a ser exibido no formulario',
    # )
    # Novo = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'class':'classe-a classe-b',
    #             'placeholder':'campo novo no formulario'
    #         }
    #     ),
       
    #     help_text='testando campo',
    # )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields['first_name'].widget.attrs.update({
        #     'class':'classe-a classe-b',
        #     'placeholder':'veio do init'
        # })
    class Meta:
        model = models.Contact
        fields = (
            'first_name',
            'last_name',
            'phone',
            'email',
            'description',
            'category',
            'picture',


        )
        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'class':'classe-a classe-b',
        #             'placeholder':'Escreva aqui'
        #         }
        #     )
        # }

    def clean(self):
        cleaned_data = self.cleaned_data
       
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        
        if first_name ==last_name:
            msg = ValidationError(
                'Primeiro nome deve ser diferente do segundo nome',
                code='invalid'
            )
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)


            # self.add_error(
            #     'first_name',
            #     ValidationError(
            #         'MEnsagem de erro',
            #         code='invalid'
            #     )
            # )  
        return super().clean()

    def clean_first_name(self):
        cleaned_data = self.cleaned_data.get('first_name')
        
        if cleaned_data =='ABC':
            self.add_error('first_name', ValidationError(
                'Nao digite ABC neste Campo',
                code='invalid'
                )
            )

        return cleaned_data

class RegisterForm(UserCreationForm):
    ...
