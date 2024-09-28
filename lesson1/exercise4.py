# Main Template

# def main(): — This function is where you place the main logic of your exercise. It can be more complex as needed.
# if __name__ == "__main__": — This ensures that the script is only executed when run directly (not when imported as a module in another script).
# Execution — Running python exercise-name.py from the terminal will execute the main() function and print "This is a simple Python exercise!".

def main():
    # do a membership check on the string for the following text:

    validate = "Processor board ID"

    line = "Processor board ID FAL127990LA"
    
    #print the output
    print("\n" + line)

    #check membership
    if validate in line:
        print("\nThe command output relates to the following Serial Number:")
        print("\n" + line.split()[3] + "\n")

if __name__ == "__main__":
    # This block only runs if the script is executed directly
    main()