from django.shortcuts import render, redirect
from .models import FreeClass

# 🔹 Home / Search Page
def login(request):
    # Extract unique values for dropdowns
    blocks = FreeClass.objects.values_list('Block', flat=True).order_by('Block').distinct()
    floors = FreeClass.objects.values_list('Floor', flat=True).order_by('Floor').distinct()
    days = [day for day, _ in FreeClass.DAY_CHOICES]
    times = [time for time, _ in FreeClass.TIME_CHOICES]

    context = {
        'blocks': blocks,
        'floors': floors,
        'days': days,
        'times': times,
    }
    return render(request, 'login.html', context)


# 🔹 Common Query Function
def get_classes(block, day, time, floor, occupied=None):
    query = FreeClass.objects.filter(Block=block, Day=day, Time=time, Floor=floor)

    # Apply filter if 'occupied' flag is given
    if occupied is not None:
        query = query.filter(is_occupied=occupied)

    return query.order_by('Room_No')


# 🔹 Default Search: Show Available Classes
def searchclass(request):
    block = request.GET.get('block')
    day = request.GET.get('day')
    time = request.GET.get('time')
    floor = request.GET.get('floor')

    # Default → show only available classes
    if all([block, day, time, floor]):
        classes = get_classes(block, day, time, floor, occupied=False)
        return render(request, 'base.html', {
            'classes': classes,
            'block': block, 'day': day, 'time': time, 'floor': floor
        })

    return redirect('login')


# 🔹 Show All Classes (when filter clicked)
def all_classes(request):
    block = request.GET.get('block')
    day = request.GET.get('day')
    time = request.GET.get('time')
    floor = request.GET.get('floor')

    if all([block, day, time, floor]):
        classes = get_classes(block, day, time, floor)
        return render(request, 'base.html', {
            'classes': classes,
            'block': block, 'day': day, 'time': time, 'floor': floor
        })

    return redirect('login')


# 🔹 Available Classes (filter button)
def available_classes(request):
    block = request.GET.get('block')
    day = request.GET.get('day')
    time = request.GET.get('time')
    floor = request.GET.get('floor')

    if all([block, day, time, floor]):
        classes = get_classes(block, day, time, floor, occupied=False)
        return render(request, 'base.html', {
            'classes': classes,
            'block': block, 'day': day, 'time': time, 'floor': floor
        })

    return redirect('login')


# 🔹 Occupied Classes (filter button)
def occupied_classes(request):
    block = request.GET.get('block')
    day = request.GET.get('day')
    time = request.GET.get('time')
    floor = request.GET.get('floor')

    if all([block, day, time, floor]):
        classes = get_classes(block, day, time, floor, occupied=True)
        return render(request, 'base.html', {
            'classes': classes,
            'block': block, 'day': day, 'time': time, 'floor': floor
        })

    return redirect('login')
