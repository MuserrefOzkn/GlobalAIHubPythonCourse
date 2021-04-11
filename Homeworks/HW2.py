#Get username and password values from the user
# Check the values in an if statement and tell the user ir they were successful

#Question 1
dct = {"Username":"MÜŞERREF", "Password":"12345"}


username = input("Username: ")
password = input("Password: ")

dct2 = {"Username":username.upper(), "Password":password}

if dct == dct2:
  print("Giriş başarılı")
else:
  print("Giriş başarısız. Tekrar deneyiniz")
