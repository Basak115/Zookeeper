days = int(input())
food_per_day = int(input())
fly_cost = int(input())
nights = int(input())
sum = days * food_per_day + fly_cost * 2 + nights * (days - 1)
print(sum)
