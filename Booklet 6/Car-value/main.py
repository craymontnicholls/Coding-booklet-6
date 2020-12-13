
def depreciation(year, value, min_resale):
  print("Year {}: value = £{:.2f} ".format(year, value))
  year = 1
  value = value * 0.7
  print("Year {}: value = £{:.2f} ".format(year, value))
  year = year + 1


  

  while value >= min_resale:
    value = value * 0.8
    print("Year {}: value = £{:.2f} ".format(year, value))
    year = year + 1
      
 



  
 

  


depreciation(2020, 12500, 2000)