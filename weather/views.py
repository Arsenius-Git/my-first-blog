from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
import requests
from django.template import loader
from .models import ToDoList, Item, ExpensesTrack
from django.db.models import Sum
from .forms import CreateNewList, GetUrl, Transaction
from .shorten_url import shorten
# Create your views here.
WEATHER_API_KEY = 'b9c694f06f6246f08fb195351252402'

def weather(response):
    return render(response, 'weather/home.html')

def get_weather(api_key, location):
    base_url = 'http://api.weatherapi.com/v1/current.json'
    params = {
        'key': api_key,
        'q': location,
        'aqi': 'no'
    }
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        response = response.json()
        return response
    else:
        return {"error":f"Error:{response.status_code}", 'message': response.text}
def view_weather(request):
        weather_data = None

        if request.method == 'POST':
            location = request.POST.get('location', '')
            if location:
                weather_data = get_weather(WEATHER_API_KEY, location)

        return render(request, 'weather/weather_template.html', {'weather': weather_data})
def view_todo(response):
    td = ToDoList.objects.get(id=1)

    {"save":["save"], "c1":["clicked"]}
    if response.method == 'POST':
        print(response.POST)
        if response.POST.get("save"):
            for item in td.item_set.all():
                if response.POST.get('c'+ str(item.id)) == 'clicked':
                    item.complete = True
                else:
                    item_complete = False
                item.save()

        elif response.POST.get('newItem'):
            txt = response.POST.get("new")

            if len(txt) > 2:
                td.item_set.create(text=txt, complete=False)
            else:
                print('Invalid input')


    return render(response, 'weather/todo_template.html', {"name":td.name,"td": td})
def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
             n = form.cleaned_data["name"]
             t = ToDoList(name=n)
             t.save()

    else:
        form = CreateNewList()
    return render(response, 'weather/create.html', {"form": form})

def short_url(request):
    #BITLY_API = '4eb9f978f4d96fc38b6de686e8be2826cf6d386e'
    if request.method == 'POST':
        form = GetUrl(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data['url']
            shortened = shorten(user_input)
            return render(request, 'weather/short_url.html', {
                "form":form,
                "shortened_url":shortened
            })
    else:
        form = GetUrl()
    return render(request, 'weather/short_url.html', {"form":form})

def expenses_track(request):
    expenses = ExpensesTrack.objects.all().order_by('-date')
    balance = ExpensesTrack.objects.aggregate(Sum('amount'))['amount__sum'] or 0

    form = Transaction()
    if request.method == 'POST':
        form = Transaction(request.POST)
        if form.is_valid():
            #f = form.cleaned_data["description"]
            form.save()
            return redirect('expense_track')
    return render(request, 'weather/expenses_template.html', {
        'expenses':expenses,
        'balance':balance,
        'form':form,
    })