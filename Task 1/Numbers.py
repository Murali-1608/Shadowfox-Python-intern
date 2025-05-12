#code for 1st problem in numbers
def format_number(num, specifier):
    return format(num, specifier)

result = format_number(145, 'o')
print("Octal representation of the decimal number 145: "+result)
print()

#code for the 2nd problem in numbers
r=84
pi=3.14
ca=pi*r*r
print(f"Area of the pond: {ca}square meters")
print(f"Total water in the pond: {int(ca)} litres")
print()

#code for 3rd problem in numbers
distance = 490
time_minutes = 7
time_seconds = time_minutes * 60
speed = distance / time_seconds
print(f"Speed: {int(speed)} m/s")
print()