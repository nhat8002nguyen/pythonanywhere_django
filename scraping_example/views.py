from django.shortcuts import render
from .forms import FileFormatSelectForm
from django.http import HttpResponse, HttpResponseRedirect
from .scraper import start_process_scraping, fake_download_process
from threading import Thread
import time


def get_file_format(request):
    if request.method == "POST":
        return HttpResponseRedirect(f"{request.path}download/")

    return render(request, "scraping_example/choices.html")

def download_file(request):
    return start_process_scraping()
    



