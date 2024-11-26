import os

def main():
    # Access environmental variables
    username = os.environ.get('USERNAME')
    password = os.environ.get('PASSWORD')
     # Note: In a real application, never print passwords!
    print(username,password)

    if username and password:
        print(f"Logged in as: {username}")
    else:
        print("Environmental variables not found")

if __name__ == "__main__":
    main()