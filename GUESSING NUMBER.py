from random import randint

number=randint(1,100)
chances=int(input("ENTER NUMBER OF CHANCES: "))
while chances>0:
    userinput=int(input("GUESS A NUMBER: "))
    if userinput==number:
        print("YOU WON!!!")
        break
    elif userinput>number:
        print("The userinput is greater than the number")
        chances-=1
    else:
        print("The userinput is less than the number")
        chances-=1
else:
    print(number)
    print("YOU LOST!!!!!")
