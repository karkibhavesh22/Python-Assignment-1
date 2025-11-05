def show_menu():
    print(" Calorie Tracking App ")
    print("1. Add Food Item")
    print("2. View Daily Log")
    print("3. Set Daily Calorie Goal")
    print("4. Check Progress")
    print("5. Exit")
    
def add_food(food_log):
    food_name = input("Enter food name: ")
    calories = int(input("Enter calories: "))
    food_log.append((food_name, calories))
    print(f"{food_name} ({calories} cal) added successfully!")
    
def view_log(food_log):
    if not food_log:
        print("No food items logged yet.")
        return
    print("\n--- Today's Food Log ---")
    total = 0
    for food, cal in food_log:
        print(f"{food}: {cal} cal")
        total += cal
    print(f"Total: {total} cal")
    
def set_goal():
    goal = int(input("Enter your daily calorie goal: "))
    print(f"Calorie goal set to {goal} cal.")
    return goal

def check_progress(food_log, goal):
    total = sum(cal for _, cal in food_log)
    print(f"\nDaily Goal: {goal} cal")
    print(f"Calories Consumed: {total} cal")
    if total < goal:
        print(f"You are {goal - total} cal below your goal. Keep going!")
    elif total == goal:
        print("Perfect! You've hit your goal.")
    else:
        print(f"You are {total - goal} cal above your goal. Try to adjust tomorrow!")
        
def main():
    food_log = []
    calorie_goal = 2000  # Default goal

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_food(food_log)
        elif choice == "2":
            view_log(food_log)
        elif choice == "3":
            calorie_goal = set_goal()
        elif choice == "4":
            check_progress(food_log, calorie_goal)
        elif choice == "5":
            print("Exiting... Stay healthy!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
    