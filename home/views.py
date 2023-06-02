from django.shortcuts import render,HttpResponse
from home.models import Contact
from django.contrib import messages

# super user id and pass is vaibhav 

# Create your views here.
def index(request):
    return render(request,'index.html')





def analyze(request):
    # if request.method=="GET":
        rtext=request.GET.get('text','default')
        removepunc=request.GET.get('removepunc','off')
        lowercase=request.GET.get('lowercase','off')
        fullcaps=request.GET.get('fullcaps','off')
        rnum=request.GET.get('rnum','off') 
        newliner=request.GET.get('newliner','off')  
        rspace=request.GET.get('rspace','off')    
        # print(removepunc)
        # print(rtext)
        punctuations='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        num='''1234567890'''
        analyzed=""
        if(removepunc=='on'):
            for char in rtext:
                if char not in punctuations:
                    analyzed=analyzed+char
            rtext=analyzed
            


        # to lower case
        if(lowercase=="on"):
            analyzed=""
          
            for char in rtext:
                analyzed=analyzed+char.lower()

            
            rtext=analyzed

        # to capital 
        if(fullcaps=="on"):
            analyzed=""
            for char in rtext:
                analyzed=analyzed+char.upper()
            
            rtext=analyzed


        # remove Number 
        if(rnum=="on"):
            analyzed=""
        
            for char in rtext:
                if char not in num:
                    analyzed=analyzed+char
            
            rtext=analyzed
                

        # to remove out new line 
        if(newliner=="on"):
            analyzed=""
            print("ur Input ")
            print(rtext)
            for char in rtext:
                if char !="\n":
                    analyzed = analyzed + char.upper()
            print("analyze ")
            print(analyzed)
        
            rtext=analyzed
            
        # to remove spaces 

        if(rspace=="on"):
            analyzed = ""
            for index, char in enumerate(rtext):
                if not(rtext[index] == " " and rtext[index+1]==" "):
                    analyzed = analyzed + char
            
        
        param={'purpose':'Remove new line ',
                'analyzed_text':analyzed}
        

         
             
        return render(request,'analyze.html',param)

        
                



def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
        messages.success(request,"Your form has been submitted succesfully")


    return render(request,'contact.html')