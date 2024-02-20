import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 
userimage=0
computerimage=0
userimagename=""
comimagename=""
user=int(input("please give a number. 0 1 2 "))
random_number_computer=random.randint(0,2)
if user==0:
    userimage=rock
    userimagename="rock"
elif user==1:
    userimage=scissors
    userimagename="scissors"
else:
    userimage=paper
    userimagename="paper"
if random_number_computer==0:
    computerimage=rock
    comimagename="rock"
elif random_number_computer==1:
    computerimage=scissors
    comimagename="scissors"
else:
    computerimage=paper
    comimagename="paper"
  

# condition for the game
# 0 for rock
# 1 for scissor
# 2 for paper
print(f"you choose {userimagename} {userimage}")

print(f"computer choose {comimagename} {computerimage}")
if user==0 and random_number_computer==1:
    print("you won")
elif user==0 and random_number_computer==2:
    print("computer won")
elif user==1 and random_number_computer==0:
    print("computer won")
    
elif user==1 and random_number_computer==2:
     print("you won")
elif user==2 and random_number_computer==0:
    print("you won")
elif user==2 and random_number_computer==1:
     print("computer won")
     
else :
    print("draw")