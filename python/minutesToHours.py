def mToH(): #minutes to hours
    minutes = input("Minutes: ")
    hours = minutes / 60
    print(f"Hours: {hours:.0f}")

def hToM(): #hours to minutes
    hours = int(input("Hours: "))
    minutes = hours * 60
    print(f"Minutes: {minutes:.0f}")

def mToD(): #minutes to days
    minutes = int(input("Minutes: "))
    days = (minutes / 60) / 24
    print(f"Days: {days:.2f}")

def hToD(): #hours to days
    hours = int(input("Hours: "))
    days = hours / 24
    print(f"Days: {days:.2f}")

invalid = "Invalid input, please try again: "
ignore = False

while(True):
    opt = input("Minutes to hours or hours to minutes: ")

    while(opt != "Hours" and opt != "Minutes" and opt != "" and opt != "end"):
        opt = input(invalid)

    if(opt == "end"): break

    if(opt == ""):
        ignore = True
        opt = input("Minutes to days or hours to days: ")

        while(opt != "Hours" and opt != "Minutes" and opt != "end"):
            opt = input(invalid)

        if(opt == "end"): break
    
        if(opt == "Hours"): hToD()
        else: mToD()

    if(opt == "Hours" and ignore == False): hToM()
    elif(opt == "Minutes" and ignore == False): mToH()
    ignore = False
