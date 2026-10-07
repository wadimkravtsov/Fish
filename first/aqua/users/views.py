from django.shortcuts import render, redirect
from .forms import UserLoginForm,  UserRegistrationForm, UserProfileForm
from django.contrib import auth, messages
from products.models import Basket
from products.models import CatSlider
from django.contrib.auth.decorators import login_required


def login(request):
    slider_list = CatSlider.objects.all()
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                messages.success(request, 'Вы успешно авторизированны')
                return redirect('aqua_base')
    else:
        form = UserLoginForm()
    content = {
        'title': 'Авторизация',
        'form': form,
        'slider_list': slider_list
    }
    return render(request, 'users/login.html', content)

# def register(request):
#     slider_list = CatSlider.objects.all()
#     content = {"title": 'Регистрация',
#                'slider_list': slider_list
#                }
#
#     return render(request, 'users/register.html', content)

def register(request):
    slider_list = CatSlider.objects.all()
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            # username = form.cleaned_data['first_name']
            # email = form.cleaned_data['email']
            # subject = 'Ваш аккаунт создан'
            # message = username + "! Добро пожаловать в Store! Ваша регистрация прошла успешно!"
            # try:
            #     send_mail(
            #         subject,
            #         message,
            #         settings.EMAIL_HOST_USER,
            #         [email]
            #     )
            # except BadHeaderError:
            #     return HttpResponse('Обнаружен неверный заголовок')
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    content = {
        'title': 'Регистрация',
        'form': form,
        'slider_list': slider_list
    }
    return render(request, 'users/register.html', content)

@login_required
def profile(request):
    slider_list = CatSlider.objects.all()
    user = request.user
    if request.method == "POST":
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user)

    baskets = Basket.objects.filter(user=user)
    total_quantity = sum(basket.quantity for basket in baskets)  # [7, 3, 2] = 12
    total_sum = sum(basket.sum() for basket in baskets)

    context = {
        'title': 'Store - Профиль',
        'form': form,
        'slider_list': slider_list,
        'baskets': Basket.objects.filter(user=user),
        'total_quantity': total_quantity,
        'total_sum': total_sum
    }
    return render(request, 'users/profile.html', context)

def logout(request):
    auth.logout(request)
    messages.success(request, 'Вы вышли из учетной записи')
    return redirect('aqua_base')

# Create your views here.
