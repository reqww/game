from django.shortcuts import render 
from accounts.models import Profile
from django.contrib.auth.models import User 
from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm
from game.models import GameItem
from django.contrib.auth import authenticate, login
from django.contrib import messages 
from accounts.forms import UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth.hashers import check_password, make_password

def register(request):
	if request.method == "POST":
		form = RegistrationForm(request.POST)
		if form.is_valid(): 
			new_user = form.save(commit=False)
			new_user.set_password(form.cleaned_data["password"])
			new_user.save()
			new_player = GameItem()
			new_player.owner = new_user
			new_player.save()
			Profile.objects.create(user=new_user)

			return render(
				request, "accounts/registration_complete.html", {
				"new_user": new_user}
			)
	else:
		form = RegistrationForm()

	return render(request, "accounts/register.html", {"user_form": form})

def log_in(request):
	if request.method=="POST":
		username = request.POST["username"]
		password = request.POST["password"]

		print(username, password)

		user = authenticate(
		request,
		username = username,
		password = password
		)

		if user is None:
			messages.error(request,"Неправильный логин и/или пароль")
			return redirect("list")

		login(request,user)
		messages.success(request, "Вы успешно вошли!")
		return redirect("list")

	return redirect("list")

@login_required
def edit(request):
	if request.method == "POST":
		user_form = UserEditForm(instance=request.user, data=request.POST)
		profile_form = ProfileEditForm(
			instance=request.user.profile, 
			data=request.POST,
			files=request.FILES
		)

		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
		u = request.user
		return redirect(f"/game/profile/{u.username}")
	else:
		user_form = UserEditForm(instance=request.user)
		profile_form = ProfileEditForm(instance=request.user.profile)

	return render(
		request,
		"accounts/edit.html",
		{"user_form": user_form, "profile_form": profile_form},
	)

class PasswordChangeView(View):

	def post(self, request, *args, **kwargs):
		u = self.request.user
		old_pass = request.POST.get('old_pass', False)
		if check_password(old_pass, u.password):
			new_pass1 = request.POST.get('new_pass1', False)
			new_pass2 = request.POST.get('new_pass2', False)
			if new_pass1 == new_pass2:
				if len(new_pass1)>=8:
					if check_password(old_pass, new_pass1):
						messages.error(request,"Пароли одинковые!")
					else:
						u.set_password(new_pass1)
						u.save()
						login(request,u)
						messages.success(request,"Вы успешно сменили пароль!")
						return redirect(f"/game/profile/{u.username}")
				else:
					messages.error(request,"Пароль слишком короткий!")
			else:
				messages.error(request,"Пароли не совпадают!")
		else:
			messages.error(request,"Неправильный пароль!")

		return redirect("edit")

