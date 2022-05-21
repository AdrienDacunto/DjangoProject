from django.forms.models import ModelForm
from .models import Student, Presence

class StudentForm(ModelForm):

    class Meta:
        #Le model auquel on se refere
        model= Student

        #Les champs qu'on veut voir apparaitre dans le formulaire
        fields = (
            "first_name",
            "last_name",
            "birth_date",
            "email",
            "phone",
            "comments",
            "cursus",
        )
class StudentCallOfRollParticularForm(ModelForm):
    class Meta:
        #Le model auquel on se refere
        model = Presence

        #Les champs qu'on peut voir apparaitre dans le formulaire
        fields = (
            "reason",
            "isMissing",
            "date",
            "student"
        )