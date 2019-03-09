
import time 
def main() : 
  
    moreitem=True
    total = 0
    while(moreitem):
        time.sleep(3)
        print ('Welcome to the StemBrain')
        print ("Please enter y for yes amd n for no ")
        response = input()
        if response == 'y' or response =='Y': 
           print("please enter for item name") 
        else:
            print("Goodbye,Thank you for shopping with us")
            break 
        total += get_item_price(get_item_name())
        print ('Total Sum = ',total)
        print("")
    
def  get_item_name():
         name = input()
         return name
def  get_item_price(value):
     #price = 0 
     price =int( input("Please enter the price of your item"+ value))
     quantity = get_item_quantity()
     return price * quantity 
def  get_item_quantity():
     quantity =int( input("please enter your itwm quantity"))
     return quantity

main()
