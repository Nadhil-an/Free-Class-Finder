from django.shortcuts import render, redirect
from .models import FreeClass
from django.db.models import Q

def login(request):

    days = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY']
    times = ['9-10 AM', '10-11AM', '11-12PM', '12-1PM', '1-2PM', '2-3PM', '3-4PM', '4-5PM']

    blocks =FreeClass.objects.values_list('Block',flat=True).distinct()

    context = {
        'days':days,
        'times':times,
        'blocks':blocks
    }
    return render(request,'login.html',context)

def searchclass(request):
    block = request.GET.get('block')
    day   = request.GET.get('day')
    time  = request.GET.get('time')

    if block and day and time:
        classes = FreeClass.objects.filter(Block=block, Day=day, Time=time,is_occupied=True).order_by('Room_No')
        context = {'classes': classes, 'block': block, 'day': day, 'time': time}
        return render(request, 'base.html', context)

    return redirect('login')

def all_classes(request):
    return _filter_classes(request, filter_type='all')

def available_classes(request):
    return _filter_classes(request, filter_type='available')

def occupied_classes(request):
    block = request.GET.get('block')
    day = request.GET.get('day')
    time = request.GET.get('time')

    if block and day and time:
        classes = FreeClass.objects.filter(Block=block, Day=day, Time=time,is_occupied=False).order_by('Room_No')
        context = {'classes': classes, 'block': block, 'day': day, 'time': time}
        return render(request, 'base.html', context)
    else:
        return redirect('searchclass')

def _filter_classes(request, filter_type=None):
    block = request.GET.get('block')
    day = request.GET.get('day')
    time = request.GET.get('time')

    if block and day and time:
        if filter_type == 'all':
            # Only filter by block and day
            classes = FreeClass.objects.filter(Block=block, Day=day, Time=time).order_by('Room_No')

        elif filter_type == 'available':
            if time:
                classes = FreeClass.objects.filter(Block=block, Day=day, Time=time, is_occupied=True).order_by('Room_No')
            else:
                return redirect('searchclass')

        else:
            return redirect('searchclass')

        context = {
            'classes': classes,
            'block': block,
            'day': day,
            'time': time
        }
        return render(request, 'base.html', context)

    return redirect('login')
