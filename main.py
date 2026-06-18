from api_client import fetch_users
from file_utils import load_json_from_file, save_json_to_file
from user_search import filter_users

DATA_FILE = "internship-20/users.json"


def display_user(user):
    company_name = user.get("company", {}).get("name", "N/A")
    city = user.get("address", {}).get("city", "N/A")
    print(f"Name: {user.get('name', 'N/A')}")
    print(f"Email: {user.get('email', 'N/A')}")
    print(f"Phone: {user.get('phone', 'N/A')}")
    print(f"Company: {company_name}")
    print(f"City: {city}")
    print("-" * 40)


def display_users(users):
    if not users:
        print("No users to display.")
        return
    for user in users:
        display_user(user)


def show_menu():
    print("\n=== User Data Assignment ===")
    print("1. Fetch user data from API and save to file")
    print("2. Load user data from local JSON file")
    print("3. Search loaded users")
    print("4. Display all loaded users")
    print("5. Exit")


def prompt_search_field():
    print("Choose a search field:")
    print("  name")
    print("  city")
    print("  company")
    return input("Search field: ").strip().lower()


def main():
    users = []
    print("This program fetches user data from jsonplaceholder.typicode.com and saves it locally.")

    while True:
        show_menu()
        choice = input("Enter option number: ").strip()

        if choice == "1":
            try:
                users = fetch_users()
                save_json_to_file(users, DATA_FILE)
                print(f"Fetched {len(users)} users and saved data to {DATA_FILE}.")
            except Exception as exc:
                print(f"Error: {exc}")

        elif choice == "2":
            try:
                users = load_json_from_file(DATA_FILE)
                print(f"Loaded {len(users)} users from {DATA_FILE}.")
            except Exception as exc:
                print(f"Error: {exc}")

        elif choice == "3":
            if not users:
                print("No user data loaded. Choose option 1 or 2 first.")
                continue
            field = prompt_search_field()
            if field not in ("name", "city", "company"):
                print("Invalid search field. Please choose name, city, or company.")
                continue
            query = input("Enter search query: ").strip()
            results = filter_users(users, query, field)
            print(f"Found {len(results)} matching users.")
            display_users(results)

        elif choice == "4":
            if not users:
                print("No user data loaded. Choose option 1 or 2 first.")
                continue
            display_users(users)

        elif choice == "5":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
