print('Welcome! This is your very own story creator - just type in a few words and this code will do the rest!')


theme = input("First, select a theme -  hope, dystopian, hierarchy, horror:  ")
print("NOTE: if you do not choose a theme mentioned above the code will resort to a general story (horror)")

if theme =='hope':
    hp_character = input("Let's begin this hopeful journery with our charcater's name: ")
    adj_for = input("Enter the first adjective you think of when you picture a forest: ")
    adj_tree = input("Enter an interesting adjective to describe a tree: ")
    adj_birds = input("Now, Enter the first adjective you think of when you imagne birds making sounds: ")
    adj_storm = input("Choose a fitting adjective to describe a storm: ")
    an_dest = input("Enter a synonym for the word destroyed: ")
    adj_mat = input("Enter an adjective with a positive connotation to describe materials - eg. adeqaute or required: ")
    it_nes = input("Enter a material you would need to build a nest - exlcuding sticks & twigs: ")
    adj_har = input("Enter an adjective to describe someone working hard - eg. tirelessly: ")
    adj_hom = input("Enter an adjective to describe home - eg. loving: ")
    adj_com = input("Enter an adjective to describe a community - eg. beautiful: ")
    adj_sun = input("Enter an adjective reflecting how the sun shined - eg. brightly: ")
    adj_smel = input("Enter an adjective to describe a smell: ")
    adj_mor = input("Enter a synonym for the word beautiful: ")
    adj_det = input("Enter a synonym for the word determined: ")
    fin_lis = input("Lastly, Enter a word that fitsunity in the following list - peace, love, and : ")
    print("")

    print(f'''Once upon a time, there was a small bird named {hp_character}. {hp_character} lived in a {adj_for} forest filled with {adj_tree} trees and {adj_birds} birds. One day, a {adj_storm} storm hit this {adj_for} forest, and all the trees were destroyed, leaving {hp_character} without a place to call home.
{hp_character} flew from tree to tree, searching for shelter but found nothing. Despair began to set in, but then {hp_character} remembered its mother's words,''where there's life, there's hope'' {hp_character} realized that even though its home was {an_dest}, it was still alive and could create a new home.
{hp_character} began to search for {adj_mat} materials to build a nest. It found sticks, twigs, and {it_nes} and worked {adj_har}, weaving them together to make a cozy and {adj_hom} home. As {hp_character} worked, other birds in the forest saw its determination and came to help. Soon, a {adj_com} new community was formed, filled with hope and love.
The sun shone {adj_sun}, and the flowers bloomed, filling the air with their {adj_smel} fragrance. {hp_character}'s hard work and determination had paid off, and it was now living in a place that was even more {adj_mor} than its old home. From that day on, {hp_character} served as an inspiration to all the other birds in the {adj_for} forest. Whenever they faced a challenge,
they thought of {hp_character} and its unwavering hope and belief that things would get better. They stayed perseverant and {adj_det}, and the forest became a place of peace, love, and {fin_lis}, all because of one little bird's hope.
The end.''')
    


elif theme == 'dystopian':
    char_1 = input("We being this story with our protagonists name - a hero name eg. Hawkeye: ")
    char_2 = input("Next choose a name for the antagonist of this story - the villian: ")
    adj_cit = input('Enter an adjective describing a place: ')
    city = input('Enter a real or fictional name for a city: ')
    wep = input('Enter an item or weapon: ')
    pe_em = input('Enter a negative emotion - eg. sadness: ')
    challenge = input("Enter a an obstacle or problem the hero has to solve - eg. cyborg attack: ")
    friend = input("Enter a your best friends's name: ")
    skill = input("Enter a your best skill: ")
    action = input("Enter an aggresive verb - eg. attack: ")
    secret = input("Enter a secret - eg. a villian was the hero's brother: ")
    out = input("Enter a HAPPY outcome - eg. rejoicement, alliance, partnership: ")
    print("")

    print(f'''In the {adj_cit} ruins of {city}, where hope was a distant memory, a hero named {char_1} fought to reclaim the shattered world. Armed with a trusty {wep}, {char_1} knew that every battle would be fraught with danger and the lingering feeling of {pe_em}.
The city was controlled by the ruthless villain, {char_2}, who had unleashed a devastating {challenge} upon the survivors. As the last remnants of humanity struggled to resist, {char_1} found strength in the bonds of friendship, particularly with {friend}, who shared the same vision of a brighter future.
Using their exceptional {skill}, {char_1} devised a daring plan to {action} against {char_2}'s forces. However, the stakes were higher than ever when {char_1} discovered a shocking {secret}: {secret}. This revelation twisted their purpose, igniting a fire within to not only fight but also to understand the enemy.
As the climactic battle unfolded in the heart of {city}, {char_1} faced the ultimate choice. The outcome would determine not only the fate of the city but the future of humanity itself: would it be a {out} or a tragic defeat?
In that decisive moment, {char_1} realized that heroism sometimes meant embracing the complexities of loyalty and betrayal. And so, with courage and resolve, they charged forward, ready to change the course of history.
The end.''')
    

elif theme ==  'hierarchy':
    leader = input("Enter the name of your leader: ")
    rival = input("Enter the name of your rival: ")
    adj_soc = input("Enter an adjective to describe the society: ")
    city_name = input("Enter a real or fictional city name: ")
    pos = input("Enter a position of power - king, governor: ")
    em = input("Enter a negative emotion - resentment: ")
    obstacle = input("Enter a major challenge -  an uprising, a newcomer, an opponent: ")
    ally = input("Enter the name of an ally: ")
    talent = input("Enter a special talent you have or wish to have: ")
    des_ac = input("Enter a decisive action verb - declare, pronounce: ")
    hid_tr = input("Enter a a short sentence; a twist / truth - eg. the queen had died : ")
    out2 = input("Enter an outcome - eg. change, collapse: ")
    print("")
    

    print(f'''In the {adj_soc} city of {city_name}, a leader named {leader} ruled with an iron fist, holding the position of {pos}. Despite the outward appearance of stability, whispers of discontent brewed beneath the surface, fueled by the rival, {rival}, who sought to dismantle {leader}'s power.
The tension reached a boiling point as {leader} grappled with feelings of {em}. The society was on the brink 
of a(n) {obstacle}, and {leader} knew they had to act swiftly. Turning to their trusted ally, {ally}, {leader} devised a plan to maintain control.
Using their unique ability to {talent}, {leader} prepared to {des_ac} a speech that would rally the citizens. But just as they were about to take the stage, 
a shocking revelation emerged: {hid_tr}. This truth threatened to shatter everything {leader} had built.
Faced with the choice of revealing this hidden truth or maintaining the status quo, {leader} stepped forward, knowing that the outcome would either lead to a {out2}
or plunge the city into chaos. In that moment, the foundations of hierarchy were put to the test. Would {leader}'s courage inspire unity, or would the society crumble under the weight of betrayal?
The end.''')
    

else:
    hchar_1 = input("Enter the name of the protagonist: ")
    hchar_2 = input("Enter the name of the antagonist - monster, ghost: ")
    hplace = input("Enter a creepy location - abandoned house, forest: ")
    hadj_place = input("Enter an adjective to describe the night: ")
    htime = input("Enter a time of day - midnight, dusk: ")
    h_em = input("Enter a negative emotion - fear, dread: ")
    h_so = input("Enter a disturbing sound - whispering, growling: ")
    h_item = input("Enter an object that brings dread - old doll, bloody knife: ")
    h_sec = input("Enter a dark secret about the place - eg. a man had murdered his entire family within the premise: ")
    h_vis = input("Enter a frightening vision - shadowy figure, glowing eyes: ")
    h_chal = input("Enter a challenge the protagonist faces - escape, confront: ")
    h_fr = input("Enter the name of a friend or companion: ")
    h_dis = input("Enter a horrifying discovery - a hidden room: ")
    h_ac = input("Enter an action the protagonist must take - run, hide: ")
    h_end = input("Enter a chilling outcome - escape, possession: ")

    print(f'''On a {hadj_place} night in the depths of {hplace}, {hchar_1} found themselves alone, the air thick with {h_em}. It was {htime}, a time when the darkness seemed alive. As they ventured deeper 
into the shadows, an eerie {h_so} echoed through the trees, sending chills down their spine. lutching an old {h_item}, {hchar_1} felt a wave of dread wash over them. 
They had heard the whispers of a dark secret: {h_sec}. With each step, the weight of the unknown pressed heavier on their heart. 
Suddenly, a {h_vis} flickered in the corner of their eye, leaving {hchar_1} frozen in place. Was it real? Or was it just their imagination? 
But before they could gather their thoughts, the chilling realization struck: they weren't alone. In the darkness, the presence of {hchar_2} loomed, 
and {hchar_1} knew they had to {h_chal} to survive. Panic surged as they recalled the comforting presence of {h_fr}, who had gone missing earlier in the night. 
Driven by fear, {hchar_1} stumbled upon a horrifying discovery: {h_dis}. The sight was enough to make anyone scream, but {hchar_1} knew they had to act. With trembling hands, they decided to {h_ac}, their mind racing with thoughts of escape.
As the night wore on, the tension escalated. Just when it seemed all hope was lost, the darkness closed in, and the ultimate {h_end} awaited them. Would they escape the horrors that lurked, or would they become part of the legend of {hplace} forever?
The end.''')
     



