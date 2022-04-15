"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from lycee import views
from lycee.views import StudentCreateView
from lycee.views import StudentCallOfRollParticularForm
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('lycee', views.index, name='index'),
    path('lycee/<int:cursus_id>', views.liste_student, name ='liste_student'),
    path('lycee/student/<int:student_id>', views.detail_student, name='detail_student'),
    path('lycee/student/create', StudentCreateView.as_view(), name='create_student'),
    path('lycee/student/edit/<int:student_id>', views.edit_student, name='edit_student'),
    path('lycee/call/1', StudentCallOfRollParticularForm.as_view(), name='call_of_roll_particular'),
    path('lycee/cursuscall/<int:cursus_id>', views.call_of_roll, name='call_of_roll'),
]