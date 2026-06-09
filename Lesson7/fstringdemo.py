import math
print(f"Value of pi is {math.pi:.2f}") #f-string

pi = 3.141574334
print(f"{pi:.2f}") #rounding to 2 decimal places

num = 123
print(f"Number is {num:10}") #right aligned with 10 spaces 

print(f"{num:<10}") #left aligned with 10 spaces
print(f"{num:^10}") #center aligned with 10 spaces

value = 12384381374
print(f"{value:,}") #with comma as thousand separator

m1 = 0.876
print(f"Value of m1 is {m1:.2%}") #percentage format with 2 decimal places

v1 = 25
print(f"binary of v1 is {v1:b}") #binary format
print(f"octal of v1 is {v1:o}") #octal format
print(f"hexadecimal of v1 is {v1:x}") #hexadecimal format

# %d - decimal integer 
# %f - floating point number
# %s - string
# %x - hexadecimal integer
# %o - octal integer
# %e - scientific notation
# %g - general format (uses %f or %e depending on the value)

name = "Megha"
phone = 1234567890
salary = 50000.75
print("Name: %s, Phone: %d, Salary: %.2f" % (name, phone, salary)) #using old style formatting  
