'''
chapter 3
1.Write a python program to display a user entered name followed by Good 
Afternoon using input () function.

2. Write a program to fill in a letter template given below with name and date.

letter = ''\' 

Dear <|Name|>,

You are selected!

<|Date|>

'\''

3. Write a program to detect double space in a string.

4. Replace the double space from problem 3 with single spaces.

5. Write a program to format the following letter using escape sequence 

characters.

letter = "Dear Harry, this python course is nice. Thanks!" '''

print (" good morning 🌄 " ,name)

a = '''Dear <|Name|>,
You are  selected!
<|Date|>
'''

b = a.replace("<|Name|>" ,name)
c = a.find("  ")

print (b,c)
print("Dear Harry,\t this python course is nice. Thanks")
# chapter 4 prectice set
''' 
1. Write a program to store seven fruits in a list entered by the user.

2. Write a program to accept marks of 6 students and display them in a sorted 

manner.

3. Check that a tuple type cannot be changed in python.

4. Write a program to sum a list with 4 numbers.

5. Write a program to count the number of zeros in the following tuple: '''
list =[]
for i in range(7): 
    fruit = input(f"enter {i} fruits name: ")
    list.append(fruit)
print (list)
list.clear()
for i in range (6):
    a = int(input(f"enter your marks of {i} subject "))
    list.append(a)
print (list)
list.sort()
print (list)

tuple =(6,28,"coko")
#tuple[2] = "NEW"

print (sum(list))

