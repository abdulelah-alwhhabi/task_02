from django.shortcuts import render

def test(request):

    context = {
        'msg': 'Hello World!'
    }
    return render(request, 'hello.html' , context)

# Create your views here.
