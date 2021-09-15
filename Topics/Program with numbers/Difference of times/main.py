a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

first_event = a * 60 * 60 + b * 60 + c
second_event = d * 60 * 60 + e * 60 + f
num_of_seconds = second_event - first_event
print(num_of_seconds)
