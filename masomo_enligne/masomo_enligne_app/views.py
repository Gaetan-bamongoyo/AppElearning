from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def IndexPage(request):
    personne = Personne.objects.all()
    context = {
        'personne':personne
    }
    template = 'index.html'
    return render(request, template, context)

# create
def CreatePersonne(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        postnom = request.POST.get('postnom')
        form = Personne(
            nom=nom,
            postnom=postnom
        )
        form.save()
        return redirect('app:index')

