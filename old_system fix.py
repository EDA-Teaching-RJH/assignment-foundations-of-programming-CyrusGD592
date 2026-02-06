n = ["Picard", "Riker", "Data", "Worf"]
r = ["Captain", "Commander", "Lt. Commander", "Lieutenant"]
d = ["Command", "Command", "Operations", "Security"]

active = True

def run_system_monolith():
    print("BOOTING SYSTEM...")
    print("...")
    print("WELCOME TO FLEET COMMAND")
    
    
    loading = 0
    while loading < 5:
        print("Loading module " + str(loading)) # loading does not increase so dies not stop printing  need function to increase loading level
        loading = loading + 1
        
    
    while True:
        print("\n--- MENU ---")
        print("1. View Crew")
        print("2. Add Crew")
        print("3. Remove Crew")
        print("4. Analyze Data")
        print("5. Exit")
        
        opt = input("Select option: ")
        
        if opt == "1":  #syntax error need == if equals to
            print("Current Crew List:")
            
            for i in range(len(n)): #  range was too high needed to be dynamic when adding or removing crew
                print(n[i] + " - " + r[i]) 
                
        elif opt == "2":
            new_name = input("Name: ")
            new_rank = input("Rank: ")
            new_div = input("Division: ")
            
           
            n.append(new_name) 
            r.append(new_rank) # need to append rank and div as well for it to display
            d.append(new_div)
            print("Crew member added.")
            
        elif opt == "3":
            rem = input("Name to remove: ")
           
            idx = n.index(rem)
            n.pop(idx)
            r.pop(idx)
            d.pop(idx)
            print("Removed.")
            
        elif opt == "4":
            print("Analyzing...")
            count = 0
            
            for rank in r:
                if rank == "Captain" or  rank == "Commander": # displays as all ranks being high ranking officers due to logic error 
                    count = count + 1
            print("High ranking officers: " + str(count)) # count is a interger and needs to be converted to a string to print
            
        elif opt == "5":
            print("Shutting down.")
            break
            
        else:
            print("Invalid.")
            
        
        x = 10
        if x > 5:
            print("System Check OK")
        else:
            print("System Failure")
            
       
        if len(n) > 0:
            print("Database has entries.")
        if len(n) == 0:
            print("Database empty.")

        
        fuel = 100
        consumption = 20     # consumption at 0 so fuel does not decrease
        while fuel > 0:
            
            print("Idling...")
            break 
            
        print("End of cycle.")

run_system_monolith() # need () to run function
