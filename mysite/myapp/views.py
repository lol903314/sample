from django.shortcuts import render,redirect
from django.http import HttpResponse
import random
from .models import Player,Dreamreal
from django.core.mail import send_mail

# Create your views here.
def hello(request):
    # text='hello lol'
    return render(request,'hello.html')

def bmi(request):
    height=float(request.GET.get('height'))/100
    weight=float(request.GET.get('weight'))
    bmi=round(weight/(height**2),2)
    return render(request,'bmi.html',locals())

def multi(request):
    row=int(request.GET.get('row'))
    col=int(request.GET.get('col'))

    box=[]
    for i in range(1,row+1):
        box1=[]
        for j in range(1,col+1):
            result=f'{i}*{j}={i*j}'
            box1.append(result)
        box.append(box1)
    return render(request,'multi.html',locals())

def crudops(request):
    # Creating an entry

    # dreamreal = Dreamreal(
    #     website="www.google.com",
    #     mail="alvin@google.com.com",
    #     name="alvin",
    #     phonenumber="0911222333"
    # )

    # dreamreal.save()

    # # Read ALL entries
    # objects = Dreamreal.objects.all()
    res = 'Printing all Dreamreal entries in the DB : <br>'

    # for elt in objects:
    #     res += elt.name + "<br>"

    # Read a specific entry:
    # sorex = Dreamreal.objects.get(name="alvin")
    # res += 'Printing One entry <br>'
    # res += sorex.name

    # # Delete an entry
    # res += '<br> Deleting an entry <br>'
    # sorex.delete()

    # # Update
    dreamreal = Dreamreal(
        website="www.google.com",
        mail="alvin@google.com.com",
        name="alvin",
        phonenumber="0911222444"
    )

    dreamreal.save()
    res += 'Updating entry<br>'

    dreamreal = Dreamreal.objects.get(name='alvin')
    dreamreal.name = 'mary'
    dreamreal.save()

    return HttpResponse(res)

def test(request):
    if request.method=='GET':
        return render(request,'test.html')
    else:
        fname=request.POST.get('fname')
        return HttpResponse(fname)

def register(request):
    if request.method=="POST":
        user=request.POST.get('user','')
        password=request.POST.get('password','')
        name=request.POST.get('name','')
        email=request.POST.get('email','')

        if Player.objects.filter(user=user).exists():
            return render(request,'register.html',{'error':'帳號已存在'})

        player=Player.objects.create(
            user=user,
            password=password,
            name=name,
            email=email
        )

        request.session['id']=player.id
        return redirect('login')
    return render(request,'register.html')

def login(request):
    if request.method=="POST":
        user=request.POST.get('user')
        password=request.POST.get('password')

        try:
            player=Player.objects.get(user=user,password=password)
            request.session['id']=player.id
            return redirect('mora')
        except Player.DoesNotExist:
            return render(request,'login.html',{'error':'帳密錯誤'})
    return render(request,'login.html')

def mora(request):
    player_id=request.session.get('id')
    if not player_id:
        return redirect('login')

    player=Player.objects.get(id=player_id)
    you=computer=result=None

    if request.method=='POST':
        you=request.POST.get('choice')
        computer=random.choice(['stone','paper','scissors'])

        if you==computer:
            result='平手'
            player.tie+=1
        elif (you=='stone' and computer=='scissors') or (you=='scissors' and computer=='paper') or (you=='paper' and computer=='stone'):
            result='你贏了'
            player.win+=1
        else:
            result='你輸了'
            player.lose+=1

        player.save()

    return render(request,'mora.html',{
        'user':player.user,
        'you':you,
        'computer':computer,
        'result':result,
        'win':player.win,
        'lose':player.lose,
        'tie':player.tie
    })

def reset(request):
    player_id=request.session.get('id')
    if not player_id:
        return redirect('login')

    player=Player.objects.get(id=player_id)
    player.win=player.lose=player.tie=0
    player.save()

    return redirect('mora')

def logout(request):
    del request.session['id']
    return redirect('login')

def sendSimpleEmail(request,emailto):
    res=send_mail('hello xxx','我來晚了，要重播惹QQ','xxx@gmail.com',[emailto])
    return HttpResponse('%s'%res)