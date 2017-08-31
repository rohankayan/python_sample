# question2.py
#
# A program to convert miles per gallon to liter per 100 km 
# Date: 08/28/2017
# Author: Rohan Kayan



def fuelEff():
    print("This program converts milage to liters per 100 km.")
    # user input in mpg
    mpg = eval( input("Please enter mileage (miles per gallon): " ))
    #mpg to kmpl conversion
    kmpl = mpg*1.6/3.785
    #kmpl to liter per 100 km conversion 
    lper100km = 100/(kmpl)
    print("Vehicle consumption is "+str(mpg)+" miles per gallon.")
    print("Vehicle economy is "+str(lper100km)+" liters per 100 km.")
    
def main():    
    fuelEff()
main()



