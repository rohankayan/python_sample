# question3.py
#
# A program to convert Celcius to Fahrenheit in loop  
# Date: 08/28/2017
# Author: Rohan Kayan

def celciusToFahrenheit(celcius):
    #Celcius to Fahrenheit conversion
    return celcius * 1.8 + 32

def main():
    print ("Celsius"+"  "+"Fahrenheit")
    print ("-------------------")
    print (" "+str(0)+"\t    "+str(celciusToFahrenheit(0)))
    for i in range(10,110,10):
        print (str(i)+"\t    "+str(celciusToFahrenheit(i)))

main()