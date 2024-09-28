# Main Template

# def main(): — This function is where you place the main logic of your exercise. It can be more complex as needed.
# if __name__ == "__main__": — This ensures that the script is only executed when run directly (not when imported as a module in another script).
# Execution — Running python exercise-name.py from the terminal will execute the main() function and print "This is a simple Python exercise!".

def main():
    # Program Logic
    
    # Create a script that prompts for a data center location.
    dclocation = input("Insert Datacentre location: ")

    print("Upper case: " + dclocation.upper() + "\n")
    print("Show whitespace" + repr(dclocation))
    print("Remove whitespace and uppercase, while checking for whitespace left: " + repr(dclocation.upper().strip()))

if __name__ == "__main__":
    # This block only runs if the script is executed directly
    main()