from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import UserManager, User, MessageManager, MessagePost, EditManager, Edit

def index(request):
    return render(request, "main.html")

def register(request):
    if request.method=='POST':
        errors=User.objects.validator(request.POST)
        if errors:
            for error in errors:
                messages.error(request, errors[error])
            return redirect('/')

        user_pw=request.POST['pw']
        hash_pw=bcrypt.hashpw(user_pw.encode(), bcrypt.gensalt()).decode()
        print(hash_pw)
        new_user = User.objects.create(first_name=request.POST['f_n'], last_name=request.POST['l_n'], email=request.POST['email'], password=hash_pw)
        print(new_user)
        request.session['user_id']=new_user.id
        request.session['user_name']=f"{new_user.first_name} {new_user.last_name}"
        return redirect('/quotes')
    return redirect('/')

def log_in(request):
    if request.method=='POST':
        logged_user=User.objects.filter(email=request.POST['email'])
        if logged_user:
            logged_user=logged_user[0]
            if bcrypt.checkpw(request.POST['pw'].encode(), logged_user.password.encode()):
                request.session['user_id']=logged_user.id
                request.session['user_name']=f"{logged_user.first_name} {logged_user.last_name}"
                return redirect('/quotes')
            else:
                messages.error(request, "Password was incorrect.")
        else:
            messages.error(request, "Email was not found.")
    return redirect('/')

def  sucess(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'all_messages':MessagePost.objects.all()
    }
    return render(request, "quotes.html", context)

def create_mess(request):
    if request.method=='POST':
        print(request.POST)
        error=MessagePost.objects.empty_validator(request.POST)
        if error:
            messages.error(request, error)
            return redirect('/quotes')
        MessagePost.objects.create(content=request.POST['contents'], poster=User.objects.get(id=request.session['user_id']))
        return redirect('/quotes')
    return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

def delete_mess(request, mess_id):
    MessagePost.objects.get(id=mess_id).delete()
    return redirect('/quotes')

def profile(request, user_id):
    context = {
        'user': User.objects.get(id=user_id)
    }
    return render(request, 'profile.html', context)

def add_like(request, user_id):
    liked_message = MessagePost.objects.get(id=user_id)
    print(f'user_id{user_id}')
    print(liked_message)
    user_liking = User.objects.get(id=request.session['user_id'])
    liked_message.user_likes.add(user_liking)
    print(user_liking.first_name)
    return redirect('/quotes')

def edit(request, user_id):
    context = {
        'edit':User.objects.get(id=user_id)
    }
    return render(request, 'edit.html', context)

def update(request, user_id):
    if request.method=='POST':
        errors=User.objects.new_validator(request.POST)
        if errors:
            for error in errors:
                messages.error(request, errors[error])
            return redirect('/edit')

    to_update = User.objects.get(id=user_id)
    to_update.first_name = request.POST['f_n']
    to_update.last_name = request.POST['l_n']
    to_update.email = request.POST['email']
    to_update.save()
    return redirect('/quotes')