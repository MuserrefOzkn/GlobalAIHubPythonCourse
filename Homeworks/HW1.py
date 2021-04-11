#Create a list ans swap the second half of the list with the first half of the list
#print this list on the screen

#Question 1
#1
mylist = []

while True:
  value = input("Please enter an integer value (press q for quit the number entering): ")
  
  if value == "q":
    break
  
  mylist.append(value)

if len(mylist) %2 != 0:
  first_half = mylist[:(int(len(mylist2)/2))]
  second_half = mylist[(int(len(mylist2)/2)):]
    
else:
  first_half = mylist[:int(len(mylist)/2)]
  second_half = mylist[int(len(mylist)/2):]

first_half, second_half = second_half, first_half
first_half.extend(second_half)

print(first_half)

#2
#Ask the user to input a single digit integer to a variable 'n'
#Then, print out all of the even numbers from 0 to n(including n)

value2 = int(input("Please enter a singel gidit integer number : "))

while True:
  if value2 > 9:
    value2 = int(input("Please enter a SINGEL DIGIT integer number: "))
  else:
    break

for i in range(value2+1):
  if i % 2 == 0:
    print(i)
