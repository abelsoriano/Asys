
from django.forms import *
from django import forms
from app.models import *
from django_select2.forms import ModelSelect2Widget, ModelSelect2MultipleWidget



# Create Miembro
class MemberForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Miembro
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese un nombre'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su apellido'}),
            'dni': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su numero de identidad'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'date_joined': DateInput(format='%d/%m/%Y',
                                     attrs={'class': 'form-control datepicker', 'placeholder': 'mm/dd/yyyy'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Direccion'}),
            'fecha_ingreso': DateInput(format='%d/%m/%Y', attrs={'class': 'form-control datepicker', 'placeholder': 'mm/dd/yyyy'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese sin guión'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
            'cargo': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'})
        }


    def clean_dni(self):
        dni = self.cleaned_data.get('dni')
        if len(dni) != 13 or not dni.replace("-", "").isdigit():
            raise forms.ValidationError("El DNI debe tener el formato 000-0000000-0 y contener 11 números.")
        return dni

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if len(phone) != 12 or not phone.replace("-", "").isdigit():
            raise forms.ValidationError("El teléfono debe tener el formato 000-000-0000 y contener 10 números.")
        return phone

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


# Formulario para crear servicio
class PersonaWidget(ModelSelect2Widget):
    search_fields = [
        'nombre__icontains',
    ]
class ServicioForm(ModelForm):
    class Meta:
        model = Servicio
        fields = '__all__'
        widgets = {
            'fecha': DateInput(
                format='%d/%m/%Y',
                attrs={'autocomplete': 'off', 'id': 'datepicker2', 'class': 'form-control datepicker', 'placeholder': 'dd/mm/yyyy'}),
            'direccion': TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Ingrese un nombre'}),
            'lectura': TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Ingrese la lectura'}),
            'devocional': TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Ingrese un libro'}),
            'cultural_1': forms.Select(attrs={'class': 'form-control'}),
            'participantes': ModelSelect2MultipleWidget(model=Persona, search_fields=['nombre__icontains'], attrs={'class': 'form-control', 'placeholder': 'Ingrese una dirección'}),
            'cultural': TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Ingrese un cultural'}),
            'mensaje': TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Ingrese el mensaje'}),
            'ofrenda': forms.NumberInput(attrs={'type': 'text', 'class': 'money-input form-control', 'step': '0.01', 'min': '0', 'placeholder': 'Ingrese un valor'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'opcional', 'rows': 3, 'style': 'resize:none;'}),
        }

    def __init__(self, *args, **kwargs):
        super(ServicioForm, self).__init__(*args, **kwargs)
        self.fields['participantes'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ingrese una dirección'
        })

    def clean_participantes(self):
        participantes = self.cleaned_data.get('participantes')
        if participantes.count() > 3:
            raise forms.ValidationError('Solo puede seleccionar hasta 3 participantes.')
        return participantes

    def save(self, commit=True):
        form = super(ServicioForm, self).save(commit=False)
        data = {}
        if commit:
            form.save()
            self.save_m2m()
        return data

class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['miembro', 'date', 'present']

class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['titulo', 'contenido']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el título'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese el contenido'}),
        }
