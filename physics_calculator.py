print("PHYSICS FORMULA CALCULATOR")

print("1. Speed = Distance / Time")
print("2. Force = Mass × Acceleration")
print("3. Work = Force × Distance")
print("4. Density = Mass / Volume")
print("5. Power = Work / Time")

choice = int(input("Select a formula (1-5): "))

if choice == 1:
    distance = float(input("Enter distance: "))
    time = float(input("Enter time: "))
    print("Speed =", distance / time, "m/s")

elif choice == 2:
    mass = float(input("Enter mass: "))
    acceleration = float(input("Enter acceleration: "))
    print("Force =", mass * acceleration, "N")

elif choice == 3:
    force = float(input("Enter force: "))
    distance = float(input("Enter distance: "))
    print("Work =", force * distance, "J")

elif choice == 4:
    mass = float(input("Enter mass: "))
    volume = float(input("Enter volume: "))
    print("Density =", mass / volume, "kg/m³")

elif choice == 5:
    work = float(input("Enter work: "))
    time = float(input("Enter time: "))
    print("Power =", work / time, "W")

else:
    print("Invalid choice!")
