from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Board
from app1.forms import chessForm

# Create your views here.
def home(request):
   
    newGame()

    page_data = { "rows": [], "chess_form": chessForm }
    if (request.method == 'POST'):
        chess_form = chessForm(request.POST);
        if (chess_form.is_valid()):
            location = chess_form.cleaned_data["location"]
            value = chess_form.cleaned_data["value"]
            Board(name=location, value=value).save()
        else:
            page_data["chess_form"] = chess_form          

    for row in range (1,9):
        row_data = {}
        for col in range (1,9):
            name = "{}{}".format(row,col)
            try:
                record = Board.objects.get(name=name)
                row_data[name] = record.value
            except Board.DoesNotExist:
                row_data[name] = 0
        page_data.get("rows").append(row_data)

    return render(request, 'app1/home.html', context=page_data)

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

def about(request):
    request_args = request.GET
    request_args_string = request_args.urlencode()
    page_data = {"args": request_args_string}
    return render(request, 'app1/about.html', context=page_data)

def newGame():
    page_data = {
        "rows": [
            {"A8": "<sup>8</sup>&#9820;", "B8": "&#9822;", "C8": "&#9821;", "D8": "&#9818;", "E8": "&#9819;", "F8": "&#9821;", "G8": "&#9822;", "H8": "&#9820;"},
            {"A7": "<sup>7</sup>&#9823;", "B7": "&#9823;", "C7": "&#9823;", "D7": "&#9823;", "E7": "&#9823;", "F7": "&#9823;", "G7": "&#9823;", "H7": "&#9823;"},
            {"A6": "<sup>6</sup>&nbsp;", "B6": "&nbsp;", "C6": "&nbsp;", "D6": "&nbsp;", "E6": "&nbsp;", "F6": "&nbsp;", "G6": "&nbsp;", "H6": "&nbsp;"},
            {"A5": "<sup>5</sup>&nbsp;", "B5": "&nbsp;", "C5": "&nbsp;", "D5": "&nbsp;", "E5": "&nbsp;", "F5": "&nbsp;", "G5": "&nbsp;", "H5": "&nbsp;"},
            {"A4": "<sup>4</sup>&nbsp;", "B4": "&nbsp;", "C4": "&nbsp;", "D4": "&nbsp;", "E4": "&nbsp;", "F4": "&nbsp;", "G4": "&nbsp;", "H4": "&nbsp;"},
            {"A3": "<sup>3</sup>&nbsp;", "B3": "&nbsp;", "C3": "&nbsp;", "D3": "&nbsp;", "E3": "&nbsp;", "F3": "&nbsp;", "G3": "&nbsp;", "H3": "&nbsp;"},
            {"A2": "<sup>2</sup>&#9817;", "B2": "&#9817;", "C2": "&#9817;", "D2": "&#9817;", "E2": "&#9817;", "F2": "&#9817;", "G2": "&#9817;", "H2": "&#9817;"},
            {"A1": "<sup>1</sup> &#9814;<sub>A</sub>", "B1": "&#9816;<sub>B</sub>", "C1": "&#9815;<sub>C</sub>", "D1": "&#9812;<sub>D</sub>", "E1": "&#9813;<sub>E</sub>", "F1": "&#9815;<sub>F</sub>", "G1": "&#9816;<sub>G</sub>", "H1": "&#9814;<sub>H</sub>"
            }
        ]
    }
    for row in page_data.get("rows"):
        for name, value in row.items():
            Board(name=name, value=value).save()
