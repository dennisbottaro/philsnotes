from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from .models import Job, JobNote, Builder
from .forms import JobNoteForm, JobForm, BuilderForm


# Create your views here.
def joblist(request):
    # dump name sorted list of jobs
    jobs = Job.objects.all().order_by('job_name')
    return render(request, 'joblist.html', {'jobs': jobs})


def builder_list(request):
    builders = Builder.objects.all()
    return render(request, 'builderlist.html', {'builders': builders})


def jobnotes(request, job_id):
    # job = Job.objects.get(pk=job_id)
    job = get_object_or_404(Job, pk=job_id)
    jobnotes = JobNote.objects.filter(job=job).order_by('-note_date')

    noteform = JobNoteForm()

    return render(request, 'jobnotes.html', {'noteform': noteform, 'job': job, 'jobnotes': jobnotes})


def savenote(request, job_id):
    # get form data...  new stuff for me.. LOL

    if request.method == "POST":
        form = JobNoteForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.job_id = job_id
            model_instance.save()
            return redirect('/')


def jobedit(request, pk):
    job = get_object_or_404(Job, pk=pk)

    form = JobForm(request.POST or None, instance=job)

    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, 'jobform.html', {'jobform': form})


def builder_edit(request, pk):
    builder = get_object_or_404(Builder, pk=pk)

    form = BuilderForm(request.POST or None, instance=builder)

    if form.is_valid():
        form.save()
        return redirect('/builders/')

    return render(request, 'builderform.html', {'builderform': form})


def jobdelete(request, pk):
    job = get_object_or_404(Job, pk=pk)

    if request.method == 'POST':
        job.delete()
        return redirect('/')
    return render(request, 'jobdelete.html', {'object': job})


def builder_delete(request, pk):
    builder = get_object_or_404(Builder, pk=pk)
    if request.method == 'POST':
        builder.delete()
        return redirect('/builders/')
    return render(request, 'builderdelete.html', {'object': builder})


def jobadd(request, template_name='jobform.html'):
    form = JobForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, template_name, {'jobform': form})


def builder_add(request, template_name='builderform.html'):
    form = BuilderForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/builders/')
    return render(request, template_name, {'builderform': form})
