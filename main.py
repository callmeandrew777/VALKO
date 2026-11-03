import json
import os

DATABASE_FILE = "workouts.json"

def load_workouts():
    if not os.path.exists(DATABASE_FILE):
        return []
    try:
        with open(DATABASE_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("[!] Error: The database file is corrupted.")
        return []

def save_workouts(workouts):
    with open(DATABASE_FILE, "w", encoding="utf-8") as file:
        json.dump(workouts, file, indent=4, ensure_ascii=False)

user_workouts = load_workouts()


        

def get_valid_number(prompt, field_name, num_type=int, allow_zero=False):
    while True:
        try:
            value = num_type(input(prompt))
            if allow_zero and value >= 0:
                return value
            if not allow_zero and value >0:
                return value

            if allow_zero:
                print(f"[!] {field_name} cannot be negative.")
            else:
                print(f"[!] {field_name} must be greater than 0.")
        except ValueError:
            if num_type == int:
                print("[!] Error: You must enter a whole number.")
            else:
                print("[!] Error: You must enter a number (use dot).")
                      

while True:
    print()
    print("╔══════════════════════╗")
    print("║[1] Add exercise      ║")
    print("╠══════════════════════╣")
    print("║[2] Show workout      ║")
    print("╠══════════════════════╣")
    print("║[3] Delete workout    ║")
    print("╠══════════════════════╣")      
    print("║[4] Exit              ║")
    print("╚══════════════════════╝")
    print()
    print(" Choose: [1][2][3][4] ")
    print()
    user_choice = input(" Your choice: ")
  

    if user_choice == "1":
            while True:
                name = (input(" Exercise name: ").strip())
                if name: 
                    break

                print("[!] Exercise name cannot be empty.")

            sets = get_valid_number(" Number of sets: ", "Number of sets", num_type=int)
            reps = get_valid_number(" Number of reps: ", "Number of reps", num_type=int)
            weight = get_valid_number(" Kilograms: ", "Weight", num_type=float, allow_zero=True)

            workout_input = {
                "name" : name,
                "sets" : sets,
                "reps" : reps,
                "weight" : weight,
            }

            user_workouts.append(workout_input)
            save_workouts(user_workouts)

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
                    print('"0" to cancel')
                    delete_choice = int(input(" Your choice: "))

                    if 1 <= delete_choice <= len(user_workouts):
                        deleted_exercise = user_workouts.pop(delete_choice - 1)
                        save_workouts(user_workouts)
                        
                        print(f"\n[-] {deleted_exercise['name']} has been deleted successfully!")
                        break
                    elif choice == 0:
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
