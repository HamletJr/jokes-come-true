from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Joshua Montolalu',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)