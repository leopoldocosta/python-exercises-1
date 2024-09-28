# Main Template

# def main(): — This function is where you place the main logic of your exercise. It can be more complex as needed.
# if __name__ == "__main__": — This ensures that the script is only executed when run directly (not when imported as a module in another script).
# Execution — Running python exercise-name.py from the terminal will execute the main() function and print "This is a simple Python exercise!".

def main():
    # Program Logic
    
    # Create a variable named 'sf_gw1', assign it an IP address of 172.31.255.1/24
    ip1 = "172.31.255.1/24"
    ip2 = input("sf_gw1 IP address is: " + ip1 + ". Type sf_gw2 IP address: ")

    name1 = "sf_gw1"
    name2 = "sf_gw2"

    header = "-" * 20

    print()
    print(f"{name1:^20}{name2:^20}")
    print(f"{header:^20}{header:^20}")
    print(f"{ip1:^20}{ip2:^20}")

if __name__ == "__main__":
    # This block only runs if the script is executed directly
    main()