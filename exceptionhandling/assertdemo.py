try:

    num=int(input("enter a even number"))
    assert num%2==0,"you have entered an invalid input"

except AssertionError as obj:
    print(obj)

print("after the assertion")
