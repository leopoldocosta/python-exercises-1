# Main Template

def main():
    # string concatenation

    ip_addr = "10.12.17.1"
    mac_addr = "0024.c4e9.48ae"

    print("\n1. String concatenation:")
    print(ip_addr + " --> " + mac_addr + "\n")

    # using f-strings
    print("2. Using f-strings")
    print(f"{ip_addr} --> {mac_addr}\n")

    #using format() method
    print("3. Using format method:")
    print("{} --> {}\n".format(ip_addr,mac_addr))


if __name__ == "__main__":
    # This block only runs if the script is executed directly
    main()