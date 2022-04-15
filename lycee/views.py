from django.shortcuts import render, redirect
# Create your views here.

from django.http import HttpResponse
from .models import Cursus, Student, Presence
from django.template import loader
from django.views.generic.edit import CreateView
from .forms import StudentForm, StudentCallOfRollParticularForm
from django.urls import reverse

class StudentCreateView(CreateView):
  #Le modele auquel on se refere
  model = Student
  #Le formulaire associe (dans form.py)
  form_class = StudentForm
  #le nom du template
  template_name = 'lycee/student/create.html'

  #page appelee si creation ok
  def get_success_url(self):
    return reverse ("detail_student", args=(self.object.pk,))
def home(request):
  return HttpResponse("Home")
def index(request):
  result_list = Cursus.objects.order_by('name')
  # chargement du template
  template = loader.get_template('lycee/index.html')

  #context
  context = {
    'liste' : result_list,
  }
  return HttpResponse(template.render(context, request))
def liste_student(request, cursus_id):
  #resp= 'result for cursus {}'.format(cursus_id)
  #return HttpResponse(resp)
  result_list = Student.objects.filter(cursus_id=cursus_id)

  context = { 'liste' : result_list}

  return render( request,'lycee/student/liste_student.html', context)

def detail_student(request, student_id):
  result_list = Student.objects.get(pk=student_id)

  context = {'liste': result_list}

  return render(request, 'lycee/student/detail_student.html', context)

def edit_student(request, student_id):
  result = Student.objects.get(pk=student_id)

  if request.method == 'POST':
    form = StudentForm(request.POST,instance=result)
    if form.is_valid():
        form.save()
        return redirect('detail_student', student_id)
  else:
    form = StudentForm(instance=result)

  return render(request, 'lycee/student/edit/edit_student.html',{'form': form})

class StudentCallOfRollParticularForm(CreateView):
  #Le model auquel on se refere
  model = Presence
  #Le model associe (dans forms.py)
  form_class= StudentCallOfRollParticularForm
  #le nom du template
  template_name= 'lycee/call/call_of_roll_particular.html'

  #page appelee si creation ok
  def get_success_url(self):
    return reverse("index")

def call_of_roll(request, cursus_id):
  result_list = Student.objects.filter(cursus_id=cursus_id)
  result_cursus = Cursus.objects.get(pk=cursus_id)

  context = {
    'liste': result_list,
    'cursus': result_cursus
  }

  return render(request,'lycee/cursuscall/call_of_roll.html', context)