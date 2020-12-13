def Compound(Balance, InterestRate, TargetBalance):
  Year = 1
  while Balance < TargetBalance:
    Interest = Balance * InterestRate
  
    
    Year = Year + 1
    Balance = Balance + InterestRate
  print("Year {}: New balance = £{:.2f}".format(Year, Balance))

Compound(100,0.04,200)