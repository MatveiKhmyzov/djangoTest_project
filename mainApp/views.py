from django.shortcuts import render


def index(request):
    return render(request, 'mainApp/homePage.html')


def contact(request):
    return render(request, 'mainApp/basic.html',
                  {'values': ['Если у Вас остались вопросы, звоните по телефону',
                               '(067) 067-67-67']})
