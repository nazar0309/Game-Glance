from django.shortcuts import render
from .forms import CollaborateForm
from django.contrib import messages

def about_view(request):

    if request.method == "POST":
        print('Getting the POST request...')
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )
            
    collaborate_form = CollaborateForm()
    print('Rendering template...')
    return render(
        request,
        "about/about.html",
         {
        "collaborate_form": collaborate_form,
        },
    )
