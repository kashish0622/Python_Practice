#Print numbers from 1 to 100
'''count = 1
while count<=100:
    print(count)
    count += 1

#Print numbers from 100 to 1
count = 100
while count>=1:
    print(count)
    count -= 1
'''
# Print the multiplication table of a number n
'''
number = int(input("Enter the number: "))
print("\n--- Table of entered number is:  ---")

i = 1
while i<=10:
    print(number*i)
    i += 1

# Print the elements using a loop
i = 1
while i<=10:
    print(i*i)
    i += 1
'''
#Search for a number x in this tuple using loop:
tup1 = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = int(input("Enter a number to search: "))

i = 0 
while i < len(tup1):
   if tup1[i] == x:
    print(x, "number is present in tuple")
    break
   i+=1
else:
   print(x, "number is not present in tuple")