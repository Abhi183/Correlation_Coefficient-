#2018/06/25
#calcualtion of product moment correlation coefficient (r)
N=int(input("Enter number of data (n):"))
list=[]
list2=[]
list3 = []
for i in range(N):
    X = int(input("Enter the values of (x):"))
    Y = int(input("Enter the values of (y):"))

    list3.append(X * Y)
    list.append(X)
    list2.append(Y)
print("x=",list)
print("y=", list2)

#now calculating summation x and y
sum_x=0
sum_y=0
sxy=0 #calulating Sxy

for j in range(N):
    sxy=sxy+ list3[j]
    sum_x=sum_x + list[j]
    sum_y= sum_y + list2[j]
print ("\u03A3x=", sum_x)
print("\u03A3y=",sum_y)

#now calculating summation of x square and y square
list=[ list[k]**2 for k  in range(N)]
list2=[ list2[k]**2 for k  in range(N)]
sum_sq_x= sum(list)
sum_sq_y= sum(list2)
print("\u03A3x\N{SUPERSCRIPT TWO}", sum_sq_x)
print("\u03A3y\N{SUPERSCRIPT TWO}", sum_sq_y)

#now calculating Sxx, Syy
sxx= int(sum_sq_x - ((sum_x)**2)/N)
syy=int(sum_sq_y - ((sum_y)**2)/N)
print ("Sxx=",sxx)
print ("Syy=",syy)
print ("Sxy=", sxy)

#calculating r
r = float(sxy/ ((sxy*sxx)**1/2))
print("Product moment correlation coefficient(r)=",r)