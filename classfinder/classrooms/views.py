from django.shortcuts import render, redirect
from .models import FreeClass
from django.db.models import Q

def login(request):

    days = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY']
    times = ['9-10 AM', '10-11AM', '11-12PM', '12-1PM', '1-2PM', '2-3PM', '3-4PM', '4-5PM']

    blocks =FreeClass.objects.values_list('Block',flat=True).distinct()
    floors = FreeClass.objects.values_list('Floor',flat=True).distinct()

    context = {
        'days':days,
        'times':times,
        'blocks':blocks,
        'floors':floors
    }
    return render(request,'login.html',context)

def searchclass(request):
    block = request.GET.get('block')
    day   = request.GET.get('day')
    time  = request.GET.get('time')
    floor = request.GET.get('floor')

    if block and day and time and floor:
        classes = FreeClass.objects.filter(Block=block, Day=day, Time=time,Floor=floor,is_occupied=True).order_by('Room_No')
        context = {'classes': classes, 'block': block, 'day': day, 'time': time,'floor':floor}
        return render(request, 'base.html', context)

    return redirect('login')

def occupied_classes(request):
    block = request.GET.get('block')
    day = request.GET.get('day')
    time = request.GET.get('time')
    floor = request.GET.get('floor')

    if block and day and time and floor:
        classes = FreeClass.objects.filter(Block=block, Day=day, Time=time,Floor=floor,is_occupied=False).order_by('Room_No')
        context = {'classes': classes, 'block': block, 'day': day, 'time': time,'floor':floor}
        return render(request, 'base.html', context)
    else:
        return redirect('searchclass')
    

def available_classes(request):
    block = request.GET.get('block')
    day = request.GET.get('day')
    time = request.GET.get('time')
    floor = request.GET.get('floor')

    if block and day and time and floor:
        classes = FreeClass.objects.filter(Block=block,Day=day,Time=time,Floor=floor,is_occupied=True).order_by('Room_No')
        context = {'classes': classes, 'block': block, 'day': day, 'time': time,'floor':floor}
        return render(request, 'base.html', context)
    else:
        return redirect('searchclass')
    
def all_classes(request):
    block = request.GET.get('block')
    day = request.GET.get('day')
    time = request.GET.get('time')
    floor = request.GET.get('floor')

    if block and day and time and floor:
        classes = FreeClass.objects.filter(Block=block,Day=day,Time=time,Floor=floor).order_by('Room_No')
        context = {'classes': classes, 'block': block, 'day': day, 'time': time,'floor':floor}
        return render(request, 'base.html', context)
    else:
        return redirect('searchclass')




