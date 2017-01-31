from django.shortcuts import render
from collection.models import Thing

# Create your views here.
def index(request):
	#defining the variable
	things= Thing.objects.all()
	#this is your new view
	return render(request, 'index.html', {
		'things': things,
	})