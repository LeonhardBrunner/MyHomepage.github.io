def main():

    name = input("Enter your name: ")
    while True:
        if name == "":
            print("Name cannot be empty. Please enter your name.")
            name = input("Enter your name: ")
        else:
            print(f"Hello, {name}!")
            break

    #while len(name) == 0:
    #    print("Name cannot be empty. Please enter your name.")
    #    name = input("Enter your name: ")
    #    break

if __name__ == "__main__":
    main()