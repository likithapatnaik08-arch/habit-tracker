import json
from datetime import datetime

FILE_NAME = "habits.json"


def load_habits():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []


def save_habits(habits):
    with open(FILE_NAME, "w") as file:
        json.dump(habits, file, indent=4)


def add_habit(habits):
    name = input("Enter habit name: ").strip()

    if name == "":
        print("Habit name cannot be empty.")
        return

    category = input("Enter category (Study/Fitness/etc): ").strip()

    habit = {
        "name": name,
        "category": category,
        "done": False,
        "streak": 0,
        "created_date": str(datetime.now().date()),
        "last_completed": "",
        "completed_count": 0
    }

    habits.append(habit)
    save_habits(habits)

    print("✅ Habit added successfully!")


def view_habits(habits):

    if len(habits) == 0:
        print("\nNo habits found.")
        return

    print("\n========== YOUR HABITS ==========\n")

    for i, habit in enumerate(habits, start=1):

        status = "✅" if habit["done"] else "❌"

        print(f"{i}. {status} {habit['name']}")

        print(f"   Category : {habit['category']}")
        print(f"   Streak   : {habit['streak']} 🔥")
        print(f"   Created  : {habit['created_date']}")
        print(f"   Completed: {habit['completed_count']} times")

        if habit["last_completed"] == "":
            print("   Last Done: Never")
        else:
            print(f"   Last Done: {habit['last_completed']}")

        print("-" * 35)


def mark_done(habits):

    if len(habits) == 0:
        print("No habits available.")
        return

    view_habits(habits)

    try:
        num = int(input("\nEnter habit number: "))

        if num < 1 or num > len(habits):
            print("Invalid habit number.")
            return

        habit = habits[num - 1]

        today = str(datetime.now().date())

        if habit["last_completed"] == today:
            print("Already completed today.")
            return

        if habit["last_completed"] != "":
            last = datetime.strptime(
                habit["last_completed"],
                "%Y-%m-%d"
            ).date()

            difference = (datetime.now().date() - last).days

            if difference == 1:
                habit["streak"] += 1
            else:
                habit["streak"] = 1
        habit["done"] = True
        habit["last_completed"] = today
        habit["completed_count"] += 1

        save_habits(habits)

        print("🎉 Habit completed!")

    except:
        print("Please enter a valid number.")


def delete_habit(habits):

    if len(habits) == 0:
        print("No habits to delete.")
        return

    view_habits(habits)

    try:
        num = int(input("Enter habit number to delete: "))

        if 1 <= num <= len(habits):

            deleted = habits.pop(num - 1)

            save_habits(habits)

            print(f"🗑️ {deleted['name']} deleted successfully!")

        else:
            print("Invalid habit number.")

    except:
        print("Please enter a valid number.")


def edit_habit(habits):

    if len(habits) == 0:
        print("No habits found.")
        return

    view_habits(habits)

    try:

        num = int(input("Enter habit number to edit: "))

        if 1 <= num <= len(habits):

            new_name = input("Enter new habit name: ")

            new_category = input("Enter new category: ")

            habits[num - 1]["name"] = new_name
            habits[num - 1]["category"] = new_category

            save_habits(habits)

            print("✅ Habit updated!")

        else:
            print("Invalid habit number.")

    except:
        print("Please enter a valid number.")


def search_habit(habits):

    keyword = input("Search: ").lower()

    found = False

    for habit in habits:

        if keyword in habit["name"].lower():

            print()

            print("Found Habit")

            print("--------------------")

            print("Name :", habit["name"])

            print("Category :", habit["category"])

            print("Streak :", habit["streak"])

            print("Completed :", habit["completed_count"])

            found = True

    if not found:
        print("No matching habit found.")
def show_statistics(habits):

    total = len(habits)

    if total == 0:
        print("\nNo habits available.")
        return

    completed = 0

    for habit in habits:
        if habit["done"]:
            completed += 1

    pending = total - completed

    percentage = (completed / total) * 100

    print("\n========== STATISTICS ==========")
    print("Total Habits      :", total)
    print("Completed Habits :", completed)
    print("Pending Habits   :", pending)
    print(f"Completion       : {percentage:.2f}%")
    print("================================")


def reset_daily_status(habits):

    today = str(datetime.now().date())

    changed = False

    for habit in habits:
        if habit["done"]:
            if habit.get("last_completed") != today:
                habit["done"] = False
                changed = True

    if changed:
        save_habits(habits)


habits = load_habits()
reset_daily_status(habits)

while True:

    print("\n========== HABIT TRACKER ==========")

    print("1. Add Habit")
    print("2. View Habits")
    print("3. Mark Habit as Done")
    print("4. Delete Habit")
    print("5. Edit Habit")
    print("6. Search Habit")
    print("7. View Statistics")
    print("8. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        add_habit(habits)

    elif choice == "2":

        view_habits(habits)

    elif choice == "3":

        mark_done(habits)

    elif choice == "4":

        delete_habit(habits)

    elif choice == "5":

        edit_habit(habits)

    elif choice == "6":

        search_habit(habits)

    elif choice == "7":

        show_statistics(habits)

    elif choice == "8":

        print("\nThank you for using Habit Tracker ❤️")
        break

    else:

        print("Invalid choice. Please try again.")
