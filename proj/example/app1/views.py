from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Board
from app1.forms import SudokuForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def home(request):
    if request.method == 'GET' and 'cellname' in request.GET:
        cellname = request.GET["cellname"]
        if (cellname is not None and cellname != ''):
            cellvalue = request.GET["cellvalue"]
            if (cellvalue is not None and cellvalue != ''):
                Board(name=cellname, value=cellvalue).save()

    if request.method == 'GET' and 'new_game' in request.GET:
        newGame()

    page_data = { "rows": [], "sudoku_form": SudokuForm }
    if (request.method == 'POST'):
        sudoku_form = SudokuForm(request.POST);
        if (sudoku_form.is_valid()):
            location = sudoku_form.cleaned_data["location"]
            value = sudoku_form.cleaned_data["value"]
            Board(name=location, value=value).save()
        else:
            page_data["sudoku_form"] = sudoku_form

    for row in range (1,10):
        row_data = {}
        for col in range (1,10):
            name = "r{}c{}".format(row,col)
            try:
                record = Board.objects.get(name=name)
                row_data[name] = record.value
            except Board.DoesNotExist:
                row_data[name] = 0
        page_data.get("rows").append(row_data)

    return render(request, 'app1/home.html', context=page_data)

@login_required(login_url='/login/')
def history(request):
    request_args = request.GET
    request_args_string = request_args.urlencode()
    page_data = {"args": request_args_string}
    return render(request, 'app1/history.html', context=page_data)

@login_required(login_url='/login/')
def rules(request):
    request_args = request.GET
    request_args_string = request_args.urlencode()
    page_data = {"args": request_args_string}
    return render(request, 'app1/rules.html', context=page_data)


def newGame():
    page_data = {
        "rows": [
            {"r1c1": 6, "r1c2": 7, "r1c3": 0, "r1c4": 0, "r1c5": 4, "r1c6": 8, "r1c7": 0, "r1c8": 1, "r1c9": 0},
            {"r2c1": 3, "r2c2": 5, "r2c3": 0, "r2c4": 0, "r2c5": 0, "r2c6": 1, "r2c7": 0, "r2c8": 4, "r2c9": 7},
            {"r3c1": 0, "r3c2": 1, "r3c3": 0, "r3c4": 7, "r3c5": 2, "r3c6": 0, "r3c7": 6, "r3c8": 8, "r3c9": 0},
            {"r4c1": 8, "r4c2": 0, "r4c3": 3, "r4c4": 0, "r4c5": 0, "r4c6": 0, "r4c7": 1, "r4c8": 6, "r4c9": 9},
            {"r5c1": 0, "r5c2": 0, "r5c3": 7, "r5c4": 9, "r5c5": 1, "r5c6": 0, "r5c7": 8, "r5c8": 3, "r5c9": 0},
            {"r6c1": 0, "r6c2": 9, "r6c3": 6, "r6c4": 4, "r6c5": 8, "r6c6": 3, "r6c7": 0, "r6c8": 0, "r6c9": 0},
            {"r7c1": 0, "r7c2": 0, "r7c3": 9, "r7c4": 1, "r7c5": 0, "r7c6": 4, "r7c7": 3, "r7c8": 0, "r7c9": 8},
            {"r8c1": 4, "r8c2": 8, "r8c3": 1, "r8c4": 0, "r8c5": 0, "r8c6": 0, "r8c7": 7, "r8c8": 0, "r8c9": 6},
            {"r9c1": 7, "r9c2": 0, "r9c3": 0, "r9c4": 8, "r9c5": 6, "r9c6": 2, "r9c7": 0, "r9c8": 0, "r9c9": 1}
        ]
    }

    Board.objects.all().delete()
    for row in page_data.get("rows"):
        for name, value in row.items():
            if (value != 0):
                Board(name=name, value=value).save()
