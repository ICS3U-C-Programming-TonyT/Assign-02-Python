#!/usr/bin/env python3

# Created by: Tony Tran
# Created on: September. 25, 2023
# This program does Surface Area, Volume, and Lateral Surface Area using the user input


# Importing Modules
import os
import math


# Function to Calculate Surface Area
def surface_area_calculate(length, width, height, unit):
    # Declaring Variables for Length, Width, Height, Unit
    length = length
    width = width
    height = height
    unit = unit
    # Calculate Surface Area and rounding the decimals up to 2
    surface_area = round(
        length * width
        + length * math.sqrt(((width / 2) ** 2) + height**2)
        + width * math.sqrt(((length / 2) ** 2) + height**2),
        2,
    )
    # Print Surface Area
    print(f"Surface Area: {surface_area}{unit}")


# Function to Calculate Volume
def volume_calculate(length, width, height, unit):
    # Declaring Variables for Length, Width, Height, Unit
    length = length
    width = width
    height = height
    unit = unit
    # Calculate Volume and rounding the decimals up to 2
    volume = round(length * width * height / 3, 2)
    # Print Volume
    print(f"Volume: {volume}{unit}")


# Function to Calculate Lateral Surface Area
def lateral_surface_area(length, width, height, unit):
    # Declaring Variables for Length, Width, Height, Unit
    length = length
    width = width
    height = height
    unit = unit
    # Calculate Lateral Surface Area and rounding the decimals up to 2
    lateral_surface_area = round(
        length * math.sqrt((width / 2) ** 2 + height**2)
        + width * math.sqrt((length / 2) ** 2 + height**2),
        2,
    )
    # Print Lateral Surface Area
    print(f"Lateral Surface Area: {lateral_surface_area}{unit}")


# Main Function
def main():
    # Prints Options
    print(
        "Right Rectangular Pyramid\n[1] Surface Area\n[2] Volume\n[3] Lateral Surface Area\n[4] All"
    )
    # Gets Options
    options = int(input("Which Formula would you like to use?\n"))
    # Clears Terminal
    os.system("clear")
    # Getting Length, Width, Height, Unit
    length = float(input("Base Length: "))
    width = float(input("Base Width: "))
    height = float(input("Pyramid Height: "))
    unit = str(input("Unit: ")).lower()
    if options == 1:
        surface_area_calculate(length, width, height, unit)
    elif options == 2:
        volume_calculate(length, width, height, unit)
    elif options == 3:
        lateral_surface_area(length, width, height, unit)
    elif options == 4:
        surface_area_calculate(length, width, height, unit)
        volume_calculate(length, width, height, unit)
        lateral_surface_area(length, width, height, unit)


if __name__ == "__main__":
    main()
