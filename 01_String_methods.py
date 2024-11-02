# This is usefull 7 methods in python for i am usinge
# String in python
name = "md alif islam"

method1 = len(name) # Output is : 13
method2 = name.endswith("if") # Output is : False
method3 = name.count("i") # Output is : 2
method4 = name.capitalize() # Output is : Md alif islam
method5 = name.title() # Output is : Md Alif Islam
method6 = name.find("is") # Output is : 8
method7 = name.replace("f", "m")
print(method7)

text = "This is an example text with a  double space."
# This will print True if double spaces are found, otherwise False
rep = text.replace("  ", "   ")
print("   " in rep)

