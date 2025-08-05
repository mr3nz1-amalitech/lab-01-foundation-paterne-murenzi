# Focus: Collect attendee details
#
# · Task: Prompt the user to input name, age, and ticket type (VIP or Regular)
#
# · Expected Outcome: Data correctly stored with proper types
#
# · Test Case: Input: John, 28, VIP → Output: Attendee Registered

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
