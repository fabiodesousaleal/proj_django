from django.shortcuts import render, redirect


def mod_quest(request):
    return render(request, "mod_questoes.html")