password = str(input(f'Enter a Password: '))

length = False

print(password)

if len(password) < 8:
    print('Not enough characters')
    length = True

if len(password) > 15:
    print('Too many characters')
    length = True



z = True
upper = True
exell = True

password_2 = password

symbol_list = ['!', '@', '#', '$', '%', '^', '&', 
               '*', '(', ')', '_', '-', '+', '=',
                 '`', '~', ',', "'", '"', ';', ':', 
                 '<', '>', '.', '?', '/', '[', ']', 
                 '{', '}', '|']

checker = False
y = 0
x = 0
for i in range(len(password)):
    y = 0
    for i in range(len(symbol_list)):
         if password[x] == symbol_list[y]:
              checker = True
              break
         y += 1
    y = 0
    if password[x] == symbol_list[y]:
        checker = True
        break

    x += 1
    
      


if checker:
    if "Z" in password or "z" in password:
        if password[0].isupper():
            if '!' == password[len(password) - 1]:
                print('Accept')
            else:
                print('Need to use ! at the end')
                print('Reject')
        else:
                print('Reject')
                print('Need to use an UpperCase for the first letter')
else:
    print('Reject')


    


