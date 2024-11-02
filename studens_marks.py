score = int(input("What's your Score? "))

if score>= 90 and score<100: 
    print("Your Gread is: A")
elif score>=80 and score<90:
    print("Your Gread is: B")
elif score>=70 and score<80:
    print("Your Gread is: C")
elif score>=60 and score<70:
    print("Your Gread is: D")
elif score>=33 and score<60:
    print("Your Gread is: Pass")
elif score>100:
    print("You are wrong")
else:
    print("Your Gread is failed")
    print("Try next year!")