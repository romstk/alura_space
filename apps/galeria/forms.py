from django import forms
from apps.galeria.models import Fotografia
class FotografiaForm(forms.ModelForm):
    #Dentro desta classe de formulário vou inserir outra classe com os matadados da model que irei utilizar para criar o form. 
    class Meta: 
        model = Fotografia
        exclude = ['publicada',] #este atributo refere-se aos fields da model que não quero incluir no formulário
        labels = {
            'descricao' : "Descrição",
            'data_fotografia' : 'Data de registro',
            'usuario' : 'Usuário'
        }
        widgets = {
            'nome' : forms.TextInput(attrs={'class':'form-control'}),
            'legenda' : forms.TextInput(attrs={'class':'form-control'}),
            'categoria' : forms.Select(attrs={'class':'form-control'}),
            'descricao' : forms.Textarea(attrs={'class':'form-control'}),
            'foto' : forms.FileInput(attrs={'class':'form-control'}),
            'data_fotografia' : forms.DateInput(
                format = '%d/%m/%y',
                attrs={
                    'type':'date',
                    'class':'form-control'
                    }),
            'usuario' : forms.Select(attrs={'class':'form-control'}),
        }




     
