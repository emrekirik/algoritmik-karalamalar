from django.shortcuts import render
from django.utils import timezone
from .models import Gonderi


def gonderi_listesi(request):
    gonderiler= Gonderi.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
    return render(request, 'blog/gonderi_listesi.html', {'gonderiler':gonderiler})

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")