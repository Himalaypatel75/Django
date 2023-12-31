from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm
# Create your views here.

# rooms = [
#     {'id': 1,'name' : 'Lets Lear Python!'},
#     {'id': 2,'name' : 'Himalay Design!'},
#     {'id': 3,'name' : 'Front-end Developemnt!'},
# ]

def home(request):
    rooms = Room.objects.all().order_by('-id')
    return render(request, 'base/home.html', {'rooms' : rooms})

def room(request, pk):
    room = Room.objects.get(id = pk)
    context =  {'room' : room}
    return render(request, 'base/room.html', context)


def create_room(request):
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
            
        # print(request.POST)
    context = {'form' : form}
    return render(request, 'base/room_form.html', context)


def update_room(request, pk):
    room = Room.objects.get(id = pk)
    form = RoomForm(instance=room)
    context = {'form' : form}
    
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
            
            
    return render(request, 'base/room_form.html', context)


def delete_room(request, pk):
    room = Room.objects.get(id = pk)
    if request.method == "POST":
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj' : room})