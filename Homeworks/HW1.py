#Explain your work

#Question 1
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
