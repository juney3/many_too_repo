from django.shortcuts import render, redirect

from models import User, Interest

# Create your views here.
def index(request):
	return render(request, 'many/index.html')

def submit(request):
	name = request.POST['name']
	interest = request.POST['interest']

	if not User.objects.filter(name=name):
		user = User.objects.create(name=name)
		interest = Interest.objects.create(interest=interest)
		interest.names.add(user)

	else:
		user = User.objects.get(name=name)
		interest = Interest.objects.create(interest=interest)
		interest.names.add(user)
	return redirect('many/users')

def users(request):
	users = User.objects.all()
	context = {
		'users': 
		users
		}
	return render(request, 'many/users.html', context)

def interests(request, id):
	user = User.objects.get(id=id)
	interests = Interest.objects.filter(names=user)
	print interests
	context = {
		'user': user, 
		'interests': interests
		}
	return render(request, 'many/interests.html', context)