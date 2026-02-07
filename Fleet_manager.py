n = ["Picard", "Riker", "Data", "Worf", "La Forge"]
r = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Lieutenant"]
d = ["Command", "Command", "Operations", "Security", "Engineering"]
f = ["10", "12", "14", "18", "22"]
name = input("User Full Name: ")
def display_menu(): 
        
        print("MENU: ") 
        print("User: " + name) 
        print("1: Display Roster -")  
        print("2: Add Crew -")

        opt = input("Select Option: ") 
        if opt == "1": 
                display_roster()  

        if opt == "2":


def display_roster(): 
        print("Current Crew Roster -") 
        print("Name:  Rank:   Divison:   Id:")
        for i in range(len(n)): 
                print(n[i] + ": " + r[i] + " - " + d[i] + " #" + f[i])  
        display_menu() 


def init_database()  : 
 print("Welcome")  
 print("Initialising Database . . . .")
 print("Current Crew: ")
 for i in range(len(n)): 
                print(n[i] + ": " + r[i] + " - " + d[i] + " #" + f[i]) 
 print("Loading Menu . . . . .") 

                



def main():  
        init_database()   
        display_menu() 


main() 

