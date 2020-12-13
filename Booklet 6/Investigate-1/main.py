def LCD(Number1, Number2):
  Counter = 1
  while Counter % Number1 != 0 or Counter % Number2 !=0:
    Counter = Counter + 1
  return Counter

Number1 = 100
Number2 = 50
Result = LCD(Number1, Number2)
print("The LCD of {} and {} is {}".format(Number1, Number2, Result))