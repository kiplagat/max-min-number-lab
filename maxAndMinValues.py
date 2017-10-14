def findMaxMin(list):
 minval = min(list)
 maxval = max(list)
 if minval == maxval:
  return [maxval]
 return [minval, maxval]

print (findMaxMin([2,5,10,1,15]))
 



