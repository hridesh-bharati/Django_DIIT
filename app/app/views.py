from django.shortcuts import render
from django.http import HttpResponse

def home(request):
        diit={
        'title':'Home Page',
        'DIIT':'DRISHTEE COMPUTER CENTER',
        'img1':'https://images.unsplash.com/photo-1547394765-185e1e68f34e?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTh8fGNvbXB1dGVyfGVufDB8fDB8fHww',
        'img2':'https://images.unsplash.com/photo-1548092372-0d1bd40894a3?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjZ8fGNvbXB1dGVyfGVufDB8fDB8fHww',
        'CardPic1':'https://i.morioh.com/210414/6c7f6e9b.webp',
        'CardPic2':'https://revelry.co/wp-content/uploads/2019/05/react-native-UX-design.gif',
        'CardPic3':'https://th.bing.com/th/id/OIP.M1U-BOiIzjE8ERoPA2GqpQHaE8?rs=1&pid=ImgDetMain',
        'pythonTitle':'LEARN PYTHON COURSE',
        'ReactTitle':'LEARN REACT JS COURSE',
        'NodeTitle':'LEARN REACT JS COURSE'
            
    }
        return render(request, "index.html",diit)

def aboutUs(request):
    return HttpResponse("Drishtee computer center About")

def course(request):
    return HttpResponse("Course")

def courseDetails(request, courseid):
    return HttpResponse(courseid)
