
fav =[]
count = 1

while len(fav) < 5:
    fav.append(input(f"Add something to the list! Whats anything you would considera favorite of yours? this is you no. {count} item: "))
    count +=1
    if len(fav) == 4:
        fav.append(input("This is your final item! enter it here: "))

    print(fav)


fav.sort()
print(fav)