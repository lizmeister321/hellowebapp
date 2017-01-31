from django.shortcuts import render, redirect
from collection.models import Thing

# Create your views here.
def index(request):
	#defining the variable
	things= Thing.objects.all()
	#this is your new view
	return render(request, 'index.html', {
		'things': things,
	})

def thing_detail(request, slug):

	thing = Thing.objects.get(slug=slug)
	return render(request, 'things/thing_detail.html', {'thing': thing,
		})