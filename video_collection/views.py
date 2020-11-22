from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from .forms import VideoForm
from .models import Video


def home(r):
    app_name = 'Horse Videos'
    return render(r, 'video_collection/home.html', {'app_name': app_name})


def add(r):
    if r.method == 'POST':
        new_video_form = VideoForm(r.POST)
        if new_video_form.is_valid():
            try:
                new_video_form.save()
                return redirect('video_list')
            except ValidationError:
                messages.warning(r, 'Invalid YouTube URL')
            except IntegrityError:
                messages.warning(r, 'Video already added')
        messages.info(r, 'Please check the data entered.')
        return render(r, 'video_collection/add.html', {'new_video_form': new_video_form})
    new_video_form = VideoForm()
    return render(r, 'video_collection/add.html', {'new_video_form': new_video_form})


def video_list(r):
    videos = Video.objects.all()
    return render(r, 'video_collection/video_list.html', {'videos': videos})
