m=int(input("enter the marks for subject maths"))

p=int(input("enter the marks for subject physics"))

c=int(input("enter the marks for subject chemistry"))

if ((m + p + c) >= 35):
    print("pass")

    if (35<= (m+p+c) <= 59):

        print("your grade is C")

    elif (59< (m+p+c) <= 69):

        print("your grade is B")

    elif (69 < (m+p+c) <= 79):

        print("your grade is A")

else:print("failed")