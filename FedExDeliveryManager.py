"""
Name: Devon Lee

Course: CS1430, Section 00,  Fall 2021

Assignment: Assignment 2

Purpose: Make FedEx more efficient

Input:   Number of deliveries and the locations of each one for a given route

Output:  Statistics about each route and a highlight of any particularly
         efficient routes

"""

"""
CONSTANTS
"""


"""
Fill in a short program description here. 
"""

ROUND_HUNDREDTHS = 2

# Arbitrary large number so that any normal route is shorter
SHORT_TRIP_DEFAULT = 1000000000000


def main():
    
    total_deliveries = 0
    total_distance = 0
    
    route_number = 0
    
    shortest_route = -1
    longest_route = -1
    shortest_route_distance = SHORT_TRIP_DEFAULT
    longest_route_distance = -1
    
    num_deliveries = input()
    while num_deliveries != "":
        route_number += 1
        
        num_deliveries = int(num_deliveries)
        print(num_deliveries)
        
        x_curr = 0
        y_curr = 0
        route_distance = 0
        shortest_trip_distance = SHORT_TRIP_DEFAULT
        longest_trip_distance = -1
        
        for i in range(num_deliveries):
            x_next_del, y_next_del = input().split(" ")
            x_next_del = int(x_next_del)
            y_next_del = int(y_next_del)
            print(x_next_del, y_next_del)
            
            trip_distance = abs(x_next_del - x_curr) + abs(y_next_del - y_curr)
            route_distance += trip_distance
            x_curr += x_next_del
            y_curr += y_next_del
            
            if trip_distance < shortest_trip_distance:
                shortest_trip_distance = trip_distance
            elif trip_distance > longest_trip_distance:
                longest_trip_distance = trip_distance
    
        average_trip_distance = float(route_distance) / num_deliveries
        average_trip_distance = round(average_trip_distance, ROUND_HUNDREDTHS)
        
        total_deliveries += num_deliveries

        if route_number == 1:
            shortest_route_distance = route_distance
            longest_route_distance = route_distance
        elif route_distance < shortest_route_distance:
            shortest_route_distance = route_distance
            shortest_route = route_number
        elif route_distance > longest_route_distance:
            longest_route_distance = route_distance
            longest_route = route_number
        
        print()
        print("** Statistics for route  #" + str(route_number) + " **")
        print("Shortest distance between deliveries:", shortest_trip_distance)
        print("Longest distance between deliveries:", shortest_trip_distance)
        print("Distance traveled:", route_distance)
        print("Average distance between deliveries:", average_trip_distance)
        
        input(num_deliveries)
        
    print("Total number of delivery routes:", route_number)
    print("Total number of deliveries:", total_deliveries)
    print("Total distance traveled:", total_distance)
    
    print(f"Route #" + str(shortest_route) + " has the shortest travel distance:", shortest_route_distance)
    print(f"Route #" + str(longest_route) + " has the longest travel distance:", longest_route_distance)
    
    print("Normal Termination.")


"""
Do not remove the code below this line!
"""

if __name__ == '__main__':
    main()