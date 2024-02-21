def database() -> list:

    """
    This is the storage of our application
    --------------
    - RETURN:
        - list()
    """
    customerDetails = {
        'firstname': "Ammerin",
        'lastname': "Sangsai",
        'address': "Dublin"
    }


    employees = {
    'Joel': {'staffid': 1001, 'accesskey': 'bcjl123'},
    'Libin': {'staffid': 1002, 'accesskey': 'bcln123'},
    'Eoin': {'staffid': 1003, 'accesskey': 'bcen123'},
}

    drinksMenu = {
    1: {'name': 'latte', 'size': 'small', 'price': 2.90, 'quantity': 100},
    2: {'name': 'latte', 'size': 'regular', 'price': 3.20, 'quantity': 100},
    3: {'name': 'latte', 'size': 'large', 'price': 3.40, 'quantity': 100},
    4: {'name': 'tea', 'size': 'small', 'price': 2.80, 'quantity': 100},
    5: {'name': 'tea', 'size': 'regular', 'price': 3.10, 'quantity': 100},
    6: {'name': 'tea', 'size': 'large', 'price': 3.30, 'quantity': 100},
    7: {'name': 'coke', 'size': 'regular', 'price': 1.60, 'quantity': 100},
    8: {'name': 'coke', 'size': 'small', 'price': 1.60, 'quantity': 100},
    9: {'name': 'coke', 'size': 'large', 'price': 2.10, 'quantity': 100},
    10: {'name': 'fanta', 'size': 'regular', 'price': 1.50, 'quantity': 100},
    11: {'name': 'fanta', 'size': 'large', 'price': 2.00, 'quantity': 100},
    12: {'name': 'fanta', 'size': 'small', 'price': 2.00, 'quantity': 100},
    13: {'name': 'water', 'size': 'regular', 'price': 1.50, 'quantity': 100},
    14: {'name': 'water', 'size': 'large', 'price': 2.00, 'quantity': 100},
    15: {'name': 'water', 'size': 'small', 'price': 1.00, 'quantity': 100}
}

    foodMenu = {
    1: {'name': 'chicken sandwitch', 'price': 2.50, 'quantity': 40},
    2: {'name': 'cheese sandwitch', 'price': 2.30, 'quantity': 40},
    3: {'name': 'chicken goujons', 'price': 2.80, 'quantity': 40},
    4: {'name': 'mexican rice', 'price': 3.10, 'quantity': 20},
    5: {'name': 'potato wedges', 'price': 1.60, 'quantity': 30},
    6: {'name': 'chips', 'price': 1.00, 'quantity': 100},
    7: {'name': 'fish fillet','price': 2.60, 'quantity': 30},
    8: {'name': 'veg salad','price': 2.80, 'quantity': 30}}

    bookList = {
    1: {'name': 'The Happiest Man on Earth', 'author': 'Eddie Jaku', 'price': 8.99, 'quantity': 10},
    2: {'name': 'Manifest', 'author': 'Roxie Nafousi', 'price': 15.99, 'quantity': 10},
    3: {'name': 'The Importance of Being Aisling', 'author': 'Emer McLysaght', 'price': 14.99, 'quantity': 10},
    4: {'name': 'Iron Flame', 'author': 'Rebecca Yarros', 'price': 13.99, 'quantity': 10},
    5: {'name': 'Aisling Ever After', 'author': 'Emer McLysaght', 'price': 18.99, 'quantity': 10},
    6: {'name': 'Prophet Song P/B', 'author': 'Lynch Paul', 'price': 15.99, 'quantity': 10},
    7: {'name': 'Happy Mind, Happy Life', 'author': 'Dr Rangan Chatterjee', 'price': 13.99, 'quantity': 10},
    8: {'name': 'Harry Potter and the Deathly Hallows', 'author': 'J. K. Rowling', 'price': 7.99, 'quantity': 10},
    9: {'name': 'The Freedom Within', 'author': 'Gerry Hussey', 'price': 14.99, 'quantity': 10},
    10: {'name': 'The Bee Sting', 'author': 'Paul Murray', 'price': 13.99, 'quantity': 10},
    11: {'name': 'Sherlock Homes', 'author': 'Arthur Conan Doyle', 'price': 9.99, 'quantity':9}}
        
    data = [customerDetails,employees,drinksMenu,foodMenu,bookList]

    return data
