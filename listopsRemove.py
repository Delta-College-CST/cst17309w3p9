# This program demonstrates various Python list functions
# mainly that remove elements

airports = ["MBS", "DTW", "FNT", "LAN"]

airports.remove("LAN")

print(airports)

airports.extend(["TVC","YYZ","JFK"])

print(airports)

europeair = ["BHX","CDG","AMS"]

airports = airports + europeair

print(airports)

deleted = airports.pop(6)

print(deleted)

print(airports)

airports.clear()

print(airports)
