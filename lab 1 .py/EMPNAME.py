EMPNAME = []

def add_employee(name):
    EMPNAME.append(name)
    print(f"Added {name} to EMPNAME")

def remove_employee(name):
    if name in EMPNAME:
        EMPNAME.remove(name)
        print(f"Removed {name} from EMPNAME")
    else:
        print(f"{name} not found in EMPNAME")

def add_multiple_employees(names):
    EMPNAME.extend(names)
    print(f"Added {', '.join(names)} to EMPNAME")

initial_names = ["Alice", "Bob", "Charlie"]

EMPNAME.extend(initial_names)

print("Initial EMPNAME:", EMPNAME)

add_employee("David")


remove_employee("Bob")

additional_names = ["Emily", "Frank"]
add_multiple_employees(additional_names)

print("Final EMPNAME:", EMPNAME)