n = ["Picard", "Riker", "Data", "Worf", "La Forge"]
r = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Lieutenant"]
d = ["Command", "Command", "Operations", "Security", "Engineering"]
f = ["10", "12", "14", "18", "22"]

def display_menu(): 
        name = input("User Full Name: ") 
        print("MENU: ") 
        print("User: " + name) 
        print("1: Display Roster -") 

        opt = input("Select Option: ") 
        if opt == "1": 
                display_roster()

def display_roster(): 
        print("Current Crew Roster -")
        for i in range(len(n)): 
                print() 


def init_database()  :
 for i in range(len(n)): 
                print(n[i] + ": " + r[i] + " - " + d[i] + " #" + f[i])


def main():  
        display_menu()
        init_database()   


main() 

