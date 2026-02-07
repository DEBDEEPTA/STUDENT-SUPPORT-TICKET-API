from schemas.user import User

u1 = User(
    user_id="CS033",
    user_name = "DEBDEEPTA SAMUI",
    email = "askdev2003@gmail.com",
    password= "Dev2oo3"
)

u2 = User(
    user_id="CS034",
    user_name= "BRIJESH GABA",
    email= "brijesh@gmail.com",
    password= "brijesh1234"
)

u3 = User(
    user_id= "CS065",
    user_name= "DHIRAJ KUMAR M",
    email = "dhiru@gmail.com",
    password="dhiru1234"
)

a1 = User(
    user_id= "AD243",
    user_name= "SAM Varghese",
    email = "sam@gmail.com",
    password="sam1234"
)

a2 = User(
    user_id= "AD248",
    user_name= "Suriya P.",
    email = "suriya@gmail.com",
    password="suriya1234"
)

def get_users():
    return u1,u2,u3

def get_admins():
    return a1,a2


if __name__=="__main__":
    # TESTING GET_USERS TO OBTAIN IN MEMORY USERS
    for user in get_users():
        print("="*30)
        print(user.user_id)
        print(user.user_name)
        print(user.email)
        print(user.password)

    # TESTING GET_ADMINS TO OBTAIN IN MEMORY USERS
    for admin in get_admins():
        print("="*30)
        print(admin.user_id)
        print(admin.user_name)
        print(admin.email)
        print(admin.password)