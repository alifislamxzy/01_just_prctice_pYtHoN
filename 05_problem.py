p1 = "Make a lot of money" 
p2 = "buy now" 
p3 = "subscribe this" 
p4 = "click this"

message = input("Give me a comment: ")

if( (p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("Your comment is spam!!")
else:
    print("Your comment is not spam!!")

