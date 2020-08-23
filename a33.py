import tempconv
c=int(input("Enter the degree of Celcius temperature : "))
d=tempconv.ctof(c)
f=int(input("Enter the degree of Fahrenheit temperature : "))
g=tempconv.ftoc(f)
print(c,"celcius temperature 
= ",d,"Fahrenheit")
print(f,"fahrenheit temperature = ",g,"Celcius")