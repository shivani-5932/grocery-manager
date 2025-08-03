
items=["Milk","Bread","Eggs","Rice","Chicken Breast","Tomatoes","Apples","Dish Soap","Toothpaste","Coffee Powder"]
category=["Dairy","Bakery","Dairy","Grains/Pantry","Meat","Vegetables","Fruits","Household","Personal Care","Beverages"]
quantity=["2L","1Loaf","12Pcs","5Kg","1Kg","1Kg","6Pcs","1Bottle","1Tube","1Pack"]
priority=["High","Medium","High","Low","High","High","Medium","Medium","Medium","Low"]
instock=["No","Yes","No","Yes","No","No","Yes","No","No","Yes"]
notes=["Buy full cream","Use before friday","Needed for breakfast","Enough for 2 weeks","For dinner prep","Check for fresh ones","Use for snacing","Prefer lemon fragrance","Colgate preferred","Still half left"]
def addItem():
    newItem=input("Please enter the item you want to ad in your Grocery List")
    items.append(newItem.capitalize())
    cat=input(f"Enter the category of {newItem}")
    category.append(cat.capitalize())
    qty=input(f"Enter the quantity needed for {newItem}")
    quantity.append(qty)
    pty=input(f"Enter the priority needed for {newItem}")
    priority.append(pty.capitalize())
    instk=input(f"Enter 'Yes' if {newItem} is in stock otherwise enter 'no'")
    instock.append(instk.capitalize())
    note=input(f"Enter a note for {newItem}")
    notes.append(note.capitalize())
def removeItem():
    rmvItem=input("Please enter the item you want to remove from your Grocery List ")
    rmvItem.title()
    if rmvItem not in items:
       print (f"{rmvItem} not in your Grocery list")
    else:
       x=items.index(rmvItem)
       items.remove(rmvItem)
       category.remove(category[x])
       quantity.remove(quantity[x])
       priority.remove(priority[x])
       instock.remove(instock[x])
       notes.remove(notes[x])
       print(f"Removed {rmvItem} successfully!")
def purchase():
    print("Here is the list of items to be purchased")
    for x in range(len(items)):
      if instock[x]=="No":
          print(items[x])
       
def viewGroceryList():
   print("{:<20} {:<20} {:<15} {:<10} {:<10} {:<30}".format("ITEM","CATEGORY","QUANTITY","PRIORITY","INSTOCK","NOTE"))
   for x in range(len(items)):
      row=[items[x],category[x],quantity[x],priority[x],instock[x],notes[x]]
      print("{:<20} {:<20} {:<15} {:<10} {:<10} {:<30}".format(*row))
     
def userInput():
    n=input(""" Type...
        'View List' to take a look at your Grocery List
        'Add Item' to add an item in your Grocery List
        'Remove Item' to remove an item from your Grocery List
        'Review List' to recheck/review your Grocery List after making the changes
        'Out of stock' to check what all do you need to buy
        'Exit' when you are done making changes and reviewing your Grocery List
        
        """)
    match (n.title()):
       case 'View List':
          viewGroceryList()
          userInput()
       case 'Add Item':
          addItem()
          userInput()
       case 'Remove Item':
          removeItem()
          userInput()
       case 'Review List':
          viewGroceryList()
          userInput()
       case 'Out Of Stock':
          purchase()
          userInput()
       case 'Exit':
          print("Thank-you!")
      
       case _:
          print("Sorry, Invalid input. Please try again")
          userInput()
userInput()  



    
   




    

