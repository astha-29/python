import logging

logging.basicConfig(filename=",ylog.log",level=logging.DEBUG)
try:
    f=open("myfile","w")
    a,b=[int(x)for x in input("enter two numbers").split()]
    logging.info("division in progress")
    c=a/b
    print(c)
    f.write("writing %d into file" %c)
    
except ZeroDivisionError:
    print("Division by zero is not allowed")
    print("please enter a non zero number")
    logging.error("division by zero")
else:
    print("you have entered a non zero number")   
finally:
    f.close()
    print("file closed")
print("code after the exception")