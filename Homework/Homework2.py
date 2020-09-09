#5-10 Checking Usernames

def check_users(current_users, new_users):
    pass

current_users = ['janet', 'kayla', 'JAY', 'lucy', 'bill']
new_users = ['lily', 'jay', 'thomas', 'kayla', 'patrick']
lower_current_users = []
for user in current_users:
    lower_current_users.append(user.lower())

for new_user in new_users:
    if new_user.lower in lower_current_users:
        print('Sorry ' + new_user + ', that username is taken.')
    else:
        print('Ok ' + new_user + ', that username is available!')

if __name__ == "__main__":
    current_users = ['janet', 'kayla', 'JAY', 'lucy', 'bill']
    new_users = ['lily', 'jay', 'thomas', 'Kayla', 'patrick']
    check_users(current_users, new_users)

