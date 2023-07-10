from django import forms
from django.core import validators

class FormArticle(forms.Form):

    title = forms.CharField(
        label = "Titulo",
        max_length=50,
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese el Titulo',
                'class':'titulo_form_article'
            }
        ),
        validators=[
            validators.MinLengthValidator (4,'El titulo es demasiado corto'),
            validators.RegexValidator ('^[A-Za-z0-9ñ ]*$', 'El titulo esta mal formado','invalid_title')
        ]
    )
    content = forms.CharField(
        label = "Contenido",
        widget=forms.Textarea,
        validators=[
            validators.MaxLengthValidator(60,'Has colocado mucho texto')
        ]
    )
    
    content.widget.attrs.update({
        'placeholder': 'Ingrese el Contenido',
        'class':'contenido_form_article',
        'id':'contenido_form'
    })
    public_options = [
       (1,'Si'),
       (0,'No')
   ]
    public = forms.TypedChoiceField(
        label="¿Publicado?",
       choices = public_options
   )