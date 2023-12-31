from django.shortcuts import render


from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from .forms import *
from .models import *
from django.http import HttpResponse

def about(request):
    return render(request,'home.html')
# Create your views here.
def login(request):
   
   
   if request.method == "POST":
      #Get the posted form
      if request.POST['username'] != "":
         
         username = request.POST['username']
    
      else:
         username = "not logged in"
        
   return render(request, 'user.html', {"username" : username})

def adminlogin(request):
   return render(request,'adminlogin.html')
def adminsign(request):
   return render(request,'adminsign.html')

def home(request):
    if request.method == 'POST':
        print(request.POST)
        questions=QuesModel.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.ans ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
      #   percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            # 'percent':percent,
            'total':total
        }
        return render(request,'Result.html',context)
    else:
        questions=QuesModel.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'Quizhtml.html',context)
     
# def add(request):
#    return render(request,'addQuestion.html')


def addQuestion(request):    
   
   form=addQuestionform()
   if(request.method=='POST'):
         form=addQuestionform(request.POST)
         if(form.is_valid()):
               form.save()
               return redirect('/Quizhtml.html')
   context={'form':form}
   return render(request,'addQuestion.html',context)
   