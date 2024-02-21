import emoji
import pandas as pd
import pkg_resources
import subprocess
import sys

# VARIABLES
foods_bill = {"product":[],"price":[],"quantity":[]}
drinks_bill = {"product":[],"price":[],"quantity":[]}
books_bill = {"product":[],"price":[],"quantity":[]}



#FUNCTIONS

###############################################
# AUXILIARY FUNCTION FOR PICKING INFO OF DICS #
###############################################

def price_picker(db,product,*args) -> int | float:
    """
    this is a function to troubleshoot a design issue with the database as we chose as keys numbers and the same key
    for the different products.
    --------------
    - ARGS:
        - db: (list) --> database, list of dictionaries
        - product: (str) --> the name of the product
        - *args (string) --> other information
    - RETURN:
        - int or float
    """
    mask = []
    index = []
    # we  select the dictionary where we want to look for:
    if product == "drinks":
        # we select the product we want to get info of and make a mask list of boolean values
        for i,val in db[2].items():
            # we save the the booleans in the list mask to make the mask list for the appropiate product given as args
            mask.append((val["name"] == args[0]) and (val["size"] == args[1]))
            # we save the position of each product in the dictionary so we can then associate the index with the boolean
            index.append(i)
        # we match each index with each True boolean data so we can pick the correct index
        product_index = [i for i, m in zip(index, mask) if m][0]
        # now that we now the index of the product we want we extract the price for it
        price = db[2][product_index]["price"]
    # the rest works the same, only is changed the dictionary depending on the section:    
    elif product == "food":
        for i,val in db[3].items():
            mask.append(val["name"] == args[0])
            index.append(i)
    
        product_index = [i for i, m in zip(index, mask) if m][0]
        price = db[3][product_index]["price"]
    elif product == "books":
        for i,val in db[4].items():
            mask.append(val["name"] == args[0])
            index.append(i)
    
        product_index = [i for i, m in zip(index, mask) if m][0]
        price = db[4][product_index]["price"]

    return price

#######################################
#           CHATTING MESSAGE          #
#######################################
def chatMessage(message:str="placeHolder",
                emo:str=":older_person:") -> print():
    """
    uses a message to show a character saying the message
    - ARGS:
        - message(str) --> the message you want to show
        - emo(str) --> the emoji you want to show
    - RETURN:
        print()
    """
    # We store the emoji to place it in the print
    person = emoji.emojize(emo)
    # print the message
    response = f"{person}= {message}"
    print("\n")
    return response

########################################
#               BILLING                #
########################################
def bill(total_bill:list) -> print():
    """
    Creates the bill for the customer
    ---------
    - ARGS:
        - total_bill(list) --> list of dictionries
    ---------
    - RETURN:
        - print()
    """
    # list of sections
    order = ["food","drinks","books"]
    # storage for the total bill of each section, matchs the above index
    to_pay = []
    # bill header
    print("\n" + "="*40)
    print(" "*10+"PYTHON RANGERS CAFE")
    print("="*40)
    # for this loop we get the section in the order list
    for i in range(len(order)):
        # print the section order in the bill
        print(order[i])
        # saves the dictionary to be used temporarily [dic1,dic2,dic3]
        dic = total_bill[i]
        # for the length of the dictionary key product
        for k in range(len(dic["product"])):
            # we print the name of the product and the quantity
            # be aware that here we are looping inside the key product of the dictionary dic
            # and we are using indices because what dic["product"] contains is a list,
            # so when we access the value of the before key (list) we use [k]
            print(f"\t- {dic["product"][k]}:{dic["quantity"][k]}")
        # gets the price from the dictionary    
        prices = total_bill[i]["price"]
        # gets the quantity of the dictionaries
        quantities = total_bill[i]["quantity"]
        # calculates the total amount of each section and then sums everything up
        money = sum([prices[i]*quantities[i]for i in range(len(prices))])
        # saves the data in a list
        to_pay.append(money)
        # prints the amount for the total bill
        print(f"\t\tTOTAL FOR {order[i]}:{round(money,2)} €")
    # bill foot
    print("-"*40)
    print(f"{' '*10} TOTAL COST {round(sum(to_pay),2)} €")
    print("="*40)
    print(" "*15 + "Thank you very much! "+ '\U0001F44B')

#####################################
#            MENU DISPLAY           #
#####################################

def menuRender(dic:dict,section:str="drinks") -> print():
    """
    This function renders the menu options
    ----------
    - ARGS:
        - dic (dict) --> dictionary containing the product info
    - RETURN:
        - Print()
    """
    
    # creates the menu for drinks
    if section == "drinks":
        #print headers
        print(chatMessage("Our Drink Menu Items are as below\n"))
        print("="*41)
        print("\tDRINK\t\tSIZE\tPRICE")
        print("="*41)
        # for each product in the dictionary prints the product in a new line
        for product in dic.values():
            print(f"|\t{product['name']}\t\t{product['size']}\t{product['price']}€\t|")
        print("="*41)          
        print("\n")
    # here we do the same but for foods, it has different fields so because of that is different
    elif section == "foods":
        # for aligning in the table products with different character lenghths 
        # we create a list where to store the lenght of every product name
        lenght_prods = []
        # we set the maximum length of characters  
        # we iterate the list of products and store their lengths
        for product in dic.values():
            numcharacters = len(product["name"])
            lenght_prods.append(numcharacters)  
        maxLength = max(lenght_prods)
        # stablish the headers
        print(chatMessage("Our Foods Menu Items are as below\n"))
        equalsAdding = (maxLength-min(lenght_prods))
        multiplyer = 38
        dashLine = "="*(multiplyer+ equalsAdding) 
        print(dashLine)
        print("\tFOOD\t\t\t\tPRICE")
        print(dashLine)

        for product in dic.values():
            # we check if the name lenght is less than the maximum, if so we add
            # spaces to the left to make the name the same length of the larger name
            # if no, we leave the name as it is
            name = product["name"].ljust(maxLength) if len(product["name"])<maxLength else product["name"]
            # we print the list
            print(f"|\t{name}\t\t{product['price']}€\t|")
        print(dashLine)
        print("\n")
    elif section == "books":
        # Different way of showing the book list:
        print(chatMessage(f"Check Our Great Library!!{emoji.emojize(":books:")}\n"))
        # we format the source dictionary to a best suited dictionary for dataframes
        newDicBooks = {"title":[],"author":[],"price":[],"amount":[]}
        # store the new and old keys and convert them to lists for iterate throw
        newKeys = list(newDicBooks.keys())
        oldKeys = list(dic[1].keys())
        # we access each key and value of the old dictionary and store
        # the correspondent values into their lists inside the new dictionary
        for i in range(len(oldKeys)):
            for oldDic in dic.values():
                newDicBooks[newKeys[i]].append(oldDic[oldKeys[i]])
        # Once well formated the dictionary we create a pandas dataframe and print it
        print(pd.DataFrame(newDicBooks))

    else:
        print("Sorry,we do not have this kind of products")

def drink_menu(db:list) -> list: 

    """
    This function handles the drinks section of the cafe
    ----------
    - ARGS:
        - db:list --> list of dictionaries
    -------------
    - RETURN:
        - Print(statement)
    """
    #Display drinks
    menuRender(db[2])

    #Asks the user and saves the product requested, sanitizes the input
    orderItem = input("What would you like to order? : ").lower().strip()
    #Asks and saves the size of the product
    orderSize = input("What size would you like to order (small/regular/large)? : ")
    #Asks and saves the amount requested
    orderQty = int(input("How many items would you like to order? : "))
    #Stores the data in a list for being returned and saved in any variable
    summary = [orderItem,orderSize,orderQty]

    return summary


def food_menu(db:list) -> list:
        
        """
        This is the function that manages the food selling
        ----------
        - ARGS:
            - db:list --> list of dictionaries
        -------------
        - RETURN:
            - Print(statement)
        """

        #Display foods and price
        menuRender(db[3],"foods")

        #Asks and saves the food requested
        orderItem = input("What would you like to order? : ").lower().strip()
        #Asks and saves the amount
        orderQty = int(input("How many items would you like to order? : "))
        #Shows the customers what they have ordered
        print(f"You have ordered {orderQty}, {orderItem}")

        summary = [orderItem,orderQty]

        return summary

def book_list(db:list) -> list:
        """
        This is the function that manages books selling
        -------------
        - ARGS:
            - db:list --> list of dictionaries
        -------------
        - RETURN:
            - Print(statement)
        """

        print("Our booklist are as below")
        #Display list of books
        menuRender(db[len(db)-1],"books")
        # We store the information needed into variables
        bookQuestion = "What book would you like to order? : "
        askBookQuantity = "How many books would you like to order? : "
        bookName = input(chatMessage(bookQuestion))
        orderQty = int(input(askBookQuantity))
        bookInfoPurchase = f"You have ordered {orderQty} books titled {bookName}"
        print(chatMessage(bookInfoPurchase))

        summary = [bookName,orderQty]

        return summary


#############################################
# EMPLOYEES
#############################################

def employee_details(db:list) -> print():

    """
    This function manages the employee mode
    -----------------
    - ARGS:
        - db (list) --> the database
    """   

    print("="*60)
    print("You are at PYTHON RANGERS BOOK CAFE employee page")
    print("="*60)

    staffId = int(input("Enter your staff id for authentication: "))
    accessKey = input("Enter your access key for authentication: ")

    for details in db[1].values():
        if staffId == details["staffid"] and accessKey == details["accesskey"]:
            keep = "yes"
            while keep == "yes":
                item = input("What Item Menu would you wish to update? Type food, drinks or books: ").lower()
                if item == "food":
                    itemKey = int(input("Enter the Item Key (numbers only): "))
                    itemName = input("Enter the Item Name: ")
                    itemValue = input(f"enter the value for {itemName}: ")
                    # This line of code update the temporary dictionary stored in the variable db but it can't
                    # save the changes permanently because for that we would need to use a file which purposly
                    # is meant to save data as a .json file for example not a .py but for the purposes of the
                    # exercise works.
                    db[3][itemKey][itemName] = itemValue

                elif item == "drinks":
                    itemKey = int(input("Enter the Item Key (numbers only): "))
                    itemName = input("Enter the Item Name: ")
                    itemValue = input(f"enter the value for {itemName}: ")
                    db[2][itemKey][itemName] = itemValue 
                elif item == "books":
                    itemKey = int(input("Enter the Item Key (numbers only): "))
                    itemName = input("Enter the Item Name: ")
                    itemValue = input(f"enter the value for {itemName}: ")
                    db[4][itemKey][itemName] = itemValue
                print(f"Modification Done!!")    
                keep = input("Do you want to keep modifiying items? (yes/no): ")


#############################
#          CUSTOMER         #
#############################
                
def business_logic(db:dict):

    buyMeMore = "What Item would you wish to order? Type food or drinks or books: "
    item = input(chatMessage(buyMeMore)).lower()

    if item == "drinks":
        orders = drink_menu(db)
        price = price_picker(db,"drinks",orders[0],orders[1])
        drinks_bill["product"].append(orders[0])
        drinks_bill["quantity"].append(orders[2])
        drinks_bill["price"].append(price)
        
    #Recall food function
    elif item == "food":     
        orders = food_menu(db)
        price = price_picker(db,"food",orders[0])
        foods_bill["product"].append(orders[0])
        foods_bill["quantity"].append(orders[1])
        foods_bill["price"].append(price)
    #Recall book function.
    elif item == "books":
        orders = book_list(db)
        price = price_picker(db,"books",orders[0])
        books_bill["product"].append(orders[0])
        books_bill["quantity"].append(orders[1])
        books_bill["price"].append(price)




def autoPackagesInstaller():
    """
    This function checks if the python environment meets the libraries
    requirements for the software works properly
    """
    # reads the requirements.txt file and elaborates a list of packages needed
    def get_requirements():
        with open('requirements.txt', 'r') as f:
            return [line.strip() for line in f.readlines()]
    # store the packages needed for the for loop
    REQUIRED_PACKAGES = get_requirements()

    for package in REQUIRED_PACKAGES:
        # try to retrieve the package information
        try:
            # this variable tries to get the info of the packages
            dist = pkg_resources.get_distribution(package)
            print(chatMessage('Great!, {} ({}) already Installed'
                              .format(dist.key, dist.version)))
        # if the package info retrieval fails, execute the installation of them
        except pkg_resources.DistributionNotFound:
            print(chatMessage("I've found there are some requirements missing"))
            print(chatMessage("don't stress out I will install them"))
            print('{} INSTALLING...'.format(package))
            # this system library install the packages not found
            subprocess.call([sys.executable, '-m', 'pip', 'install', package])




