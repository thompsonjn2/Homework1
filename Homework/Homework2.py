#5-8 Hello Admin:

usernames = ['David','John','Tricia', 'Ashley', 'admin']

for username in usernames:
    if username =='admin':
        print ("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + username + ", thank you for logging in again!")


#5-9 No Users:
usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print ("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + username + ", thank you for logging in again!")
else:
    print('We need to find some users!')

#5-10 Checking Usernames

current_users = ['janet', 'kayla', 'JAY', 'lucy', 'bill']
new_users = ['lily', 'jay', 'thomas', 'kayla', 'patrick']
lower_current_users = []
for user in current_users:
    lower_current_users.append(user.lower())

for new_user in new_users:
    if new_user.lower in lower_current_users:
        print('Sorry ' + new_user + ', that username is taken.')
    else:
        print('Ok ' + new_user + 'that username is available!')

#5-11 Ordinal numbers:

numbers = list = (range(1,10))
for number in numbers:
    if number == 1:
        print('1st')
    elif number == 2:
        print('2nd')
    elif number == 3:
        print('3rd')
    else:
        print(number + 'th')
