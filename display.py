from project2 import DBHelper
def login():
    print("************LogIn*************")

    help= DBHelper()          
    u_id=int(input("User_Id="))
    u_first_name=input("FirstName= ")
    u_last_name=input("lastName= ")
    u_email=input("Email= ")
    u_phone=input("Phone= ")
    while True:
        if "@gmail.com" not in u_email:
            print("Enter a valid Email!")
            login()
        break
               
    help.insert_user(u_id,u_first_name,u_last_name,u_email,u_phone)
            
        
#help.insert_user(u_id,u_first_name,u_last_name,u_email,u_phone)

def main():
    helper = DBHelper()
    while True:
        user_input=input('''

--------------------------------------------------
|*************WHAT DO YOU WANT TO DO?************|
-------------------------------------------------
|                                                |
| [(1) View-A] |  to view  all  saved contacts   | 
| [(2) View]   |  to view a specific conntacts   |
| [(3) Add]    |  to add a new contacct          |
| [(4) Delete] |  to add a new contact           |
| [(5) Update] |  to update a contact            |
| [(6) Exits]  |  to exits the program           |
|                                                |
|------------------------------------------------|
''').upper()
        try:

            if user_input=="VIEW-A" or user_input=="1":

                helper.fetch_all()

            elif user_input=="VIEW" or user_input=="2":
                while True:
                    u_fetch=input('''How do you want to fetch the user
                    by :- (1) User_Id  | (2) User_Name \n''').upper()
                    if u_fetch=="USER_ID"or u_fetch=="USERID" or u_fetch=="1":
                        u_id=int(input("User_Id= "))
                        helper.fetch_one_by_id(u_id)
                        break
                    if u_fetch=="USER_NAME" or u_fetch=="USERNAME" or u_fetch=="2":
                        u_first_name=input("FirstName= ")
                        u_last_name=input("lastName= ")
                        helper.fetch_one_by_name(u_first_name,u_last_name)
                        break

            elif user_input=="ADD" or user_input=="3":
                u_id=int(input("User_Id="))
                u_first_name=input("FirstName= ")
                u_last_name=input("lastName= ")
                u_email=input("Email= ")
                u_phone=input("Phone= ")
                
                while True:
                    if "@gmail.com" not in u_email:
                        print("Enter a valid Email!")
                        break
        
                    else:          
                        helper.insert_user(u_id,u_first_name,u_last_name,u_email,u_phone)
                        break

                

            elif user_input=="DELETE" or user_input=="4":
                u_id=int(input("User_Id= "))

                helper.delete_user(u_id)

            elif user_input=="UPDATE" or user_input=="5":
                while True:
                    update_input=input("What do you want to update?  ((1)NAME OR (2)PHONE OR (3)EMAIL)=").upper()
                    if update_input=="NAME" or update_input=="1":
                        u_id=int(input("User_Id= "))
                        u_first_name=input("FirstName= ")
                        u_last_name=input("lastName= ")
                        helper.update_user_name(u_id,u_first_name,u_last_name)
                        break
                    if update_input=="PHONE" or update_input=="2":
                        u_id=int(input("User_Id= "))
                        u_phone=input("Phone= ")
                        helper.update_user_phone(u_id,u_phone)
                        break
                    if update_input=="EMAIL" or update_input=="3":
                        u_id=int(input("User_Id= "))
                        u_email=input("Email= ")
                        helper.update_user_email(u_id,u_email)
                        break




            elif user_input=="EXITS" or user_input=="6":
                break
            else:
                print("Invalid input ! Try again")
        except Exception as e:
            print(e)
            print("Invalid Details ! Try again")

login()


if __name__=="__main__":
    main()