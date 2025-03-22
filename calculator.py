def add(x,y):
  return x+y
def subtract(x,y):
  return x-y
def multiply(x,y):
  return x*y
def divide(x,y):
  if y!=0:
    return x / y
  else:
    return "error! divisiopn by zero."

def calculator():
  print("simple calculator")
  print("choose operation:")
  print("1. add")
  print("2. subtract")
  print("3. multiply")
  print("4. divide")

  while True:
    choice = input("enter choice(1/2/3/4):")

    if choice in ['1','2','3','4']:
      num1 = float(input("enter first number:"))
      num2 = float(input("enter second number:"))
      if choice == '1':
          print(f"The result is: {add(num1, num2)}")
      elif choice == '2':
          print(f"The result is: {subtract(num1, num2)}")
      elif choice == '3':
          print(f"The result is: {multiply(num1, num2)}")
      elif choice == '4':
          print(f"The result is: {divide(num1, num2)}")

      next_claculation= input("do you want to perform another calculation? (yes/no):")
      if next-calculation.lower() !='yes':
        break
    else:
      print("invalid input")
# run the calculator
calculator()
