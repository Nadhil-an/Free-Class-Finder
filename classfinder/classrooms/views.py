from django.shortcuts import render,redirect
from .models import FreeClass

# Create your views here.





def login(request):

    days = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY']
    times = ['9-10AM', '10-11AM', '11-12PM', '12-1PM', '1-2PM', '2-3PM', '3-4PM', '4-5PM']

    blocks =FreeClass.objects.values_list('Block',flat=True).distinct()

    context = {
        'days':days,
        'times':times,
        'blocks':blocks
    }



    return render(request,'login.html',context)


def searchclass(request):
    if request.method == 'POST':
        block = request.POST.get('block')
        day   = request.POST.get('day')
        time  = request.POST.get('time')

        print(f"Received → Block: '{block}', Day: '{day}', Time: '{time}'")

        classes = FreeClass.objects.filter(Block=block,Day=day,Time=time,is_occupied=True)
        display_block = classes.filter()
        print(display_block)

       


        

        context ={
            'classes':classes,
            'block':block,
            'time':time
            
        }

        return render(request,'base.html',context)
    return redirect('login')



