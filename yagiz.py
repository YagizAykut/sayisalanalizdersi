import math 

pi=math.pi
x=pi/5
taylorbirinci=(math.pow((-1),0))*(x**(2*0))/(math.factorial((2*0)))
taylorikinci=(-1**1)*(x**(2*1))/(math.factorial((2*1)))
print(taylorbirinci)
print(taylorikinci+taylorbirinci)
cosDegeri=math.cos(x)
birincikesmehatasi=taylorbirinci-cosDegeri
ikincikesmehatasi=taylorbirinci+taylorikinci-cosDegeri
print("kesme hatasi 1: {0}".format(ikincikesmehatasi))
print("kesme hatasi 2: {0}".format(birincikesmehatasi))