n = ["Picard", "Riker", "Data", "Worf", "La Forge"]
r = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Lieutenant"] # crew database
d = ["Command", "Command", "Operations", "Security", "Engineering"]
f = ["10", "12", "14", "18", "22"]
name = input("User Full Name: ") # asks for name and saves for menu
def display_menu(): 
        
        print("MENU: ") 
        print("User: " + name) # prints out users name
        print("1: Display Roster -")  
        print("2: Add Crew -") 
        print("3: Remove Crew -") 
        print("4: Update Rank -")

        opt = input("Select Option: ") 
        if opt == "1": 
                display_roster()  # initialises menu

        if opt == "2": 
                add_member() 

        if opt == "3": 
               remove_member() 

        if opt == "4": 
               update_rank() 
        
        if opt == "5": 
               search_crew()
               


def display_roster(): 
        print("Current Crew Roster -") 
        print("Name:   Rank:   Divison:  Id:")
        for i in range(len(n)): 
                print(n[i] + ": " + r[i] + " - " + d[i] + "  #" + f[i])  
        display_menu() 


def init_database()  : 
 print("Welcome")  
 print("Initialising Database . . . .")
 print("Current Crew: ") 
 for row in zip(n,r,d,f): 
        print(row)
 #for i in range(len(n)): 
                #print(n[i] + ": " + r[i] + " - " + d[i] + " #" + f[i]) #displays crew and their roles + divs
 print("Loading Menu . . . . .") 

def add_member():  
       nm = input("Enter Name: ") 
       rk = input("Enter Rank: ")  
       if rk not in r: 
              print("Invalid Rank")  
              add_member() 
       else:
        dv = input("Enter Division: ") 
        id = input("Enter Valid Id: ")  

       if id not in f: 
              f.append(id) 
              n.append(nm) 
              d.append(dv) 
              r.append(rk)  
              display_menu() 
       else: 
              print("Invalid Id")  
              add_member()
              

def remove_member(): 
       x = input("Id of crew to remove: ") # gets id of crew then uses index to see which column it is in then removes all valuex in that column
       im = f.index(x) 
       n.pop(im) 
       r.pop(im)
       d.pop(im)
       f.pop(im) 
       print("Removed: " + x) 
       display_menu()

def update_rank(): 
       up = input("Id of Crew Member: ") # asks for id then uses index to get number in list in order to replace that value
       pp = f.index(up)  
       rak = input("Updated Rank: ")
       r[pp] = rak # raplaces rank(r) of column(pp) with rank(rak)
       print("New Rank: " + rak)  
       display_menu()  


def search_crew(): 
     sr =  input("Enter search term: ")
     
     if sr == "Name": 
            for i in range(len(n)): # asks for term then searches and prints all results for that term 
             print(n[i])
     elif sr == "Rank":
            for i in range(len(n)):
             print(r[i]) 
     elif sr == "Division": 
            for i in range(len(n)): 
             print(d[i]) 
     elif sr == "Id": 
            for i in range(len(n)): 
             print(f[i]) 
     else:
            print("Invalid Term") 
            search_crew()  
     display_menu() 

     


 
 




        





def main():  
        init_database()   
        display_menu() 


main() 

