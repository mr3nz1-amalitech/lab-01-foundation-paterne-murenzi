# 🔹 Sub-Lab 4: Using Data Structures
# · Focus: Store and manage multiple attendee records
# · Task: Use a list of dictionaries to store data
# · Bonus: Generate summaries such as:
# o Number of attendees per zone
# o Average age of attendees
# · Expected Outcome: Able to iterate over and summarize stored records
# · Test Case: Output: Total VIP attendees: 5, Youth: 2, Average age: 26.4


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
    summary = {"average_vip_attendees": 0, "total_youth_attendees": 0, "average_age": 0}
    total_age = 0

    for attendee in attendees:
        if attendee["ticket_type"] == "VIP":
            summary["average_vip_attendees"] += 1

        if attendee["age"] <= 18:
            summary["total_youth_attendees"] += 1

        total_age += attendee["age"]
        summary["average_age"] = total_age / len(attendees)

    print(
        f"Total VIP attendees: {summary['average_vip_attendees']}, Youth: {summary['total_youth_attendees']}, Average age: {summary['average_age']}")


attendee_total = input("Enter total attendees: ")

for i in range(0, int(attendee_total)):
    store_attendee(get_attendee_info())

print_summary()
