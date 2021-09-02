"""
Name: Devon Lee

Course: CS1430, Section 00,  Fall 2021

Assignment: Assignment 2

Purpose: Provide statistics about delivery routes to make the fleet more aware
         of how efficient each driver's choices are.

Input:   Number of deliveries in a route followed by the location of each in
         Cartesian coordinates, each on a new line. This cycle repeats for each
         delivery in the system.

Output:  An echo of the input, statistics for each route, and statistics about
         the entire set of routes

"""

"""
CONSTANTS
"""
ROUND_HUNDREDTHS = 2

"""
Description: This program takes in location data for deliveries on a fleet of
             FedEx trucks and calculates statistics about the delivery routes.
             These statistics are reported so that the efficiency of each route
             can be easily accessed.
"""


def main():
    route_number = 0  # Increments with every route as an index
    total_deliveries = 0
    total_distance = 0
    
    num_deliveries = input()  # Priming read
    while num_deliveries != "":
        num_deliveries = int(num_deliveries)
        print(num_deliveries)
        
        x_current = 0
        y_current = 0
        route_distance = 0
        
        for i in range(num_deliveries):
            x_next_del, y_next_del = input().split()
            x_next_del = int(x_next_del)
            y_next_del = int(y_next_del)
            print(x_next_del, y_next_del)
            
            delta_x = x_next_del - x_current
            delta_y = y_next_del - y_current
        
            trip_distance = abs(delta_x) + abs(delta_y)
            
            x_current += delta_x
            y_current += delta_y
            route_distance += trip_distance
            
            if i == 0:  # Sets variables with first delivery
                shortest_trip_distance = trip_distance
                longest_trip_distance = trip_distance
            elif trip_distance < shortest_trip_distance:
                shortest_trip_distance = trip_distance
            elif trip_distance > longest_trip_distance:
                longest_trip_distance = trip_distance

        route_number += 1
        total_deliveries += num_deliveries
        total_distance += route_distance
        
        if num_deliveries == 0:
            average_trip_distance = 0
        elif num_deliveries == 1:
            average_trip_distance = route_distance
        else:
            average_trip_distance = float(route_distance) / num_deliveries
            average_trip_distance = round(average_trip_distance,
                                          ROUND_HUNDREDTHS)
        
        if route_number == 1:  # Sets variables with first route
            shortest_route = route_number
            longest_route = route_number
            shortest_route_distance = route_distance
            longest_route_distance = route_distance
        elif route_distance < shortest_route_distance:
            shortest_route_distance = route_distance
            shortest_route = route_number
        elif route_distance > longest_route_distance:
            longest_route_distance = route_distance
            longest_route = route_number
        
        print()
        print(f"**Statistics for route #{route_number}**")
        print(f"Shortest distance between deliveries: {shortest_trip_distance}")
        print(f"Longest distance between deliveries: {longest_trip_distance}")
        print(f"Distance traveled: {route_distance}")
        print(f"Average distance between deliveries:"
              f" {average_trip_distance:.2f}")
        print()
        
        # input(num_deliveries)
        num_deliveries = input()
    
    print(f"Total number of delivery routes: {route_number}")
    print(f"Total number of deliveries: {total_deliveries}")
    print(f"Total distance traveled for all routes: {total_distance}")
    
    print()
    print(f"Route #{shortest_route} has the shortest travel distance:"
          f"{shortest_trip_distance}")
    print(f"Route #{longest_route} has the shortest travel distance:"
          f"{longest_trip_distance}")

    print()
    print("Normal Termination.")


"""
Do not remove the code below this line!
"""

if __name__ == '__main__':
    main()
