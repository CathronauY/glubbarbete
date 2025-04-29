def minutesToHours(): #minutes to hours
    minutes = input("Minutes: ")
    hours = minutes / 60
    return hours

def hoursToMinutes(): #hours to minutes
    hours = int(input("Hours: "))
    minutes = hours * 60
    return minutes

def minutesToDay(): #minutes to days
    minutes = int(input("Minutes: "))
    days = (minutes / 60) / 24
    return days

def hoursToDay(): #hours to days
    hours = int(input("Hours: "))
    days = hours / 24
    return days

invalid = "Invalid input, please try again: "
ignore = False

while(True):
    opt = input("Minutes to hours or hours to minutes: ")

    while(opt != "Hours" and opt != "Minutes" and opt != "" and opt != "end"):
        opt = input(invalid)

    if(opt == "end"):
        break

    if(opt == ""):
        ignore = True
        opt = input("Minutes to days or hours to days: ")

        while(opt != "Hours" and opt != "Minutes" and opt != "end"):
            opt = input(invalid)

        if(opt == "end"):
            break
    
        if(opt == "Hours"): hoursToDay()
        else: minutesToDday()

    if(opt == "Hours" and ignore == False): hToM()
    elif(opt == "Minutes" and ignore == False): mToH()
    ignore = False
