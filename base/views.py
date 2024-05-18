from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Room ,Topic
from django.db.models import Q
from .forms import RoomForm
# Create your views here.

# rooms = [
#     {"id": 1, "name": "Living Room"},
#     {"id": 2, "name": "Bedroom"},
#     {"id": 3, "name": "Kitchen"},
#     {"id": 4, "name": "Bathroom"}
# ]


# cars_data = [
#     {"id": 1, "brand": "Toyota", "model": "Camry"},
#     {"id": 2, "brand": "Honda", "model": "Accord"},
#     {"id": 3, "brand": "Ford", "model": "Mustang"},
#     {"id": 4, "brand": "Chevrolet", "model": "Corvette"}
# ]

# def cars_view(request):
    
#     context = {"cars": cars_data}
#     return render(request, "base/cars.html", context)

# def cartype(request,pk):
#     car = None
#     for c in cars_data:
#         if c["id"]== int(pk):
#             car = c
#     context = {"car" : car}     
#     return render(request,"base/cartype.html",context)   

def home(request):
    q = request.GET.get("q") if request.GET.get('q') != None else '' 
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(host__username__icontains=q)
    )
    room_count = rooms.count()
    topics = Topic.objects.all()
    context = {"rooms" : rooms , "topics":topics,"room_count":room_count}
    return render(request,"base/home.html",context)

def room(request,pk):
    # rooms = Room.objects.all();
    # room = None
    # for r in rooms:
    #     if r.id == int(pk):
    #         room = r
    room = Room.objects.get(id=pk)
    context = {"room" : room}
    return render(request,"base/room.html",context)

# crud operation 
# create
def createRoom(request):
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    context = {"form":form}
    return render(request,"base/room_form.html",context)

# def createRoom(request):
#     form = RoomForm()
#     if request.method == "POST":
#         print(request.POST)
#     context = {"form":form}
#     return render(request,"room_form.html",context)

# from django.forms import ModelForm
# from .models import Room

# class RoomForm(ModelForm):
#     class Meta:
#         model=Room
#         fields = '__all__'
# {% extends 'main.html' %}

# {% block content%}

# <div>
#     <form action="" method="POST">
#         {% csrf_token %}
#         {{form.as_p}}
#         <input type="submit" value="Submit">
#     </form>
# </div>

# {% endblock content %}
# update
# def updateRoom(request,pk):
#     room = Room.objects.get(id=int(pk))
#     form = RoomForm(instance=room)
#     if request.method == "POST":
#         form =RoomForm(request.POST ,instance=room)
#         if form.is_valid():
#             form.save()
#             return redirect("home") 
#     context= {"form":form}
#     return render(request, "base/room_form.html" , context)
def updateRoom(request,pk):
    room = Room.objects.get(id = int(pk))
    form = RoomForm(instance=room)

    if request.method == "POST":
        form =RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form" : form}
    return render(request,"base/room_form.html",context)

# DELETE
def deleteRoom(request,pk ):
    room = Room.objects.get(id=pk)
    if request.method == "POST":
        room.delete()
        return redirect("home")
    return render(request,"base/delete.html",{'roomName':room})

# 

# def checkRoom(request, pk):
#     room = None
#     for r in rooms:
#         if r['id'] == int(pk):
#             room = r
#     context = {"room": room}
#     return render(request, "checkRoom.html", context)

# path("room/<str:pk>/",views.checkRoom,name="room")

# <h1>{{room.id}}</h1>
# <h1 class="check">{{room.name}}</h1>