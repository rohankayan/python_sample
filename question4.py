# question4.py
#
# Interactive Python Calculator  
# Date: 08/28/2017
# Author: Rohan Kayan

def main():
    print("Welcome to the Interactive Python Calculator")
    #for loop for 100 iteration max 
    for i in range(100):
        #user input for expression 
        x = eval(input ("Enter new expression here: "))
        print (x)
main()