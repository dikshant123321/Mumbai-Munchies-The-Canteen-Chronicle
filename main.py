dishCollection = []
orderCollection = []


def addDish(dishId,dishName, price, availability):
    dish = {
        "dishId":dishId,
        "dishName":dishName,
        "price": price,
        "availability": availability
    }
    dishCollection.append(dish)
    print(f"Dish '{dishName}' added .")


def removeDish(dishId):
    for dish in dishCollection:
        if dish["dishId"] == dishId:
            dishCollection.remove(dish)
            print(f"Dish '{dish['dishName']}' removed .")
            return
    print(f"Dish with ID '{dishId}' not found.")


def update_availability(dishId, availability):
    for dish in dishCollection:
        if dish["dishId"] ==dishId:
            dish["availability"] = availability
            print(f"Availability of dish '{dish['dishName']}' updated to '{availability}'.")
            return
    print(f"dish with ID '{dishId}' not found.")


def orderDish(customerName,dishId):
    for dish in dishCollection:
        if dish["dishId"] == dishId:
            if dish["availability"] == "yes":
                dish["availability"] = "no"
                order={
                    "orderId":"1",
                    "customerName":customerName,
                    "dishName":dish["dishName"],
                    "price":dish["price"],
                    "status":"Received"
                }
                orderCollection.append(order)
                print(f"Dish '{dish['dishName']}' Ordered.")
            else:
                print(f"Dish '{dish['dishName']}' is not available.")
            return
    print(f"Dish with ID '{dishId}' not found.")


def printMenu():
    if len(dishCollection) == 0:
        print("Menu cart Empty! .")
    else:
        print("Menu Card:")
        for dish in dishCollection:
            print(f"ID: {dish['dishId']}, Name: {dish['dishName']}, Price: {dish['price']}, Availability: {dish['availability']}")


def printOrderList():
    if len(orderCollection) == 0:
        print("Order List is Empty! .")
    else:
        print("Order record:")
        for order in orderCollection:
            print(f"ID: {order['orderId']}, dishName: {order['dishName']}, price: {order['price']} ,Status: {order['status']}")

def  changeStatus(orderId):
     for order in orderCollection:
        if order["orderId"] == orderId:
            newStatus=input("Enter new Status(Received/Preparing/Delivered): ")
            lowercase_string = newStatus.lower()
            if (lowercase_string=="received" or lowercase_string=="preparing" or lowercase_string=="delivered"):
             order["status"]=newStatus
             print("Thanks for Updating status..")
            else:
                print("Enter Valid Status..")
            
    
    
    
def start():
    print("Welcome to the Zesty Zomato!")
    while True:
        print("\nSelect an option:")
        print("-------------------")
        print("1. Add Menu of dishes ")
        print("2. Remove a Dish")
        print("3. Update the availability of a dish")
        print("4. Take Order from Customer")
        print("5. View Menu")
        print("6. view order List")
        print("7. change Status(Received/Preparing/Delivered)")
        print("8. Quit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            dishId = input("Enter Dish ID: ")
            dishName = input("Enter Dish name: ")
            price = input("Enter Dish price: ")
            availability = input("Enter Dish availability (yes/no): ")
            addDish(dishId,dishName, price, availability)
            
        elif choice == "2":
            dishId = input("Enter Dish ID to remove: ")
            removeDish(dishId)
            
        elif choice == "3":
            dishId = input("Enter Dish ID to update availability: ")
            availability = input("Enter new availability (yes/no): ")
            update_availability(dishId, availability)
            
        elif choice == "4":
            customerName=input("Enter Customer Name: ")
            dishId= input("Enter Dish ID to Order: ")
            orderDish(customerName,dishId)
            
        elif choice == "5":
            printMenu()
        elif choice == "6":
            printOrderList()
        elif choice == "7":
            orderId=input("Enter Order Id: ")
            changeStatus(orderId)
        elif choice == "8":
            break
        else:
            print("Invalid input. Please enter a valid choice (1-7).")


start()



