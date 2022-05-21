from django.shortcuts import render, redirect
# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from .models import Cursus, Student, Presence, TimeSlot
from django.template import loader
from django.views.generic.edit import CreateView
from .forms import StudentForm, StudentCallOfRollParticularForm
from django.urls import reverse
import logging

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
  return redirect("index")
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

  if request.method == 'POST':
    students = request.POST.getlist("student")
    students_map = map(int, students)
    students_int = list(students_map)
    date = request.POST["date"]
    start = request.POST["time_start"]
    end = request.POST["time_end"]
    status = 0
    for v in students_int:
      students_presence = Presence.objects.create(
        reason="Absent",
        isMissing=True,
        date=date,
        student_id=v,
      )
      students_presence.save()
      timeslot_student = TimeSlot.objects.create(
        start_time=start,
        stop_time=end,
        presence_id=students_presence.id,
        cursus_id=cursus_id
      )
      timeslot_student.save()
    return redirect("index")

  context = {
    'liste': result_list,
    'cursus': result_cursus
  }

  return render(request,'lycee/cursuscall/call_of_roll.html', context)
def appeal_view(request):

  date = "ok"
  time_end="ok"
  time_start="ok"
  cursus="ok"
  result_list = []
  count_list = []

  #For each cursus

  list = TimeSlot.objects.all().order_by('cursus_id')
  #list_student = Presence.objects.all().order_by('date')

  for v in list:
    result_presence = Presence.objects.get(pk=v.presence_id)
    if v.cursus_id != cursus or v.start_time != time_start or v.stop_time != time_end or result_presence.date != date:
      result_list.append(v)
      count_list.append(v.cursus_id)
    date = result_presence.date
    time_start = v.start_time
    time_end = v.stop_time
    cursus = v.cursus_id




  context = {'liste': result_list,
             'liste_counting' : count_list}
  return render(request, 'lycee/appeal/appeal_resume.html', context)

def detail_missing(request):
  return render(request, 'lycee/appeal/appeal_resume.html')


