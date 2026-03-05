from django.shortcuts import render

# Create your views here.
def Employee(request):
    data={
        'name':'suhas'
    }
    context={}
    
    if request.methiod=='POST':
        username=request.post.get('username')
        if username:
            context['username']=username
        else:
            context['full name']='Please enter your name'
    return render(request,'Employee.html',data) 