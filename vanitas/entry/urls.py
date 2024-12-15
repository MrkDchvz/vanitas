from django.urls import path
from . import views

app_name = 'entry'
urlpatterns = [
    path('', views.index, name='index'),
    path('/form', views.form, name='form'),
    path('<int:entry_id>/', views.detail, name='detail')
]
