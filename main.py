user_workouts = []

while True:

    print("\n")
    print("[1] Add exercise")
    print("[2] Show workout")
    print("[3] Exit")
    print()
    print("Choose option: [1] [2] [3]")


    user_choice = input("Your choice: ")

    if user_choice == "1":
            while True:
                name = str(input("Exercise name: "))
                if name: 
                    break
                print("[!] Exercise name cannot be empty.")

            while True:
                try:
                    sets = int(input("Number of sets: "))
                    if sets > 0:
                        break
                    print("[!] Number of serie must be greather than 0.")
                except ValueError:
                    print("[!] Error: You must enter a whole number.")

            while True:
                try: 
                    reps = int(input("Number of reps: "))
                    if reps > 0:
                        break
                    print("[!] Number of reps must be greather than 0.")
                except ValueError:
                    print("[!] Error: You must enter a whole number.")

            while True:
                try:
                    weight = float(input("Kilograms: "))
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
                print(f"[{index}] {exercise['name']} {exercise['sets']} x {exercise['reps']} x {exercise['weight']}kg")
                


    elif user_choice == "3":
        print()
        print("Goodbye! Have a great workout!")
        break

    else:
        print()
        print("\n[!] Invalid choice! Please choice [1] or [2] or [3]")

    
    

        

    