from django.http import HttpResponse
import random
from django.shortcuts import render,redirect,get_object_or_404
from django.forms import ModelForm
from django.db.models import Sum, Count
from .models import biaoge
import datetime
import json
from .forms import SquirrelForm
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.views.generic import View

def map(request):
    sighting100 = random.sample(list(biaoge.objects.all()),100)
    sighting_list = []
    for sighting in sighting100:
        sighting_list.append({'xx':sighting.xx,'yy':sighting.yy})
    context = {'sightings':sighting_list,}
    return render(request,'htmls/map.html',context)
    
def success(request):
    return render(request,'htmls/success.html')

def mainmenu(request):
    squirrels = biaoge.objects.filter(have_image = True)
    activities = ['Running', 'Chasing', 'Climbing', 'Eating', 'Foraging', 'Kuks', 'Quaas', 'Moans', 'Other activities','Approaches','Tail Twitches','Runs from','Nothing']
    context ={'squirrels':squirrels,
              'activities': activities,
              'img1':'img1.PNG',
              'img2':'img2.PNG',
              'img3':'img3.JPG',
              'img4':'img4.PNG',
    }
    return render(request,'htmls/mainbase.html',context)

def add(request):
    # 判断是否为 post 方法提交 
    if request.method == "POST":
    #load things from web
        test1 = biaoge.objects.create(
        xx = request.POST.get('latitude',0),
        yy = request.POST.get('longtitude',0),
        Unique_Squirrel_ID = request.POST.get('Unique_Squirrel_ID',00-0000-00-00),
        shift = request.POST.get('shift',None),
        date = request.POST.get('date',None),
        age = request.POST.get('age',None),
        primary_fur_color = request.POST.get('primary_fur_color',None),
        location = request.POST.get('location',None),
        specific_location = request.POST.get('specific_location',None),
        running = request.POST.get('running',False),
        chasing = request.POST.get('chasing',False),
        climbing = request.POST.get('climbing',False),
        eating = request.POST.get('eating',False),
        foraging = request.POST.get('foraging',False),
        other_activities = request.POST.get('other_activities',None),
        kuks = request.POST.get('kuks',False),
        quaas = request.POST.get('quaas',False),
        tail_flags = request.POST.get('tail_flags',False),
        tail_twitches = request.POST.get('tail_twitches',False),
        approaches = request.POST.get('approaches',False),
        indifferent = request.POST.get('indifferent',False),
        runs_from = request.POST.get('runs_from',False),
        moans = request.POST.get('moans',False),
        profile_image = request.FILES.get('profile_image',None),
        have_image = request.POST.get('have_image',False),
        )
        test1.save()
        return redirect(f'/success')
    else:
        context= {'sssss':'sssss.jpg'}
        return render(request, 'htmls/add.html',context)

def edit(request,squirrel_id):
    test1 = biaoge.objects.get(pk = squirrel_id)
    if request.method == "POST":
        test1.xx = request.POST.get('latitude',0)
        test1.yy = request.POST.get('longtitude',0)
        test1.Unique_Squirrel_ID = request.POST.get('Unique_Squirrel_ID',00-00-0000-00)
        test1.shift = request.POST.get('shift',None)
        test1.date = request.POST.get('date',1111-11-11)
        test1.age = request.POST.get('age',None)
        test1.primary_fur_color = request.POST.get('primary_fur_color',None)
        test1.location = request.POST.get('location',None)
        test1.specific_location = request.POST.get('specific_location',None)
        test1.running = request.POST.get('running',False)
        test1.chasing = request.POST.get('chasing',False)
        test1.climbing = request.POST.get('climbing',False)
        test1.eating = request.POST.get('eating',False)
        test1.foraging = request.POST.get('foraging',False)
        test1.other_activities = request.POST.get('other_activities',None)
        test1.kuks = request.POST.get('kuks',False)
        test1.quaas = request.POST.get('quaas',False)
        test1.tail_flags = request.POST.get('tail_flags',False)
        test1.tail_twitches = request.POST.get('tail_twitches',False)
        test1.approaches = request.POST.get('approaches',False)
        test1.indifferent = request.POST.get('indifferent',False)
        test1.runs_from = request.POST.get('runs_from',False)
        test1.moans = request.POST.get('moans',False)
        #test1.profile_image= request.FILES.get('profile_image',None)
        if request.FILES.get('profile_image',None):
            test1.profile_image = request.FILES.get('profile_image',None)
        test1.have_image = request.POST.get('have_image',False)
        test1.save()
        
        return redirect(f'/success')
    else:
        context = {'squirrels':test1,
                   'method':'POST',
                   'sssss': 'sssss.jpg'
        }
        return render(request, 'htmls/edit.html',context)
"""
def goodview(request,squirrel_id):
    squirrels = biaoge.objects.get(pk = squirrel_id)
    context = {'squirrels':squirrels,
               'method':'GET',
               'sssss': 'sssss.jpg',
    }
    return render(request, 'htmls/edit.html',context)
"""

def search(request):
    squirrel_id = request.GET.get('search')
    try:
        squirrels = biaoge.objects.get(pk = squirrel_id)
    except:
        return render(request,'htmls/busuccess.html')
    else:
        squirrels = biaoge.objects.get(pk = squirrel_id)
        context= {'squirrels':squirrels,
                    'sssss':'sssss.jpg',
                    }
        return render(request, 'htmls/edit.html',context)

def sightings(request):
    squirrels = biaoge.objects.order_by('Unique_Squirrel_ID')
    context = {'squirrels':squirrels,}
    return render(request,'htmls/sightings.html',context)

def stats(request):
    sights = biaoge.objects.all()
    # shift
    AM_n = sights.filter(shift='AM').count()
    PM_n = sights.filter(shift='PM').count()
    AM_pct = AM_n/(AM_n + PM_n)
    AM_pct = "{:.2%}".format(AM_pct)
    PM_pct = PM_n/(AM_n + PM_n)
    PM_pct = "{:.2%}".format(PM_pct)
    
    # age
    Juvenile_n = sights.filter(age='Juvenile').count()
    Adult_n = sights.filter(age='Adult').count()
    Juvenile_pct = Juvenile_n / (Juvenile_n + Adult_n)
    Juvenile_pct = "{:.2%}".format(Juvenile_pct)
    Adult_pct = Adult_n / (Juvenile_n + Adult_n)
    Adult_pct = "{:.2%}".format(Adult_pct)

    # Primary_Fur_Color
    Black_n = sights.filter(primary_fur_color='Black').count()
    Gray_n = sights.filter(primary_fur_color='Gray').count()
    Cinnamon_n = sights.filter(primary_fur_color='Cinnamon').count()
    Black_pct = Black_n / (Black_n+Gray_n+Cinnamon_n)
    Black_pct = "{:.2%}".format(Black_pct)
    Gray_pct = Gray_n / (Black_n+Gray_n+Cinnamon_n)
    Gray_pct = "{:.2%}".format(Gray_pct)
    Cinnamon_pct = Cinnamon_n / (Black_n+Gray_n+Cinnamon_n)
    Cinnamon_pct = "{:.2%}".format(Cinnamon_pct)

    # Location
    Above_Ground_n = sights.filter(location='Above Ground').count()
    Ground_Plane_n = sights.filter(location='Ground Plane').count()
    Above_Ground_pct = Above_Ground_n / (Above_Ground_n+Ground_Plane_n)
    Above_Ground_pct = "{:.2%}".format(Above_Ground_pct)
    Ground_Plane_pct = Ground_Plane_n / (Above_Ground_n+Ground_Plane_n)
    Ground_Plane_pct= "{:.2%}".format(Ground_Plane_pct)

    # Runs_From
    True_n = sights.filter(runs_from=True).count()
    False_n = sights.filter(runs_from=False).count()
    True_pct = True_n / (True_n+False_n)
    True_pct = "{:.2%}".format(True_pct)
    False_pct = False_n / (True_n+False_n)
    False_pct = "{:.2%}".format(False_pct)

    context = {
            'Total':sights.count(),
            'Shift': {'AM': AM_n,'PM': PM_n},
            'Shift_pct': {'AM': AM_pct,'PM': PM_pct},
            'Age': {'Juvenile': Juvenile_n, 'Adult': Adult_n},
            'Age_pct': {'Juvenile': Juvenile_pct, 'Adult': Adult_pct},
            'Primary_Fur_Color': {'Black':Black_n, 'Gray':Gray_n, 'Cinnamon':Cinnamon_n},
            'Primary_Fur_Color_pct': {'Black':Black_pct, 'Gray':Gray_pct, 'Cinnamon':Cinnamon_pct},
            'Location': {'Above_Ground':Above_Ground_n, 'Ground_Plane':Ground_Plane_n},
            'Location_pct': {'Above_Ground':Above_Ground_pct, 'Ground_Plane':Ground_Plane_pct},
            'Runs_From': {'True':True_n, 'False':False_n},
            'Runs_From_pct': {'True':True_pct, 'False':False_pct},
            }

    return render(request, 'htmls/stats.html', {'context':context})
