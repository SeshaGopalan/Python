number_list=[]
number_list1=[1]
number_list2=[]
number_list3=[]
number_list4=[]
number_list5=[]
N=int(input('Enter the range of number series'))
for i in range(1,N+1):
 number_list.append(i)
 if(i%2==0):
  a=number_list1[-1]*2
  even=i*i
  number_list1.append(a)
  number_list2.append(even)
  number_list3.append(i)
  number_list4.append(even)
  number_list5.append(even)
 else:
  if(i==number_list1[-1]):
    number_list2.append(i)
    number_list3.append(i)
    number_list4.append(i)
    number_list5.append(i)
    continue
  else:
   x=number_list1[-1]
   y= round(x*3/2)
   odd=i*i
   cube=i*i*i
   number_list1.append(y)
   number_list2.append(odd)
   number_list3.append(odd)
   number_list4.append(odd)
   number_list5.append(cube)
print(number_list)
print(number_list1)
print(number_list2)
print(number_list3)
print(number_list4)
print(number_list5)