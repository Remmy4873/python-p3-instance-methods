#!/usr/bin/env python3

class Person:
    # Instance method to print a greeting
    def talk(self):
        print("Hello World!")

    # Instance method to simulate walking
    def walk(self):
        print("The person is walking.")

# Example usage
john = Person()
john.talk()  # Output: Hello World!
john.walk()  # Output: The person is walking.
