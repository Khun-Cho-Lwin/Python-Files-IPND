def weekend(day):
    if day == "Saturday" or day == "Sunday":
        return True
    else:
        return False
print weekend("monday")
print weekend("Sunday")
print weekend("Saturday")
print weekend("tueday")
