from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Board

# Create your views here.
def home(request):
    #return HttpResponse("Hello World!")
    request_args = request.GET
    request_args_string = request_args.urlencode()
    page_data = {"rows":[], "args": request_args_string}
    for row in range(1,10):
        row_data = {}
        for col in range(1,10):
            name = "r{}c{}".format(row,col)
            value = request_args.get(name)
            if (value):
                row_data[name] = int(value)
            else:
                row_data[name] = 0
        page_data.get("rows").append(row_data)
    return render(request, 'app1/home.html', context=page_data)



    for row in page_data.get("rows"):
        for name, value in row.items():
            if (value!='&nbsp'):
                Board(name= "a1", value="2").save()



def history(request):
    request_args = request.GET
    request_args_string = request_args.urlencode()
    page_data = {"args": request_args_string}
    return render(request, 'app1/history.html', context=page_data)

def rules(request):
    request_args = request.GET
    request_args_string = request_args.urlencode()
    page_data = {"args": request_args_string}
    return render(request, 'app1/rules.html', context=page_data)
