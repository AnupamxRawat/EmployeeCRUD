
from django.urls import path
from . import views

urlpatterns = [
    path('', views.emp_form,name='emp_insert'),
    path('<int:id>/', views.emp_form,name='emp_update'),
    path('list/',views.emp_list,name='emp_all' ),
    path('delete/<int:id>/',views.delete,name='emp_delete' ),

    

]