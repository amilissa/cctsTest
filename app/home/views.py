from django.shortcuts import render, HttpResponse, redirect
import pdb

# Create your views here.
posts = [
    {
        'name': 'Amilissa',
        'job': 'Job Order',
        'date_apply': 'November 4, 2020'
    },
    {
        'name': 'Mark Libres',
        'job': 'Job Order',
        'date_apply': 'November 5, 2020'
    }
]
def login(request):

    # print(dir(request.user.is_authenticated))
    # pdb.set_Trace();
    if request.user.is_authenticated :
        return redirect('home/')


    return render(request, 'login.html', {'title': 'Login'})
    pass;

def home(request):
    data = {
        'posts': posts
    }

    return render(request, 'home.html', data);
    pass;
