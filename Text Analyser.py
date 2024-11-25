print("This is a text analyser: ALL THE INFORMATION YOU PROVIDE WILL BE USED FOR TESTING PURPOSES")

mstring = input("Write a short sentence or few about your favorite sports team: ")
# Example: Barcelona FC. Barcelona FC is one of the biggest football teams in all of europe. They have acquired 5 champions league trophies and multiple La Ligas. Some may even regard Barcelona Football Club as one of the best in the world.

print(len(mstring)) # Character count
r = mstring.split() # Words seperated (into list)
print(r) 
print(len(r)) # Word count

print(mstring.upper()) # Transformed to Upper Case
print(mstring.lower()) # Transformed to lower Case

print(mstring.replace("football","soccer")) # Replacing words
print(mstring.replace('t','dr')) # Replacing specified letters
print(mstring.find("biggest"))  # Locating word
print(mstring.find("e",29,40)) # Locating letter between range of characters

l = input("which letter/word's position do you wish to locate? : ")

x = mstring.find(l)

print("The location of the letter your is: ",x)  
