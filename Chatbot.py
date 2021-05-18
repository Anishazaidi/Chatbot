print("Welcome to flipkart online centre")
Name=input("enter a name:")
print("hii",Name,"how can i help you")
print("What you want know about: \n 1.About flipkart founder 1 \n 2.Branches of flipkart 2  \n 3.online shopping process 3\n 4.Payback process 4\n 5.To know about materials") 
Help=int(input("please ask what you want to know?"))
if Help==1:
    print("sachin bansal was the founder of flipkart")
    know_more=input("know more about flipkart shopping:")
    if know_more=="yes":
        print("flipkart is a online shopping centre which is used to save the time")
        facilities=input("to know about facility enter yes")
        if facilities=="yes":
            print("Facilites are good!,Here the customers felt happy to do online shopping for their needs in emergency when they do not have time to do shopping")
        else:
            print("thanks for connecting our online shopping centre")    
    else:
        print("thank you")    
elif Help==2:
    print("there are three main branches in flipkart based on ur needs")
    To_know=input("to know enter yes or no")
    if To_know=="yes":
        print("bangalore,hyderabad,chennai")
        more_to_know=input("more to know enter yes or no")
        if more_to_know=="yes":
            print("bangalore,chennai,and hyderabad is available to the all cities")
        else:
            print("thanks for connecting us")
    else:
        print("thank you")            
elif Help==3:        
    print("for doing shopping in flipkart you have to clear about the 5 steps")
    steps=input("steps to know enter yes or no ")
    if steps=="yes":
        print("first select an item,second choose colour,third clarity about payment,fourth check which type of payment is available,and fifth clarify in how many days it will delivered") 
    else:
        print("thanks for connecting")
elif Help==4:
    print("after getting flipkart service just give ur review through the ratings")    
elif Help==5:
    print("the quality of material is good and it is used to you when ur going to the parties")
    know_about=input("enter to know about press yes or no:")
    if know_about=="yes":
        print(" here every item have their unique identification like quality of cloth and richness") 
    else:
        print("thank you")           
if(True):
    print("thanks for connecting us")      
    print("if you want to know more about flipkart visit this website.http://flipkart.com")