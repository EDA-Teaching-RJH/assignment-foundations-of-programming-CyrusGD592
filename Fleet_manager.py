n = ["Picard", "Riker", "Data", "Worf", "La Forge"]
r = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Lieutenant"]
d = ["Command", "Command", "Operations", "Security", "Engineering"]
f = ["10", "12", "14", "18", "22"]



def init_database()  :
 for i in range(len(n)): 
                print(n[i] + ": " + r[i] + " - " + d[i] + " #" + f[i])


def main():
        init_database()   


main() 

