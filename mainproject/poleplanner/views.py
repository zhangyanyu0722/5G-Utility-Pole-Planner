# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
#from django.http import HttpResponse
#from django.shortcuts import render
from django.views.decorators import csrf
import urllib.request
from django.shortcuts import HttpResponse, render, redirect
import os
import numpy as np
from PIL import Image
import cv2


def download(url, name):
    #url = "https://maps.googleapis.com/maps/api/streetview?size=600x600&location=42.350770,-71.093054%20&fov=90&heading=90&pitch=10%20&key=AIzaSyAG4xG9lpMwqFx5Q52MsAeR_e4taTLCNPc"
    conn = urllib.request.urlopen(url)
   # print(conn.getcode())
    f = open(name, 'wb')
    f.write(conn.read())
    f.close()
    print('Pic Saved!')


def getpicture(x1,y1,x2,y2):
    result = []
    logi = []
    logi.append(x1)
    while x1<x2:
        x1 = x1 + 0.0011
        logi.append(x1)
    logi = [("%.6f" % i) for i in logi]
    lati = []
    lati.append(y1)
    while y1>y2:
        y1 = y1 - 0.0005
        lati.append(y1)
    lati = [("%.6f" % i) for i in lati]
    for i in logi:
        for j in lati:
            temp = [str(i),str(j)]
            result.append(temp)
    return result

def get_data(request):
    if request.method == 'POST':
        x1 = request.POST.get('x1')
        y1 = request.POST.get('y1')
        x2 = request.POST.get('x2')
        y2 = request.POST.get('y2')
        #print(x1,y1,x2,y2)
        #print(type(x1))
        x1 = float(x1)
        #print(type(x1))
        y1= float(y1)
        x2 = float(x2)
        y2 = float(y2)
        result = getpicture(x1, y1, x2, y2)
        print(result)
        getresult = [['-71.093054','42.346350'],['-71.093054','42.346350']]
        print(result[0])
        #print(getresult)
        #print(getresult[0][0])
        #print(type(result[0][0]))
        #print(len(result))
        for i in range(len(result)):
          url = "https://maps.googleapis.com/maps/api/streetview?size=600x600&location="+result[i][1]+","+result[i][0]+\
         "%20&fov=90&heading=90&pitch=10%20&key=AIzaSyAG4xG9lpMwqFx5Q52MsAeR_e4taTLCNPc"
          name = "C:/untitled1/boston_test1/5GImage15/" + result[i][0] + "_" + result[i][1] + "_" + '90' + ".jpg"
          download(url,name)
        #return redirect("http://127.0.0.1:8000/poleplanner/")
        #return render(request, "poleplanner.html")
    return render(request, "map.html")
        #print(input)

        #for i in range(len(result)):
            #url = "https://maps.googleapis.com/maps/api/streetview?size=600x600&location="+result[i][1]+","+result[i][0]+\
                 # "%20&fov=90&heading=90&pitch=10%20&key=AIzaSyAG4xG9lpMwqFx5Q52MsAeR_e4taTLCNPc"
            #name = "C:/Users/18367/Desktop/5GImage18/" + result[i][0] + "_" + result[i][1] + "_" + '90' + ".jpg"
            #download(url,name)


    #return render(request,"poleplanner.html")
    #return HttpResponse(input, content_type='image/jpg')

def get_map(request):
    return render(request,"map.html",)
def get_poleplanner(request):
    return render(request,"poleplanner.html",)

