num =int( input("Please give me a number"))

"""for element in x :

  print(element)"""
listRange = list(range(1,num + 1))

divisorList = []
for i in listRange :
 if  num % i == 0 :
  divisorList.append(i)
  print(listRange)
print(divisorList  )



