attendees = []

print("Enter attendee size:")
number_of_attendees = int(input())

for i in range(number_of_attendees):
    print("########################################")
    print("Attendee # " + str(i + 1))

    attendee = {
        "name": input("Enter name: "),
        "age": int(input("Enter age: ")),
        "ticket_type": str(input("Enter ticket type: ")),
    }

    try:
        if str.upper(str(attendee["ticket_type"])) not in ["REGULAR", "VIP"]:
            raise ValueError("Invalid ticket type: Ticket type must be Regular or VIP")
    except ValueError as e:
        print(e)

    attendees.append(attendee)

    print("Attendee registered")

    if attendee["age"] < 18 and attendee["ticket_type"] != "VIP":
        print("Youth Zone")
    elif attendee["age"] >= 18 and attendee["ticket_type"] == "REGULAR":
        print("Standard Zone")
    elif attendee["ticket_type"] == "VIP":
        print("VIP Zone")