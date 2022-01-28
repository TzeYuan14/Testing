# Program to find the sum of all numbers stored in a list

#List of numbers
numbers =[1, 6, 8, 7, 4, 6, 2, 9, 5, 3]
sum = 0

for val in numbers:
    sum = sum + val**2

print("The sum of square of numbers is", sum)

# range(start, stop, step_size)
print(list(range(1, 10, 2)))


genre = ["Poki", "Haku", "Nagi"]

for i in range(len(genre)):
    print("I like", genre[i])

A = [1,2,3]
B = [6,5,4]
C = [7,8,9]
X = [A] + [B] + [C]

print (X)