from django.shortcuts import render,redirect
from django.core.mail import send_mail
from .forms import SignUPForm,ActivateForm
from .models import Profile
from django.contrib.auth.models import User

def signup(request):
    if request.method=='POST':
        form=SignUPForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            
            user.is_active=False
            form.save()  # trigger profile

            profile=Profile.objects.get(user__username=username)
            # send email

            send_mail(
            "Activate Code",
            f"welcome mr {username}\n pls use this code {profile.code}",
            "r_mido99@yahoo.com",
            [email],
            fail_silently=False,
                )
            return redirect(f'/accounts/{username}/activate')
        

    else:
        form=SignUPForm()

    return render(request,'accounts/signup.html',{'form':form})

def activate_code(request,username):
    profile=Profile.objects.get(user__username=username)
    if request.method=='POST':
        form=ActivateForm(request.POST)
        if form.is_valid():
            code=form.cleaned_data['code']
            if code==profile.code:
                profile.code=''

                user=User.objects.get(username=username)
                user.is_active=True

                user.save()
                profile.save()

                return redirect('accounts/login')


            
            

    else:
        form=ActivateForm()
    return render(request,'accounts/activate.html',{'form':form})
