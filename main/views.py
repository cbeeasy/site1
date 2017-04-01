from datetime import datetime
from django.shortcuts import render

def date_actuelle(request):
    return render(request, 'date.html', {'date': datetime.now()})

def home(request):
	return render(request, 'base.html', {'date': datetime.now()})


