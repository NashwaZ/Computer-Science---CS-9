#This is a Text Searcher!

print("Welcome to the Python Text Searcher!")



para = input('Enter your text: ')
p = para.lower()



ff = p.find('football')
fc = p.count('football')

fb = p.find('beautiful')
bc = p.count('beautiful')

fbig = p.find('big')
bigc = p.count('big')



if 'football' in p:
    print(f'The word football is in your text, first at charcter number {ff}, and is mentioned in the text {fc} time(s) ')
else:
    print("The word football does not exist in your text.")
\

if 'beautiful' in p:
    print(f'The word beautiful is in your text, first at charcter number {fb}, and is mentioned in the text {bc} time(s) ')
else:
    print("The word beautiful does not exist in your text.")
\

if 'big' in p: 
    print(f'The word big is in your text, first at charcter number {fbig}, and is mentioned in the text {bigc} time(s) ')
else:
    print("The word big does not exist in your text.")
\

user_wish = input('Alongside, the three words our code checks for, is there any words you wish to find and locate? if so enter the word, otherwise enter no:  ')

if user_wish != 'no' or 'n':
    u = p.find(user_wish)
    uc = p.count(user_wish)
    print(f'The word {user_wish} is in your text, located at character number {u} and is mentioned {uc} time(s)')
else:
    print(f'The word {user_wish} does not exist in your text.')



