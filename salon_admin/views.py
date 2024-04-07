from decouple import config
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.core.mail import EmailMessage, message
from django.conf import settings
from django.contrib import messages
from .models import Appointment
from django.views.generic import ListView
import datetime
from django.template import Context
from django.template.loader import render_to_string, get_template
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def index(request):
    google_maps_api_key = config('GOOGLE_MAPS_API_KEY')
    return render(request, 'index.html', {'google_maps_api_key': google_maps_api_key})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            # Redirect to some page after successful login
            return redirect('manage')
        else:
            # Invalid credentials
            return render(request, 'login.html', {'error_message': 'Invalid credentials'})
    else:
        return render(request, 'login.html')

class HomeTemplateView(TemplateView):
    template_name = "index.html"
    
    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        email = EmailMessage(
            subject= f"{name} from salon connect family.",
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.EMAIL_HOST_USER],
            reply_to=[email]
        )
        email.send()
        return HttpResponse("Email sent successfully!")


class AppointmentTemplateView(TemplateView):
    template_name = "appointment.html"

    def post(self, request):
        fname = request.POST.get("fname")
        lname = request.POST.get("fname")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        message = request.POST.get("request")
        date = request.POST.get("date") 

        appointment = Appointment.objects.create(
            first_name=fname,
            last_name=lname,
            email=email,
            phone=mobile,
            request=message,
            req_date=date,
        )

        appointment.save()

        messages.add_message(request, messages.SUCCESS, f"Thanks {fname} for making an appointment, we will email you ASAP!")
        return HttpResponseRedirect(request.path)

class ManageAppointmentTemplateView(ListView):
    template_name = "manage-appointments.html"
    model = Appointment
    context_object_name = "appointments"
    login_required = True
    paginate_by = 3


    def post(self, request):
    
        date = request.POST.get("date")
        appointment_id = request.POST.get("appointment-id")
        appointment = Appointment.objects.get(id=appointment_id)
        appointment.accepted = True
        appointment.accepted_date = datetime.datetime.now()
        if(date != None):
            appointment.req_date=date
        appointment.save()

        data = {
            "fname":appointment.first_name,
            "date":date,
        }

        messages.add_message(request, messages.SUCCESS, f"You accepted the appointment of {appointment.first_name}")
        return HttpResponseRedirect(request.path)

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        appointments = Appointment.objects.all()
        context.update({   
            "title":"Manage Appointments"
        })
        return context
    
class DeleteAppointmentTemplateView(ListView):
    template_name = "manage-appointments.html"
    model = Appointment
    context_object_name = "appointments"
    login_required = True
    paginate_by = 3

    def post(self, request):
        if(request.POST.get("action")=="delete"):
            print("helllllllllll")
            appointment_id = request.POST.get("appointment-id")
            appointment = Appointment.objects.get(id=appointment_id)
            appointment.delete()
            messages.add_message(request, messages.SUCCESS, "Appointment deleted successfully!")
            return HttpResponseRedirect(request.path)

class UpdateDateView(ListView):
    def post(self, request):
        appointment_id = request.POST.get("appointment-id")
        new_date = request.POST.get("new-date")
        
        try:
            appointment = Appointment.objects.get(id=appointment_id)
            appointment.req_date = new_date
            appointment.accepted = True  # Mark appointment as accepted
            appointment.save()
            # You can add a success message here if needed
        except Appointment.DoesNotExist:
            # Handle the case where the appointment with the given ID doesn't exist
            pass
        
        return HttpResponseRedirect(request.path)
    