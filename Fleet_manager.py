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

        opt = input("Select Option: ") 
        if opt == "1": 
                display_roster()  # initialises menu

        if opt == "2": 
                add_member()


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
       else: 
              print("Invalid Id")  
              add_member()
              
       
        





def main():  
        init_database()   
        display_menu() 


main() 

