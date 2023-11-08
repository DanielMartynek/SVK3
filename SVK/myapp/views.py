from django.shortcuts import render, redirect
from django.http import HttpResponse
import pandas as pd
import numpy as np
from . import preprocessing
from . import myfunctions as mf
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url="/")
def help(request):
    return render(request,"help.html")

@login_required(login_url="/")
def home(request):
    if request.method =="POST":
        file = request.FILES["database"]
        year_from = request.POST.get('year_from')
        year_to = request.POST.get('year_to')

        table = preprocessing.preprocessing(file,year_from,year_to)
        print(len(table[0]))
        counts = mf.histograms(table)
        m_a,m_b,f_a,f_b,list_gender = mf.gender_class(table)
        c_a,c_b,n_a,n_b,list_problem = mf.problem_class(table)
        #print(list_gender)

        data = {

            "counts":counts,
            "m_a":m_a,
            "m_b":m_b,
            "f_a":f_a,
            "f_b":f_b,
            "c_a":c_a,
            "c_b":c_b,
            "n_a":n_a,
            "n_b":n_b,
            "gender_list":list_gender,
            "problem_list":list_problem,
            "number_of_patients": len(table[0])
        }
        return render(request, 'index.html', data)

    else:
        data = {
        }
        return render(request, 'index.html',data)


def login_user(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/home')
        else:
            messages.success(request, ("Wrong username or password"))
            return redirect('/')
    else:
        return render(request,'login.html')
