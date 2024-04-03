from django.urls import path
from .views import HomeTemplateView, AppointmentTemplateView, ManageAppointmentTemplateView,DeleteAppointmentTemplateView,UpdateDateView,login_view

urlpatterns = [
    path("", HomeTemplateView.as_view(), name="home"),
    path("make-an-appointment/", AppointmentTemplateView.as_view(), name="appointment"),
    path("manage-appointments/", ManageAppointmentTemplateView.as_view(), name="manage"),
    path("delete-appointments/", DeleteAppointmentTemplateView.as_view(), name="delete_appointment"),
    path("update-date/", UpdateDateView.as_view(), name="update_date"),
    path('login/', login_view, name='login'),
]
