
verification_amount = 1500

data_base = {}


menu = """
   *----------------------------------------------*
   |            Welcome to icenet                 |
   |______________________________________________|
   |  available commands:📲 📱                    |
   |----------------------------------------------|
   |   1. already have account?  select 1 to login|          |
   |______________________________________________|
   |   2. don't have account? select 2 to register|
   *----------------------------------------------*

"""
#print(" ")

print(menu)

data_base = {
    "iceking": {"username": "iceking",
                "password": "admin123",
                "initial_bal": 2000,
                "is_verified": True
    }
}

choice = int(input("enter command:  "))

print(" ")

if choice == 2:
    print("Fill in the form below to create your account...\n")
    username = input("username:  ")
    print(" ")
    password = input("password:  ")
    print(" ")
    initial_bal = float(input("deposit amount: "))

    user1 = {
        "username": username,
        "password": password,
        "initial_bal": initial_bal,
        "is_verified": False
    }
    data_base.update(user1) 

elif choice == 1:
    print("Enter your details to login: ")

#print(data_base)
