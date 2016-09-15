from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from svsite.forms import UserForm, UserProfileForm
from cars.models import Car


def user_login(request):
    invalid = True
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            invalid = False
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Your account has been deactivated.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return render(request, 'login.html', {'invalid': invalid, },)
    else:
        return render(request, 'login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
                user = user_form.save()
                user.set_password(user.password)
                user.save()
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()
                registered = True
        else:
            print(user_form.errors, profile_form.errors)
            return render(request, 'register.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered,
                   'user_form_errors': user_form.errors, 'profile_form_errors': profile_form.errors},
                  )

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
                  'register.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}
                  )


def search_form(request):
    return render(request, 'search.html')


def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        else:
            cars = Car.objects.filter(full_name__icontains=q)
            return render(request, 'search-results.html', {'cars': cars, 'query': q})

    return render(request, 'search_results.html', {'errors': errors})


def car_details(request, manufacturer, slug):
    car = get_object_or_404(Car, manufacturer_slug=manufacturer, slug=slug)
    print(car)
    return render(request, 'car_details.html', {'car': car})

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def admin_render(request):
    return render(request, 'admin.html')

def compare(request):
    return render(request, 'compare.html')

def frame(request):
    return render(request, 'compare_frame.html')

def error404(request):
    return render(request, '404.html')

def error500(request):
    return render(request, '500.html')

def aboutus(request):
    return render(request, 'about.html')

def game(request):
    return render(request, 'game.html')
