def sqroot(X):
  Root = X
  print(Root)
  
  while (Root**2) != X: 
    Root = 0.5*(Root+(X/Root)) 
    print(Root)

sqroot(15)
  