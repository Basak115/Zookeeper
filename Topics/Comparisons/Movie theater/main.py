number_of_halls = int(input())
capacity = int(input())
halls_capacity = number_of_halls * capacity
number_of_viewers = int(input())
movie = number_of_viewers <= halls_capacity
print(movie)
