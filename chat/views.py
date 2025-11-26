from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from chat.forms import ProfileForm, RoomForm
from .models import Room, Message, Profile


def index(request):
    return render(request, "chat/index.html")


@login_required
def room_list(request):
    rooms = Room.objects.all()
    return render(request, "chat/rooms.html", {"rooms": rooms})


@login_required
def chat_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    messages = room.messages.order_by("created_at")
    return render(request, "chat/chat.html", {"room": room, "messages": messages})


@login_required
def send_message(request, room_id):
    if request.method == "POST":
        text = request.POST.get("text")
        if text:
            room = Room.objects.get(id=room_id)
            Message.objects.create(room=room, user=request.user, text=text)
    return redirect("chat_room", room_id=room_id)


@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'chat/profile.html', {'form': form})


@login_required
def create_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.owner = request.user
            room.save()
            return redirect('chat_room', room_id=room.id)
    else:
        form = RoomForm()
    return render(request, 'chat/create_room.html', {'form': form})
