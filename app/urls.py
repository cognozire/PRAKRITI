from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path("index.html",views.index,name = "index"),
    path("dosh.html",views.dosh,name = "dosh"),
    path("diseases.html",views.disease,name = "diseases"),
    path("diet.html",views.diet,name='diet'),
    path("result",views.result,name = 'result'),
    path("result2",views.result2,name='result2'),
    path("result3",views.result3,name='result3'),
    path("asana.html",views.asana,name='asana'),
    path("y_asana.html",views.y_asana,name='y_asana'),
    path("anasa1.html",views.anasa1,name='anasa1')
]
