# _*_ coding: utf-8 _*_
__author__ = 'yanyuzhang'  
 
import urllib.request
 
def download(url, name):

    # url = "http://pic2.sc.chinaz.com/files/pic/pic9/201309/apic520.jpg"

    conn = urllib.request.urlopen(url) 
 
    f = open(name, 'wb')  

    f.write(conn.read())

    f.close()

    print('Pic Saved!')  

 
fp = open("/home/ece-student/Desktop/shared/5G/map_genarator/boston.txt","r") 


for line in fp.readlines():

    line =  (lambda x: x[1:25])(line)  #选取从第十一个到第十三个字符

    # line =  (lambda x: x[11:-11])(line)

    print(line)

    zu = line.split('_')

    jin = zu[0]

    wei = zu[1]

    heading = zu[2]

    print(jin + "\n" + wei + "\n" + heading + "\n")

    name = "/home/ece-student/Desktop/shared/5G/map_genarator/boston_" + jin + "_" + wei + "_" + heading + "10%20.JPG"

    url = "https://maps.googleapis.com/maps/api/streetview?size=600x600&location=" + jin + "," + wei + "%20&fov=90" + "&heading=" +heading + "&pitch=10%20&key="+ ""
    print(name)

    print(url)

    download(url, name)

fp.close()



