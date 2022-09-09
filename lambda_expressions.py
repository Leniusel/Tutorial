#Name: Doris Tran
#Date: September 8, 2022
#Lambda Expressions

#Excercise 1: Squaring the numbers in a list
my_list = [5, 4, 3]
#print squared list with lambda
new_list = list(map(lambda num: num*num, my_list))
print(new_list)


#Excercise 2: Sorting using lambda
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
#a.sort(key = lambda x: x[0])    #sort by 1st position
a.sort(key = lambda x: x[1])     #sort by 2nd position
print(a)                         #print the tuple
