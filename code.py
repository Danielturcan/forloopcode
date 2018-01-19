from time import sleep
while True:

    print("try guess my age")
    sleep(2)
    choice=input("Guess my age!")
    if choice=="15":
        sleep(1)
        print("you are correct")
        break
    else:
        sleep(1)
        print("your wrong")
