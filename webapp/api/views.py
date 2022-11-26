from django.shortcuts import render, redirect
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomPasswordChangeForm

def docs(request):
	return render(request, "api/docs.html")

@login_required()
def key(request):
	return render(request, "api/key.html")

def register(request):
	if request.method == "POST":
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect('api_key')
	else:
		form = CustomUserCreationForm()

	return render(request,'api/register.html',{'form':form})

@login_required()
def change_password(request):
	if request.method == "POST":
		form = CustomPasswordChangeForm(user=request.user, data=request.POST)
		print(form.data)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('api_key')
	else:
		form = CustomPasswordChangeForm(user=request.user)

	return render(request,'api/change_password.html',{'form':form})
