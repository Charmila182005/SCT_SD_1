# Task 1: Temperature Converter
# Software Development Internship - SkillCraft Technology
# Author: Charmila Reddy L

def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5 / 9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9 / 5 + 32


print("=== Temperature Converter ===")
print("C - Celsius")
print("F - Fahrenheit")
print("K - Kelvin")

try:
    scale = input("Enter scale (C/F/K): ").upper()
    value = float(input("Enter temperature value: "))

    if scale == 'C':
        print("Fahrenheit:", celsius_to_fahrenheit(value))
        print("Kelvin:", celsius_to_kelvin(value))

    elif scale == 'F':
        print("Celsius:", fahrenheit_to_celsius(value))
        print("Kelvin:", fahrenheit_to_kelvin(value))

    elif scale == 'K':
        print("Celsius:", kelvin_to_celsius(value))
        print("Fahrenheit:", kelvin_to_fahrenheit(value))

    else:
        print("Invalid scale!")

except ValueError:
    print("Enter a valid number!")
