# Create your views here.
from academic.models import user
from django.shortcuts import render_to_response

def usuario(request):
    users = user.objects.all()
    return render_to_response('usuario.html',{'lista':users})