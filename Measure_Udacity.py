def measure_udacity(name):
    count = 0
    for a in name:
        if a[0] == "U":
            count+=1
    return count
print measure_udacity(["Andy","Uas","Bibi"])
print measure_udacity(['Umika','Umberto',"Uaaa"])



def measure_udacity(list):
    count = 0
    for name in list:
        if name[0] == 'U':
            count+=1
    return count
print measure_udacity(['Umika'])



def calandar(day):
    count = 0
    for holidays in day:
        if holidays[0] == "S" or holidays[0] == "s":
            count += 1
    return count
print calandar(["Sunday"])
print calandar(["monday"])
print calandar(["Saturday","Sunday"])
print calandar(["Saturday"])



# My testing
# But i want to get:
# print calandar(["monday","sunday"])
# answer is Weekday .. Weekend
# How can i get?....I don't know.. :(
def calandar(day):
    count = 0
    for holidays in day:
        if holidays == "sunday" or holidays == "Saturday":
            return "Weekend"
        else:
            return "Weekday"
            count += 1
    return count
print calandar(["monday"])
print calandar(["sunday"])
print calandar(["Saturday"])
