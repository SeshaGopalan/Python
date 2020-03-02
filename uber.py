location=['tambaram','chrompet','pallavaram','meenambakkam','guidy']
transport=['bike','auto','mini','micro','prime']
print('Location :' +str(location))
slocation = input('Enter the source : ')
source = location.index(slocation)
#print(source)
dlocation = input('Enter the desgination :')
designation = location.index(dlocation)
#print(designation)
print('Transport_type :' +str(transport))
transport_type=input('Enter the transport mode: ')
transport_type=transport_type.lower()
mode=(transport.index(transport_type)*2+20)
#print(mode)
if(source>=0 and designation>=0 and mode>=0):
 fare=(source+ designation)*50 +mode
 print('Total fare :₹' +str(fare))
 print('Enjoy your ride!!!')
else:
 print('Invaild source,designation &transport type correctly')