import random
numbers=list(range(1,101))
guess=True
while guess!='yes':
    random.shuffle(numbers)
    yournum=numbers[-1] 
    numbers.sort()
    index=numbers.index(yournum)
    guess=input("is your num "+str(yournum)+"? Is it bigger or lower?")
    if guess=='yes':
        print("bravo! your num is "+str(yournum)+"!")
        break
    elif guess=='bigger':
        del numbers[:index+1]
    elif guess=='lower':
        del numbers[index:]
    else:
        print("Invalid input!")
        continue
