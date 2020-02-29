list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q']
n = str(input("Enter the string util loop execute or 'quit' :"))
if(n.lower()=='q' or n.lower()=='quit'):
 for i in list:
  print(i,end=' ')
  if i == n.lower():
   break
else:
 for i in list:
    print(i)
    if i == n.lower():
     break
