from django.urls import path
from . import views

app_name = 'entry'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_entry', views.add_entry, name='add_entry'),
    path('<int:entry_id>/', views.detail, name='detail')
]
