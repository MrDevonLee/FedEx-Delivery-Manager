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


def main():
    
    pass
    
    total_deliveries = 0
    total_distance = 0
    
    shortest_route_distance = 100000000
    longest_route_distance = -1
    
    route_number = 0 # Temporary
    
    while route_number < 5:
        
        route_number += 1
        
        x_curr = 0
        y_curr = 0
        route_distance = 0
        shortest_trip_distance = 100000000
        longest_trip_distance = -1
        
        num_deliveries = int(input())
       
        for i in range(num_deliveries):
            x_next_del, y_next_del = int(input().split(" "))
            
            trip_distance = abs(x_curr - x_next_del) + abs(y_curr - y_next_del)
            route_distance += trip_distance
            
            if trip_distance < shortest_trip_distance:
                shortest_trip_distance = trip_distance
            elif trip_distance > longest_trip_distance:
                longest_trip_distance = trip_distance
    
            x_curr += x_next_del
            y_curr += y_next_del
            
        average_trip_distance = float(route_distance) / num_deliveries
        
        total_deliveries += num_deliveries

        if route_distance < shortest_route_distance:
            shortest_route_distance = route_distance
            shortest_route = route_number
        elif route_distance > longest_route_distance:
            longest_route_distance = route_distance
            longest_route = route_number
        
        print("** Statistics for route  #" + route_number + "**")
        print("Shortest distance between deliveries: " + shortest_trip_distance)
        print("Longest distance between deliveries: " + shortest_trip_distance)
        print("Distance traveled: " + route_distance)
        print("Average distance between deliveries: " + average_trip_distance)
        
    print("Total number of delivery routes: " + route_number)
    print("Total number of deliveries: " + total_deliveries)
    print("Total distance traveled: " + total_distance)
    
    print("Route # 1 has the shortest travel distance: " + shortest_route_distance)
    print("Route # 1 has the longest travel distance: " + longest_route_distance)
    
    print("Normal Termination.")


"""
Do not remove the code below this line!
"""

if __name__ == '__main__':
    main()