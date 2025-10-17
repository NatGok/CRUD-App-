from django.shortcuts import render, redirect
from noteapp.forms import NoteForm
from noteapp.model import Note


def note(request):
    # create instance for the form
    form = NoteForm()
    if request.method == "POST":
        form = NoteForm(request.POST)
        # save the modal instance if the form is valid
        if form.is_valid():
            form.save()
            # clearing the form data by redirecting to the root of the app
            return redirect('note-root')
    # get all note objects
    notes = Note.objects.all().order_by('id')
    return render(request, "index.html", {"form": form, "notes": notes})


def update_note(request, id):
    # get the instance
    instance = Note.objects.get(id=id)
    # initialise form instance with the note instance
    form = NoteForm(instance=instance)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=instance)
        # save the modal instance if the form is valid
        if form.is_valid():
            form.save()
            # refresh the page after save
            return redirect('note-root')
    return render(request, "index.html", {"form": form})


def delete_note(request, id):
    Note.objects.get(id=id).delete()
    return redirect('note-root')
