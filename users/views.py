from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import userregisterform, user_update, profile_update
from django.contrib.auth.decorators import login_required


# Create your views here.


def register(request):
    if request.method == 'POST':
        form = userregisterform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f"{username}are registered successfully!")
            return redirect('login')
    else:
        form = userregisterform()
    return render(request, 'users/reg.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        p_form = profile_update(request.POST, request.FILES, instance=request.user.profile)
        u_form = user_update(request.POST, request.user,instance=request.user)
        if u_form.is_valid() and p_form.is_valid():
            p_form.save()
            u_form.save()
            messages.success(request, "profile updated succesfully!")
            return redirect('profile')
    else:
        p_form = profile_update(instance=request.user.profile)
        u_form = user_update(instance=request.user)
    data = {'u_form': u_form,
            'p_form': p_form}

    return render(request, 'users/profile.html',data)
