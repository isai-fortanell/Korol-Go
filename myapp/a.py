from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from .models import *
from .forms import *
from datetime import datetime

# Create your views here.


def home(request):
    date = datetime.now()
    months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio",
              "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    date_now = "{} {}, {} [{}:{}]".format(
        months[date.month - 1], date.day, date.year, datetime.now().hour, datetime.now().minute)

    form = MakeOrder()
    if request.method == "POST":
        if str(request.user)=="AnonymousUser":
            request.session['next_url'] = "/#order-section"
            login(request)
            context = {'redirected': True, 'backto': request.session['next_url']}
            return (render(request, 'login.html', context))

        form = MakeOrder(request.POST)
        if form.is_valid():
            order = Order.objects.create(client=request.user, time=str(
                date_now), name=request.POST['name'])
            order = Order.objects.get(
                time=str(date_now), name=request.POST['name'])
            return (redirect('/post-ordering/{}'.format(order.number)))
    _title = "Korol GO"
    context = {'form': form, 'title': _title}
    # return (render(request, 'order.html', context))
    return (render(request, 'index.html', context))


def greeting(request):
    name = request.GET['text']
    return (render(request, 'counter.html', {'name': name}))

@login_required(login_url="login")
def orders(request):
    def binarySearch(arr, l, r, x):
        # Check base case
        if r >= l:
            mid = l + (r - l) // 2
            # If element is present at the middle itself
            if arr[mid]['user_id']== x:
                return mid
            # Element  present in left subarray
            elif arr[mid]['user_id'] > x:
                return binarySearch(arr, l, mid-1, x)
            # Element present in right subarray
            else:
                return binarySearch(arr, mid + 1, r, x)
        else:
            # Element is not present in the array
            return -1

    clients = Client.objects.values()
    user = clients[binarySearch(clients, 0, len(clients)-1, request.user.id)]
    client = Client.objects.get(pk=request.user.id)

    if client.is_worker:
        orders = Order.objects.all()
        products = Product.objects.all()
        context = {
            'orders': orders,
            'products': products
        }
        return (render(request, 'view-orders.html', context))
    else:
        return(redirect("work_login"))




def view_order(request, order_number):
    try:
        order = Order.objects.get(pk=order_number)
    except:
        return(redirect('not_found'))
    context = {'order': order}
    return (render(request, 'view-order.html', context))


# @login_required(login_url="login")
def order(request):

    if not request.user.is_authenticated:
        login(request)
        context = {'redirected': True}
        return (render(request, 'login.html', context))

    date = datetime.now()
    months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio",
              "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    date_now = "{} {}, {} [{}:{}]".format(
        months[date.month - 1], date.day, date.year, datetime.now().hour, datetime.now().minute)

    form = MakeOrder()
    if request.method == "POST":
        form = MakeOrder(request.POST)
        if form.is_valid():
            order = Order.objects.create(client=request.user, time=str(
                date_now), name=request.POST['name'])
            order = Order.objects.get(
                time=str(date_now), name=request.POST['name'])
            return (redirect('/post-ordering/{}'.format(order.number)))
    context = {'form': form, 'auth':request.user.is_authenticated}
    return (render(request, 'order.html', context))

    # if request.method == "GET":
    #     return( render(request, 'order.html', {'form':MakeOrder()}))
    # else:
    #     Order.objects.create(time=str(date_now), name=request.POST['name'])
    #     return(redirect('/post-ordering/'))


def post_ordering(request, order_number):
    try:
        order = Order.objects.get(pk=order_number)
    except:
        return(redirect('not_found'))
    context = {'order': order}
    return (render(request, 'post-ordering.html', context))


def change_order(request, order_number):
    try:
        order = Order.objects.get(pk=order_number)
    except:
        return(redirect('not_found'))
    form = MakeOrder(instance=order)

    if request.method == "POST":
        form = MakeOrder(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return (redirect('/post-ordering/{}'.format(order_number)))

    context = {'form': form}
    return (render(request, 'order.html', context))


def cancel_order(request, order_number):
    try:
        order = Order.objects.get(pk=order_number)
    except:
        return(redirect('not_found'))
    if request.method == "POST":
        order.delete()
        return (redirect('home'))
    context = {'order': order}
    return (render(request, 'cancel-order.html', context))


def login(request):
    
    if request.method == "POST":
        _username = request.POST.get("username")
        _password = request.POST.get("password")
        try:
            user = authenticate(
                request, username=_username, password=_password)
        # if user is not None:
            dj_login(request, user)
            return (redirect("home"))
        except:
            messages.error(request, "Username and password do not match")
        try:
            user = User.objects.get(username=_username)
        except:
            messages.error(request, "Are you already registered?")

        next_url = request.session.get('next_url')
        # del request.session['next_url']
        return(redirect("work_login"))

    if str(request.user)=="AnonymousUser":
        context = {'redirected': False}
        return (render(request, 'login.html', context))
    else:
        return(redirect("work_login"))



def logout(request):
    dj_logout(request)
    return (redirect("home"))


def registrer(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():

            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            dj_login(request, user)
            #Registrer in clients (for have access to the worker attribute)
            Client.objects.create(user=request.user)

            return (redirect("home"))
        else:
            messages.error(request, "Somehting went wrong")
    context = {'form': form}
    return (render(request, "registrer.html", context))


def jsondata(request):
    data = list(Order.objects.values())
    return (JsonResponse(data, safe=False))

def not_found(request,):
    context = {}
    return(render(request, '404.html', context))

@login_required(login_url="login")
def work_login(request):


    def binarySearch(arr, l, r, x):
        # Check base case
        if r >= l:
            mid = l + (r - l) // 2
            # If element is present at the middle itself
            if arr[mid]['user_id']== x:
                return mid
            # Element  present in left subarray
            elif arr[mid]['user_id'] > x:
                return binarySearch(arr, l, mid-1, x)
            # Element present in right subarray
            else:
                return binarySearch(arr, mid + 1, r, x)
        else:
            # Element is not present in the array
            return -1
    
    clients = Client.objects.values()
    user = clients[binarySearch(clients, 0, len(clients)-1, request.user.id)]
    client = Client.objects.get(pk=request.user.id)

    if request.method =="POST":
        client.is_worker = False if client.is_worker == True else True
        client.save()
        return(redirect("work_login"))


    context = {'work': GetWork(), 'is_working': user['is_worker'], 'clients': clients}
    return(render(request, 'get-work.html',context ))

