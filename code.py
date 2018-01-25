from time import sleep
while True:

    print("try guess this persons age bet you wont get it")
    sleep(2)
    choice=input("Guess his age!")
    if choice=="15":
        sleep(1)
        print("you are correct welldone")
        break
    else:
        sleep(1)
        print("your wrong m8")
        
