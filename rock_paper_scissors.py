import random

count=0
moves=int(input("enter the number of moves you want: "))
points=0
ties=0

while (count<moves):
    choice=input("enter your choice: ")
    choice=choice.lower()
    choices=["rock", "paper","scissors"]
    random.shuffle(choices)
    rand_str=random.randint(0,len(choices)-1)
    computer_choice=choices[rand_str]
    
    print("you entered: ", choice)
    print("The computer thought: ", computer_choice)

    if(choice=="rock"):
        if(computer_choice=="rock"):
            print("it was a tie.")
            ties+=1
        elif(computer_choice=="paper"):
            print("sorry to say, but you lost, sad.")
        elif(computer_choice=="scissors"):
            print("wohoo!!, congrats you won it!!")
            points+=1

    elif(choice=="paper"):
        if(computer_choice=="rock"):
            print("wohoo!!, congrats you won it!!")
            points+=1
        elif(computer_choice=="paper"):
            print("it was a tie.")
            ties+=1
        elif(computer_choice=="scissors"):
            print("sorry to say, but you lost, sad.")

    elif(choice=="scissors"):
        if(computer_choice=="rock"):
            print("sorry to say, but you lost, sad.")
        elif(computer_choice=="paper"):
            print("wohoo!!, congrats you won it!!")
            points+=1
        elif(computer_choice=="scissors"):
            print("it was a tie.")
            ties+=1

    else:
        print("please enter a proper value you 'not_a_goodreader!!'")
        ties+=1
        
    count+=1
    print()

if(points<(moves-points)-ties):
    print("The computer won with: ", (moves-points)-ties, " points.")
elif(points>(moves-points)-ties):
    print("You won with: ", points, " points.")
else:
    print("it was tie in points between you and the computer.")
