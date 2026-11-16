def speed():
    print("\nSPEED")
    print("Formula: Speed = Distance / Time")
    print("= 10 / 60")
    print("Answer = 0.167 m/s")


def force():
    print("\nFORCE")
    print("Formula: Force = Mass x Acceleration")
    print("= 2 x 15")
    print("Answer = 30 N")


def work():
    print("\nWORK DONE")
    print("Formula: Work = Force x Distance")
    print("= 30 x 10")
    print("Answer = 300 J")


def kinetic_energy():
    print("\nKINETIC ENERGY")
    print("Formula: KE = 1/2 x Mass x Velocity^2")
    print("= 1/2 x 2 x 5^2")
    print("Answer = 25 J")


def density():
    print("\nDENSITY")
    print("Formula: Density = Mass / Volume")
    print("= 2 / 3")
    print("Answer = 0.667 kg/m^3")


while True:
    print("\n===== PHYSICS CALCULATOR =====")
    print("1. Speed")
    print("2. Force")
    print("3. Work Done")
    print("4. Kinetic Energy")
    print("5. Density")
    print("6. Display All Answers")

    choice = input("\nSelect an operation (1-6): ")

    if choice == "1":
        speed()
    elif choice == "2":
        force()
    elif choice == "3":
        work()
    elif choice == "4":
        kinetic_energy()
    elif choice == "5":
        density()
    elif choice == "6":
        speed()
        force()
        work()
        kinetic_energy()
        density()
    else:
        print("Invalid choice!")

    again = input("\nWould you like to continue? (yes/no): ")

    if again.lower() != "yes":
        print("Thank you for using the Physics Calculator!")
        break