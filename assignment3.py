bs=int(input("Enter the base salary of an employee : "))
gs=0
if bs>1 and bs<=4000:
 hra=bs*0.10
 da=bs*0.50
 gs=bs+hra+da
 print("The total gross salary of an employee : ",gs)
elif bs>4000 and bs<=8000:
 hra=bs*0.20
 da=bs*0.60
 gs=bs+hra+da
 print("The total gross salary of an employee : ",gs)
elif bs>8000 and bs<=12000:
 hra=bs*0.25
 da=bs*0.70
 gs=bs+hra+da
 print("The total gross salary of an employee : ",gs)
else:
 hra=bs*0.30
 da=bs*0.80
 gs=bs+hra+da
 print("The total gross salary of an employee : ",gs)
