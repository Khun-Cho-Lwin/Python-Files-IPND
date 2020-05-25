def how_many_days(month_number):
    days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    return days_in_month[month_number-1]
print how_many_days(12)

def dice_surface(color):
    number_name = [1,2,3,4,5,6]
    color_name = ["blue","white","red","pink","black","green"]
    number_name == color_name
    return color_name[color-1]
print dice_surface(2)
print dice_surface(5)
print dice_surface("blue")
