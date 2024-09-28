# Main Template

# def main(): — This function is where you place the main logic of your exercise. It can be more complex as needed.
# if __name__ == "__main__": — This ensures that the script is only executed when run directly (not when imported as a module in another script).
# Execution — Running python exercise-name.py from the terminal will execute the main() function and print "This is a simple Python exercise!".

def main():
    # extract the serial number from the output of show version command

    line = "Processor board ID FAL127990LA"
    
    print("\n" + line)

    #unpack into 4 variables
    var1, var2, var3, var4 = line.split()

    print("\n" + var4)
    #alternatively better, use a list
    words = line.split()

    print("\n" + words[3] + "\n")

if __name__ == "__main__":
    # This block only runs if the script is executed directly
    main()