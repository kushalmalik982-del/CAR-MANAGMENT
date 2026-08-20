USER_FILE = "users.txt"
CAR_FILE = "cars.txt"
SOLD_FILE = "sold.txt"
for file in [USER_FILE, CAR_FILE, SOLD_FILE]:
    open(file, "a").close()
def register():
    print("\n--- Register ---")
    username = input("Create a username: ")
    password = input("Create a password: ")
    with open(USER_FILE, "a") as f:
        f.write(f"{username},{password}\n")
    print("Registered successfully!")

def login():
    print("\n--- Login ---")
    username = input("Username: ")
    password = input("Password: ")
    with open(USER_FILE, "r") as f:
        for line in f:
            u, p = line.strip().split(",")
            if u == username and p == password:
                print(f"Welcome {username}!")
                return username
    print(" Login failed.")
    return None

def add_car(username):
    print("\n--- Add Car ---")
    make = input("Car Name: ")
    model = input("Model: ")
    year = input("Year: ")
    price = input("Price: ")
    with open(CAR_FILE, "a") as f:
        f.write(f"{username},{make},{model},{year},{price}\n")
    print(" Car added.")


def view_cars():
    print("\n--- Available Cars ---")
    with open(CAR_FILE, "r") as f:
        cars = [line.strip() for line in f if line.strip()]
    if not cars:
        print(" No cars available.")
        return
    for i, line in enumerate(cars, 1):
        parts = line.strip().split(",")
        if len(parts) == 5:
            u, make, model, year, price = parts
            print(f"{i}. {make} {model} | Year: {year} | ₹{price} | Seller: {u}")




def sell_car(username):
    print("\n--- Sell a Car ---")
    with open(CAR_FILE, "r") as f:
        cars = [line for line in f if line.strip()]
    own_cars = [car for car in cars if car.startswith(username + ",")]
    if not own_cars:
        print(" You have no cars to sell.")
        return

    for i, car in enumerate(own_cars, 1):
        _, make, model, year, price = car.strip().split(",")
        print(f"{i}. {make} {model} | Year: {year} | ₹{price}")
    try:
        ch = int(input("Choose car number to sell: ")) - 1
        if ch < 0 or ch >= len(own_cars):
            print("Invalid choice.")
            return
    except ValueError:
        print("Invalid input.")
        return
    car_to_sell = own_cars[ch]
    cars.remove(car_to_sell)
    with open(CAR_FILE, "w") as f:
        f.writelines(cars)
    with open(SOLD_FILE, "a") as f:
        f.write(car_to_sell)

    print(" Car sold.")


def buy_car(username):
    print("\n--- Buy a Car ---")
    with open(CAR_FILE, "r") as f:
        cars = [line.strip() for line in f if line.strip()]
        valid_cars = [c for c in cars if len(c.split(",")) == 5]
    if not valid_cars:
        print(" No valid cars available.")
        return
    for i, car in enumerate(valid_cars, 1):
        u, make, model, year, price = car.split(",")
        print(f"{i}. {make} {model} | Year: {year} | ₹{price} | Seller: {u}")
    try:
        ch = int(input("Choose car number to buy: ")) - 1
        if ch < 0 or ch >= len(valid_cars):
            print(" Invalid choice.")
            return
    except ValueError:
        print(" Invalid input.")
        return
    selected = valid_cars[ch] + "\n"
    with open(CAR_FILE, "w") as f:
        for car in cars:
           if car.strip() != selected.strip():
                f.write(car + "\n")
    with open(SOLD_FILE, "a") as f:
         f.write(selected)
         print(" Car bought successfully.") 
def car_menu(username):
    while True:
        print(f"\n--- Welcome {username} ---")
        print("1. Add Car")
        print("2. View Cars")
        print("3. Sell My Car")
        print("4. Buy a Car")
        print("5. Logout")
        ch = input("Choose option: ")
        if ch == "1":
            add_car(username)
        elif ch == "2":
            view_cars()
        elif ch == "3":
            sell_car(username)
        elif ch == "4":
            buy_car(username)
        elif ch == "5":
            print(" Logged out.")
            break
        else:
            print(" Invalid option.")

def main():
    while True:
        print("\n===== Car Dealership Management =====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        ch = input("Choose option: ")

        if ch == "1":
            register()
        elif ch == "2":
            user = login()
            if user:
                car_menu(user)
        elif ch == "3":
            print(" Exiting program.")
            break
        else:
            print(" Invalid choice.")


if __name__ == "__main__":
    main()

