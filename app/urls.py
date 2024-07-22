from django.urls import path, include

from app.views.asistencia import views
from app.views.asistencia.views import *
from app.views.notas.views import *
from app.views.persona.views import *
from app.views.servicio.views import *

app_name = 'asys'

urlpatterns = [
    # path('get_inattendance_count/', views.get_inattendance_count, name='get_inattendance_count'),
    path('persona/list/', MembersListView.as_view(), name='miembro_list'),
    path('persona/add/', MembersCreate.as_view(), name='members_create'),
    path('persona/edit/<int:pk>/', MembersUpdate.as_view(), name='members_update'),
    path('persona/delete/<int:pk>/', MembersDelete.as_view(), name='members_delete'),

    # Url page Servico
    path('servicio/create/', login_required(ServicioCreateView.as_view()), name='servicio_create'),
    path('add-persona/', add_persona, name='add_persona'),
    path('servicio/list/', ServicioListView.as_view(), name='service_list'),
    path('service/edit/<int:pk>/', ServiceUpdate.as_view(), name='service_update'),
    path('service/delete/<int:pk>/', ServiceDelete.as_view(), name='service_delete'),

    # Url page Asistencia
    path('crear-asistencia/', AttendanceCreateView.as_view(), name='crear_asistencia'),
    path('lista-asistencia/', AttendanceList.as_view(), name='list_asistencia'),
    path('details/', AttendanceDetailsView.as_view(), name='details_asistencia'),
    path('guardar-status/', views.guardar_status, name='guardar_status'),
    path('asistencia/edit/<int:pk>/', AttendaceUpdate.as_view(), name='asistencia_update'),

    path('notas/list', NotaView.as_view(), name='nota_list'),
    path('notas/delete/<int:pk>/', NotaDeleteView.as_view(), name='nota_delete'),
    path('notas/cargar_mas/', cargar_mas_notas, name='cargar_mas_notas'),
    path('notas/update/<int:pk>/', NotaUpdateView.as_view(), name='nota_update'),


    # urls.py
    #     path('attendance/json/<str:date>/', AttendanceJsonDetail.as_view(), name='attendance_json'),
    #     path('lista-asistencia2/', AsistenciaDataTable.as_view(), name='list_asistencia2'),

]
