from . import file_word

from .Forms import ActiveForms, Dowland
from .DataandTime import dowland_now_date
from .models import diary
from django.contrib.auth import forms, login, logout
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .Forms import UserRegistrationForm


def index(request):
    return render(request, 'index.html')
@login_required(login_url='/login')
def dziennik(request):
    form = ActiveForms(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            dane = form.cleaned_data
            print("zapisujem")
            activity = dane["activity"]
            emotions = dane['emotions']
            name_user = request.user

            data = dowland_now_date()
            obj = diary(
                None, name_user, data, activity, emotions)
            obj.save()
            obj = diary.objects.all().filter(name_user=request.user).order_by('-data')
            print(obj)
            return render(request, 'list.html', {"obj": obj})
    return render(request, 'dziennik.html', {'form': form})

@login_required(login_url='/login')
def list_obj(request):
    # obj = diary()
    obj = diary.objects.all().filter(name_user=request.user).order_by('-data')
    return render(request, 'list.html', {"obj": obj})


def Exchange(obj):
    tup = []
    for item in obj:
        print(item.data)
        item_tuple = (item.data, item.activity, item.emotions)
        tup.append(item_tuple)
    return tup


def File(ex):
    file = file_word.DOC()
    file.addParagraph()
    file.AddTabet(records=ex)
    file.Save()


def sendEmail(email, name):
    from . import SendEmail
    send = SendEmail.SendEmail()
    send.EmailSettings(odbiorca=email)
    send.SendingAnEmail()


@login_required(login_url='/login')
def dowland(request):

    if request.method == 'POST':
        forms = Dowland(request.POST)
        if forms.is_valid():
            email = forms.cleaned_data['Email']
            name = forms.cleaned_data['Name']

            obj = diary.objects.all().filter(name_user=request.user).order_by('-data')
            ex = Exchange(obj)
            file = File(ex)
            sendEmail(email, name)
    else:
        forms = Dowland()
    return render(request, "register.html", {'form': forms})
def querAnd(request):
    return render(request, 'que.html')
def my_register(request):

    form = UserRegistrationForm()
    print(request.method)
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            # Ustawienie wybranego hasła.
            new_user.set_password(
                form.cleaned_data['password'])
            # Zapisanie obiektu User.
            new_user.save()
            return render(request, "login.html")
        else:
            form = UserRegistrationForm()
    return render(request, "register.html", {'form': form})

def my_login(request):
    """Logowanie uzytkownika w sytemie."""
    form = forms.AuthenticationForm() # ustawiamy formularz logowania
    if request.method == 'POST': # sprawdzamy, czy ktos probuje sie zalogowac
        # przypisujemy nadeslane dane do formularza logowania
        form = forms.AuthenticationForm(request, request.POST)
        # sprawdzamy poprawnosc formularza lub zwracamy informacje o bledzie
        if form.is_valid(): # jezeli wszystko jest ok – logujemy uzytkownika
            user = form.get_user()
            login(request, user)
            return render(request, 'index.html')
            # przekierowujemy uzytkownika na strone glowna

    context = {'form': form} # ustawiamy zmienne przekazywane do templatki
    # renderujemy templatke logowania
    return render(request, 'login.html', context)

def my_logout(request):
    """Wylogowywanie uzytkownika z systemu"""
    logout(request)
    # przekierowujemy na strone glowna
    return render(request, "index.html")
