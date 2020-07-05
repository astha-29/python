def display(name):
    def message():
        return "HELLO" 
    result = message()+name
    return result
print(display("bharat"))