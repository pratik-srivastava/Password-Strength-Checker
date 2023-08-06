import re
def my_func():
    val=0
    p=input("Please Enter a password.....\n")
    if re.search('[a-z]',p):
        val=val+1
    if re.search('[A-Z]',p):
        val=val+1
    if re.search('[0-9]',p):
        val=val+1
    if re.search('[!@#$%^&*()-_":?<>.,;=~]',p):
        val=val+1
    if len(p)<8:
        print("The password should have atleast 8 characters")
    if val==4:
        print("!Very Strong Password!")
    if val==3:
        print("!Strong Password!")
    if val==2:
        print("!Medium Password!")
    if val==1:
        print("!Weak Password!")
    return 0
my_func()
