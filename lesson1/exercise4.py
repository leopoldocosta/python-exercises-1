# Main Template

# def main(): — This function is where you place the main logic of your exercise. It can be more complex as needed.
# if __name__ == "__main__": — This ensures that the script is only executed when run directly (not when imported as a module in another script).
# Execution — Running python exercise-name.py from the terminal will execute the main() function and print "This is a simple Python exercise!".

def main():
    # string concatenation

    ip_addr = "10.12.17.1"
    mac_addr = "0024.c4e9.48ae"

    print("\n" + ip_addr + "-->" + mac_addr)

if __name__ == "__main__":
    # This block only runs if the script is executed directly
    main()