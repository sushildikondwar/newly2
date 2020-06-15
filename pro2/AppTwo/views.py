from django.shortcuts import render
from .models import User
from .forms import MyForm

# Create your views here.

def index(request):
    return render(request,'AppTwo/index.html')

def forms(request):
    
    form = MyForm()

    if request.method == 'POST':
        form = MyForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR, FORM IS INVALID")

    return render(request,'AppTwo/forms.html',{'form':form})

def users(request):
    details = User.objects.order_by('first_name')
    detail = {'alldetails':details}
    return render(request,'AppTwo/users.html',context=detail)