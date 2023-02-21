from django.shortcuts import render, redirect
from . models import *
# Create your views here.
def home(request):
    notes = Notes.objects.filter(status = True)
    context = {
        'notes' : notes
    }
    return render(request,'main/realHome.html',context)

def addNotes(request):
    subj = Subject.objects.all()
    mod = Module.objects.all()
    context = {
        'mod' : mod,
        'subj' : subj,
    }

    if request.method == 'POST':

        title = request.POST.get('title')
        sub = request.POST.get('sub')
        file = request.FILES.get('file')


        note = Notes(
            name = title,
            mod = sub,
            file = file,
            author = request.user
        )

        note.save()

        return redirect('home')

    return render(request,'main/addNotes.html',context)

def notes(request):
    notes = Notes.objects.all()
    context = {
        'notes' : notes
    }
    return render(request,'main/realHome.html',context)

def status(request):

    notes = Notes.objects.filter(author = request.user)
    context = {
        'notes' : notes,
    }

    return render(request,'main/status.html',context)

def noteDelete(request,slug):

    notes = Notes.objects.filter(slug = slug)
    notes.delete()

    return redirect('status')