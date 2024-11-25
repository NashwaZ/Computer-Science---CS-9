print("This is a weather checker - enter todays wetaher conditions and this code will assess how 'perfect' it is. ")


'''
Ideal:
weath == sunny
temp == 76
windsp == '15mph' 
humidity == 45
rain == 'no'
'''

temp = int(input("Enter todays tempreture: "))
weath = input("Whats the weather like today eg. cold, sunny: ")
windsp = int(input("Enter the wind speed today eg. 12: "))
humidity = int(input("Enter todays humidity level eg. 30: "))
rain = (input('Is it raining? yes or no: '))

if temp == 76 and weath == 'sunny' and windsp == 15 and humidity == 45 and rain == 'no':
    print('The weather conditions today are ABSOLUTELY PERFECT')
elif temp > 70 and temp < 76 and (weath == 'sunny'or 'hot') and windsp >  10 and windsp < 15 and humidity < 55 and rain == 'no':
    print("The weather conditions are ALMOST perfect")
elif temp > 65 and temp <= 69 and (weath == 'sunny' or 'hot') and windsp > 8  and windsp < 16 and humidity > 55 and humidity < 60 and rain == 'no':
    print("The weather conditions are OKAY")
elif temp > 55 and temp < 69 and (weath == 'sunny' or 'hot' or "warm" or 'okay') and windsp > 7 and windsp < 18 and humidity > 60 and humidity < 70 and rain == 'yes':
    print("The weather is BEARABLE")
else:
    print("Unfortunetly, the weather conditions are HORRIBLE for your pleasure.")
