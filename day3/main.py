# number=int(input("please type the number"))
# reminder=number%2
# if reminder==0:
#     print("the number is even")
# else:
#     print("the number is odd")

# height=int(input("please give us your height"))
# if height>=120:
#     age=int(input("please give us your age"))
#     if age<=18:
#         print("your fee is $7")
#     else:
#         print("your fee is $12")
# else:
#     print("sorry, cant ride until your heigth is 120cm")

# Bmi calculator
# height=float(input("please give us your height"))
# weight=int(input("please give us your weight"))

# bmi=weight/(height*height)
# if bmi <= 18.286:
#     print(f"your bmi is {bmi}, you are underweight")
# elif bmi<=22:
#     print(f"your bmi is {bmi}, you have a normal bmi")
# elif bmi<=28.5:
#     print(f"your bmi is {bmi}, you are slightly overweight")
# elif bmi<=32.5:
#     print(f"your bmi is {bmi}, you are obese")
# else:
#     print(f"your bmi is {bmi}, you are clinically obese")

# calculating if it is leap year or not
# year=int(input("please provide a year"))
# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             print("leap year")
#         else:
#             print("not a leap year")
#     else:
#         print("leap year")
# else:
#     print("not a leap year")

#simple resturant manangement
print("welcome to python pizza")
price=0
size=input("what size would you like? S, M, L ")
add_pepperoni=input("would you like to add peperoni? Y , N ")
extra_cheese=input("would you like to add extra cheese? Y , N ")

if size=="l":
    price=25
    if add_pepperoni=="y":
        price+=3
    if extra_cheese=="y":
        price+=1
    print(f"your total bill is ${price}.")
elif size=="m":
    price=20
    if add_pepperoni=="y":
        price+=3
    if extra_cheese=="y":
        price+=1
    print(f"your total bill is ${price}.")
elif size=="s":
    price=15
    if add_pepperoni=="y":
        price+=2
    if extra_cheese=="y":
        price+=1
    print(f"your total bill is ${price}.")