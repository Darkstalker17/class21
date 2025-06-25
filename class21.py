'''Lists
Outline:
Write a program to perform the following operations on a List:
1. Create an empty list 2. A list with elements 3. Use * operator 4.
Reverse a list'''
myList = [1,2,3,4,5]*3
print(myList)
list = ["r","a","c","e","c","a","r"]
v = list[::-1]
print(v)

'''Word Matching
Outline:
Write a Python program to count the number of strings where the string
length is two
or more, and the first and last characters are the same from a given
list of strings.'''
def reverse(word):
    character = 0
    myList = []
    for i in word:
        if len(i)>1 and i[0]==i[-1]:
            character += 1
            myList.append(i)
    print("List of words with the first and last chracter same are",myList)
    return character
a = reverse(["abc","pip","pat","1331","deeed","wfbiowbuefb"])
print(a)
'''Play with Lists
Outline:
Write a Python program to find the sum and average of the list.
The average of the list is defined as the sum of the elements divided
by the number of the elements.
Also, find the largest and the smallest number in the list.'''
new = [1,2,3909,4,3,6,23,476,23,1,23,2]
sum = 0
for i in new:
    sum += i
print(sum)
num = len(new)
avg = sum/num
print("The average of the list is",avg)
print(max(new))
print(min(new))

new.sort()
print(new)