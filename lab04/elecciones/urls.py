from django.urls import path
from . import views
app_name = 'elecciones'

urlpatterns=[
    #ex: /elecciones/
    path('', views.index, name='index'),
    #ex: /elecciones/5/
    path('<int:region_id>/',views.detalle, name='detalle'),
    #ex: /elecciones/5/detcandidatos
    path('detCandidato/<int:candidato_id>',views.detCandidato, name='detCandidato'),

   
]