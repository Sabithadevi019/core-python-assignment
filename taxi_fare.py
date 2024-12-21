def taxi_fare(distance):
    base=50
    distance_fare=10*distance
    total=base+distance_fare
    return total
trips = [5, 10, 3]
total= 0
for i in range(len(trips)):
    fare = taxi_fare(trips[i])
    print(f"Trip {i+1}: ${fare}")
    total += fare
print(f"Total Fare: ${total}")
