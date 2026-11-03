user_workouts = []

while True:

    print("╔══════════════════════╗")
    print("║[1] Add exercise    ║")
    print("║══════════════════════╣")
    print("║[2] Show workout    ║")
    print("╠══════════════════════╣")
    print("║[3] Delete workout  ║")
    print("╠══════════════════════╣")      
    print("║[4] Exit            ║")
    print("╚══════════════════════╝")
    print()
    print(" Choose: [1][2][3][4] ")
    print()
    user_choice = input(" Your choice: ")
  

    if user_choice == "1":
            while True:
                name = str(input(" Exercise name: "))
                if name: 
                    break
                print("[!] Exercise name cannot be empty.")

            while True:
                try:
                    sets = int(input(" Number of sets: "))
                    if sets > 0:
                        break
                    print("[!] Number of serie must be greather than 0.")
                except ValueError:
                    print("[!] Error: You must enter a whole number.")

            while True:
                try: 
                    reps = int(input(" Number of reps: "))
                    if reps > 0:
                        break
                    print("[!] Number of reps must be greather than 0.")
                except ValueError:
                    print("[!] Error: You must enter a whole number.")

            while True:
                try:
                    weight = float(input(" Kilograms: "))
                    if weight >= 0:
                        break
                    print("[!] Weight cannot be negative.")
                except ValueError:
                    print("[!] Error: You must enter a number (use a dot for decimals).")

            workout_input = {
                "name" : name,
                "sets" : sets,
                "reps" : reps,
                "weight" : weight,
            }

            user_workouts.append(workout_input)

            print(f"\n[+] {name} added successfully!")
        


    elif user_choice == "2":
        if not user_workouts:
            print("\n[!] Your workout list is empty!")
        else:
            print("--- Your workout list ---")
            print()
            for index, exercise in enumerate(user_workouts, 1):
                volume = exercise['weight'] * exercise['sets'] * exercise['reps']

                if volume.is_integer():
                          volume = int(volume)
              
                print(f"[{index}] {exercise['name']} {exercise['sets']} x {exercise['reps']} x {exercise['weight']}kg - vol. [{volume}kg]")

    elif user_choice == "3":
        if not user_workouts:
            print()
            print("[!] There are no exercises to delete.")
            print()
        else:
            print("--- Delete an exercise ---")
            print()

            for index, exercise in enumerate(user_workouts, 1):
                print(f"[{index}] {exercise['name']}")
                print()
        
            while True:
                try:
                    print("[?] Which exercise do you want to delete?")
                    choice = int(input(" Your choice: "))

                    if 1 <= choice <= len(user_workouts):
                        deleted_exercise = user_workouts.pop(choice - 1)
                        print(f"\n[-] {deleted_exercise['name']} has been deleted successfully!")
                        break
                    else:
                        print(f"[!] Invalid number. Please choose between 1 and {len(user_workouts)}.")
                except ValueError:
                    print("[!] Error: You must enter a valid whole number.")
                

    elif user_choice == "4":
        print()
        print(" Goodbye! Have a great workout!")
        break

    else:
        print()
        print("\n[!] Invalid choice! Please choice [1] or [2] or [3]")
        print()
