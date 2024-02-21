from CaffeFunctions import *
from datetime import timedelta, datetime
import emoji
from time import sleep
from database import database

# variable instance
db = database()


######################################
### MAIN FUNCTION
######################################

def customer_details(db:list,
                     mode:str="customer") -> print():

    """
    this is the function to handle the store
    ---------------
    - ARGS:
        - db:list --> list of dictionries containing the database
        - mode:str --> enter in customer or employee mode, options(customer/employee)
    --------------
    - RETURN:
        - Print() statement 
    """
    response = "" #ESTA VARIABLE SE ACTUALIZARÁ CON LA RESPUEST ADECUADA

    #Checks if all the required packages for the software are installed if not
    #it install them
    requirementsMessage = """
    I'm checking if all the packages needed for running
    the software are already installed. This can take a
    little moment, but it won't be long,
    Thank you for your patience. Working..."""

    response = chatMessage(requirementsMessage)
    # pause the code execution for 5 seconds
    sleep(5)
    # install the needed requirements
    autoPackagesInstaller()

    #Checks the mode of the sofware
    if mode == "customer":
        # this part contains the frontdesk funtionality
        # Welcomes the user
        first_name = "Fer"
        #first_name = input(chatMessage("Welcome to BOOK CAFE!,What's your first name?: "))
        first_response = f"Welcome!,{first_name} We offer drinks & a selection of food in our Cafe."
        response = chatMessage(first_response)
        sleep(5)
        second_response = "We also sell books and can deliver them to your home." 
        response = chatMessage(second_response)
        sleep(5)
        # The software enters where the business logic for purchasing resides
        business_logic(db)
        # We set up a variable for checking if the customer wants to keep buying
        keepBuying = "Would you like to order anything else? (yes/no): "
        more = input(chatMessage(keepBuying))
        # We delete the trailing or leading spaces and lower case the input
        more = more.lower().strip()
        # the program enter a while loop so as long as more is true, the customer
        # wants to keep buying, the program is going to continue executing business_logic()
        while more == "yes":
            # we call business logic function
            business_logic(db)
            # the variable more is updated depending on the customer response
            more = input(chatMessage(keepBuying)).lower().strip()
        # When the while loop exists we save the purchase in a variable to make the bill
        ticket = [foods_bill,drinks_bill,books_bill]
        # We ask users if they want the order to be delivered to home
        buyHome = "Would you like your purchase to be delivered?(yes/no): "
        delivery = input(chatMessage(buyHome))
        
        # If they answer yes
        if delivery == "yes":
            # Asks for the address
            askAddress = "Please provide us with your address: "
            address = input(chatMessage(askAddress))
            # Define the arrival day
            arrival = (datetime.now() + timedelta(days=2)).strftime("%d-%m-%Y")
            # Generates the bill
            bill(ticket)
            print("\n")
            infoDelivery = f"Your order will be delivered to: {address}" 
            print(chatMessage(infoDelivery))
            print(f"{emoji.emojize(":delivery_truck:")}...<-- will arrive by {arrival}")
            print("\n")
        else:
            # if they do not want home delivery we create the bill
            bill(ticket)
            print("\n")

    # Here we manage the backend of the store        
    elif mode == "employee":
        # we call the function that handles the employee's functions
        employee_details(db)
    # if a wrong parameter is inputed the person is warned
    else:
        print(" "*22+ emoji.emojize(":no_entry:"))
        print("-"*48)
        print("|The only valid values are customer or employee|")
        print("-"*48)
        
    return response

customer_details(db,mode="customer")