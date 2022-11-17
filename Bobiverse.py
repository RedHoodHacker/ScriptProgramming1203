#!/usr/bin/python3 

#List of people
people = ["Dr. Landers", "Guppy", "Bob 2.0"]

#Prints out all the people in the list 
for person in people:
    print(person)

#Prints the list joined with commas
print(", ".join(people))

#Adds the string Riker to the end of the list people
people.append("Riker")
print(people)

#Adds the string Colonel Butterworth at the front of the list people
people.insert(0, "Colonel Butterworth")
print(people)

#Printed with Commas 
print(", ".join(people))

#Replaces the 0 index with a different person
people[0] = "Bill"
print(people)

#Deletes the last element of the list, Riker 
people.pop()
print(people)

#Added with commas 
print(", ".join(people))

