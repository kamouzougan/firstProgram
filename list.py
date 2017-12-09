a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
choice = int(input( " please enter your choice "))
"""for element in a :
         print(element) """
new_list = []
for i in a :
    if i < choice :
        new_list.append(i)

print (new_list)
