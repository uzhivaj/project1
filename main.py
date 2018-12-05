# we're going to start with the basics
# lets go

# introduction

print("hello friend!")
print("let's do some math today!")
print("..")
print("but only easy stuff please, I'm still learning.")

# main code

condition = 1

while condition < 4:

    a = input("Enter a number: ")
    b = input("add[+], subtract[-], multiply[*] or divide[/]? :")
    c = input("And another..: ")

    if b == "+":
        print(float(a) + float(c))
    elif b == "-":
        print(float(a) - float(c))
    elif b == "*":
        print(float(a) * float(c))
    elif b == "/":
        print(float(a) / float(c))
    else:
        condition += 1
        print("ERROR...restarting..")

print("***********************")
print("***********************")
print("I don't think you really get this whole math-thing.")
print("I'm going to sleep for a while")
print("Goodnight <3")

exit()


