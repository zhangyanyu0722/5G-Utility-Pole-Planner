# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 15:15:20 2019

@author: 18367
"""
import urllib.request

def download(url, name):

    conn = urllib.request.urlopen(url) 
 
    f = open(name, 'wb')  

    f.write(conn.read())

    f.close()

    print('Pic Saved!') 
    
def getpicture(x1,y1,x2,y2):
    result = []
    logi = []
    logi.append(x1)
    while x1<x2:
        x1 = x1 + 0.0009
        logi.append(x1)
    logi = [("%.6f" % i) for i in logi]
    lati = []
    lati.append(y1)
    while y1>y2:
        y1 = y1 - 0.00034
        lati.append(y1)
    lati = [("%.6f" % i) for i in lati]
    for i in logi:
        for j in lati:
            temp = [i,j]
            result.append(temp)
    return result
    
    
result = getpicture(-71.124554,42.353150,-71.093398,42.346014)    

for i in range(len(result)):
    url = "https://maps.googleapis.com/maps/api/streetview?size=600x600&location=" + result[i][1] + "," + result[i][0] + "%20&fov=90" + "&heading=90" + "&pitch=10%20&key="+ "" 
    name = "C:/Users/18367/Desktop/5GImage12/" + result[i][0] + "_" + result[i][1] + "_" + '90' + ".jpg" 
    download(url,name)
    
