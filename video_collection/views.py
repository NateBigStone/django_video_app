from django.shortcuts import render
from django.contrib import messages
from .forms import VideoForm


def home(r):
    app_name = 'Horse Videos'
    return render(r, 'video_collection/home.html', {'app_name': app_name})


def add(r):
    if r.method == 'POST':
        new_video_form = VideoForm(r.POST)
        if new_video_form.is_valid():
            new_video_form.save()
            messages.info(r, 'New video saved!')
            # TODO: show success message
        else:
            messages.info(r, 'Please check the data entered.')
            return render(r, 'video_collection/add.html', {'new_video_form': new_video_form})
    new_video_form = VideoForm()
    return render(r, 'video_collection/add.html', {'new_video_form': new_video_form})
