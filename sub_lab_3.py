# 🔹 Sub-Lab 3: Modular Function Design
# · Focus: Break the logic into reusable functions
# · Tasks:
# o get_attendee_info()
# o assign_zone(age, ticket_type)
# o store_attendee(data)
# o print_summary()
# · Expected Outcome: Organized, reusable codebase
# · Test Case: Calling get_attendee_info() returns a dictionary: {'name': 'Alice', 'age': 22, 'ticket': 'VIP'}

attendees = []

def get_attendee_info():
    print("########################################")
    print("Attendee # ")

    person = {
        "name": input("Enter name: "),
        "age": int(input("Enter age: ")),
        "ticket_type": str(input("Enter ticket type: ")),
    }

    try:
        if str.upper(str(person["ticket_type"])) not in ["REGULAR", "VIP"]:
            raise ValueError("Invalid ticket type: Ticket type must be Regular or VIP")
    except ValueError as e:
        print(e)

    return person


def assign_zone(age, ticket_type):
    if age < 18 and ticket_type != "VIP":
        return "Youth Zone"
    elif age >= 18 and ticket_type == "REGULAR":
        return "Standard Zone"
    elif ticket_type == "VIP":
        return "VIP Zone"
    return None


def store_attendee(data):
    attendees.append(data)


def print_summary():
    print({'name': attendee['name'], 'age': attendee['age'], 'ticket': attendee['ticket_type']})


attendee = get_attendee_info()
attendee["ticket_type"] = assign_zone(attendee["age"], attendee["ticket_type"])

store_attendee(attendee)

print_summary()
