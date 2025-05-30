from .models import DestinosTuristicos

class DestinoForm(forms.ModelForm):
    class Meta:
        model = DestinosTuristicos
        fields = '__all__'
