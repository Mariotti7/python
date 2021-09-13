print('==== Access System ====')
answer='YES'
while answer == 'YES' :
    access_level=input('Type your access level: ').upper()
    if access_level=='ADM' or access_level=='USR' :
        gender=input('Type your gender: ').upper()
        if access_level=='ADM' :
            if gender=='FEMALE':
                print('Hello, administratrix!')
            else :
                print('Hello, administrator!')
        else :
            if gender=='FEMALE' :
                print('Hi, user X!')
            else : 
                print('Hi, user Y!')
    elif access_level=='GUEST' :
        print('Hey, guest!')
    else :
        print('Hello, no one!')
    answer=input('Type YES to continue: ').upper()
print('==== System Out ====')