# CN Practice.py

'''
1. User inputs
    1. What is your current rank?
    2. How would you like to train?
        * Current rank
            ** Randomize current belt techniques and specific combos practiced in dojo by sensei recommendation
            ** Ex) Green belt - Start in natural stance, crescent kick, slide into side snap kick
            ** Finish with a rank kata
        * Mixed rank
            ** Randomly select a stance followed by a hand, block, and leg technique
            ** Applies to moves at current rank and below, NOT a higher rank than user input
            ** Finish with any kata?

2. Current rank combos
    1. 1G (One Green Stripe):
    2. 2G (Two Green Stripe):
    3. G (Green Belt):
    4. 1Br (One Brown Stripe):
    5. 2Br (Two Brown Stripe):
    6. Br (Brown Belt)
    7. 1Bl (One Black Stripe)
    8. 2Bl (Two Black Stripe)
    9. Bl (Black Belt)

3. Randomized Combos
    1. Select one item in the list(s) of stances
    2. Select one item in the list(s) of hand techniques
    3. Select one item in the list(s) of block techniques
    4. Select one item in the list(s) of leg techniques
    5. Add footwork before leg technique optionally? (ex.shuffle into side snap kick)

4. Output
    --> Get into a (randomize left or right) stance, [hand technique] followed by [block technique]
    and a [leg technique]. Repeat (between 2 and 10) times.

*** App idea: Notification comes in your phone saying, "Tap to see today's techniques" ***

5. Ideas for Updates
    1. Written test multiple choice study guide?
    2. Code of Ethics fill in the blank?
    3. Assign moves to their youtube embeds on manual.cuongnhu.com
    4. Rank promotion awards? Gameify Cuong Nhu through app?
    5. Add child ranks and red stripe moves
'''

import random  # random function

# INDEX OF ALL CUONG NHU TECHNIQUES

# Stances
stance = ['rectangular stance', 'kicking stance', 'forward stance', 'diagonal stance', 'side stance', 'back stance',
          'inward stance', 'X stance', 'dinh stance', 'turtle stance', 'serpent stance', 'parallel stance',
          'forward parallel stance']

# Hand Techniques
hand = ['lunge punch', 'reverse punch', 'double punch', 'high/low double punch',
        'vertical punch', 'inner chop', 'downward elbow strike', 'roundhouse elbow strike',
        'jab punch', 'cross punch', 'hook punch', 'uppercut punch', 'jab, cross, hook, uppercut',
        'vertical back fist strike',
        'horizontal back fist strike', 'vertical spear hand thrust', 'horizontal spear hand thrust',
        'outer horizontal chop', 'outer diagonal chop', 'lower palm heel strike', 'middle palm heel strike',
        'rising palm heel strike', 'upward elbow strike', 'backward elbow strike', 'forward elbow strike',
        'side elbow strike', 'back roundhouse elbow strike', 'roundhouse punch', 'side punch', 'U punch',
        'hammer strike (top fist)', 'hammer strike (bottom fist)', 'inner ridge hand strike', 'outer ridge hand strike',
        'tiger mouth strike', 'horizontal bent wrist strike', 'upward bent wrist strike', 'downward bent wrist strike',
        'diagonal upward bent wrist strike', 'diagonal downward bent wrist strike', 'looping punch',
        'looping ridge hand', 'palm corner strike', 'horizontal bear hand strike', 'vertical bear hand strike',
        'horizontal bear hand knuckle strike', 'vertical bear hand knuckle strike', 'thumb strike',
        'thumb knuckle strike', 'forefinger knuckle strike', 'middle knuckle strike', 'one-finger strike',
        'two-finger strike', 'scissors punch', 'inner forearm strike', 'outer forearm strike']

# Blocks
block = ['lower block', 'inner middle block', 'rising block', 'double inner middle block',
         'knife hand block', 'outer block', 'reinforced block', 'lower x-block (closed hands)',
         'upper x-block (closed hands)', 'middle low block', 'side elbow block', 'palm heel block',
         'double forearm block', 'lower sliding block', 'middle sliding block', 'rising sliding block',
         'inner shovel block', 'outer shovel block', 'backhand block', 'wedge block', 'arrow block',
         'soft lower block', 'soft inner middle block', 'soft rising block', 'soft outer block (monkey)',
         'low sweeping block', 'middle sweeping block', 'high sweeping block', 'downward forearm block',
         'bottom hammer fist block', 'soft knife hand block (crane)', 'soft elbow block', 'soft middle low block',
         'grasping block', 'circular chop block', 'pressing block', 'low bent wrist block', 'middle bent wrist block',
         'high bent wrist block', 'palm corner block', 'palm push to elbow', 'funnel block']

# Leg Techniques
leg = ['upward knee kick', 'roundhouse knee kick', 'front snap kick', 'front thrust kick',
       'low back stamping kick', 'front stamping kick', 'side thrust kick', 'back thrust kick', 'roundhouse kick',
       'side snap kick', 'crescent kick', 'knee block', 'deflecting knee block', 'shin block',
       'side deflecting shin block', 'upward deflecting shin block', 'knee charge', 'heel kick',
       'jump front kick', 'flying front kick', 'jump roundhouse kick', 'flying roundhouse kick', 'arch sweep',
       'instep sweep', 'heel sweep', 'wheel kick', 'dropping kick', 'flying double front kick', 'flying side kick',
       'jump side kick', 'front spinning sweep', 'back spinning sweep', 'double low spinning sweeps',
       'reverse crescent kick', 'inside roundhouse kick', 'flying front / side kick', 'flying front / roundhouse kick',
       'flying front / crescent kick', 'inside axe kick', 'outside axe kick', 'spinning reverse crescent kick',
       'reverse dropping kick', 'flying back kick', 'flying wheel kick', 'jump spinning reverse crescent kick',
       'standing serpent kick', 'ground serpent kick']

# Katas
kata = ['Kata 1 (Taikyoku)', 'Kata 2', 'Kata 3', 'Kata 4',
        'Kata 5', 'Pinan 1', 'Pinan 2', '14 Basic Strikes (Yang Grip)', 'Pinan 3', 'Pinan 4',
         '14 basic strikes (Yin Grip)', 'Tambo 1', 'Jutte (Ten Hands)', 'Bo 1', 'Empi (Flying Swallow)', 'Bo 2',
        'Chinte (Beautiful Hands)', 'Bo 3']

# individual rank index
og_stance = stance[0:4]
og_hand = hand[0:13]
og_block = block[0:4]
og_leg = leg[0:5]
og_kata = kata[0:4]

tg_stance = stance[4:6]
tg_hand = hand[13:18]
tg_block = block[4:9]
tg_leg = leg[5:9]
tg_kata = kata[4:6]

g_stance = stance[6:7]
g_hand = hand[18:27]
g_block = block[9:16]
g_leg = leg[9:17]
g_kata = kata[6:9]

ob_stance = stance[7:8]
ob_hand = hand[27:28]
ob_block = block[16:25]
ob_leg = leg[17:25]
ob_kata = kata[9:11]

tb_stance = stance[8:11]
tb_hand = hand[28:34]
tb_block = block[25:34]
tb_leg = leg[25:33]
tb_kata = kata[9:12]

b_stance = stance[11:13]  # highest stance is [12]
b_hand = hand[34:35]
b_block = block[34:36]
b_leg = leg[33:40]
b_kata = kata[12:14]

obl_stance = b_stance
obl_hand = hand[35:43]
obl_block = block[36:41]
obl_leg = leg[40:44]
obl_kata = kata[14:16]

tbl_stance = b_stance
tbl_hand = hand[43:53]
tbl_block = block[41:42]  # highest block is [41]
tbl_leg = leg[44:47]  # highest leg is [46]
tbl_kata = kata[16:18]

bl_stance = b_stance
bl_hand = hand[53:56]
bl_block = tbl_block
bl_leg = tbl_leg
bl_kata = tbl_kata
# end individual rank index

# mixed rank index
og_stance_mix = og_stance
og_hand_mix = og_hand
og_block_mix = og_block
og_leg_mix = og_leg
og_kata_mix = og_kata

tg_stance_mix = stance[0:6]
tg_hand_mix = hand[0:18]
tg_block_mix = block[0:9]
tg_leg_mix = leg[0:9]
tg_kata_mix = kata[0:6]

g_stance_mix = stance[0:7]
g_hand_mix = hand[0:27]
g_block_mix = block[0:16]
g_leg_mix = leg[0:17]
g_kata_mix = kata[0:9]

ob_stance_mix = stance[0:8]
ob_hand_mix = hand[0:28]
ob_block_mix = block[0:25]
ob_leg_mix = leg[0:25]
ob_kata_mix = kata[0:11]

tb_stance_mix = stance[0:11]
tb_hand_mix = hand[0:34]
tb_block_mix = block[0:34]
tb_leg_mix = leg[0:33]
tb_kata_mix = kata[0:12]

b_stance_mix = stance[0:13]  # highest stance is [12]
b_hand_mix = hand[0:35]
b_block_mix = block[0:36]
b_leg_mix = leg[0:40]
b_kata_mix = kata[0:14]

obl_stance_mix = b_stance_mix
obl_hand_mix = hand[0:43]
obl_block_mix = block[0:41]
obl_leg_mix = leg[0:44]
obl_kata_mix = kata[0:16]

tbl_stance_mix = b_stance_mix
tbl_hand_mix = hand[0:53]
tbl_block_mix = block[0:42]  # highest block is [41]
tbl_leg_mix = leg[0:47]  # highest leg is [46]
tbl_kata_mix = kata[0:18 ]

bl_stance_mix = b_stance_mix
bl_hand_mix = hand[0:56]
bl_block_mix = tbl_block_mix
bl_leg_mix = tbl_leg_mix
bl_kata_mix = tbl_kata_mix

# end mixed rank index

# BEGIN USER PROGRAM
rank = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
train = [1, 2]

# Choices
print("\n 1 = Current Rank Training   2 = Mixed Rank Training")
train_in = int(input("How would you like to train? "))
if (train_in < 1 or train_in > 2):
    print("Please select either 1 or 2")
    quit()

print("\n1 = White Belt\n2 = One Green Stripe\n3 = Two Green Stripe"
      "\n4 = Green Belt\n5 = One Brown Stripe\n6 = Two Brown Stripe"
      "\n7 = Brown Belt\n8 = One Black Stripe\n9 = Two Black Stripe\n"
      "10 = Black Belt\n")
rank_select = int(input("What is your current rank? "))
if (rank_select < 1 or rank_select > 10):
    print("Please select a number between 1 and 10")
    quit()

# Select a training condition (1 or 2) to activate the nested if-statement that selects rank number
if train_in == train[0]:
    if rank_select == rank[0]:
        stance = og_stance
        hand = og_hand
        block = og_block
        leg = og_leg
        kata = og_kata
    elif rank_select == rank[1]:
        stance = tg_stance
        hand = tg_hand
        block = tg_block
        leg = tg_leg
        kata = tg_kata
    elif rank_select == rank[2]:
        stance = g_stance
        hand = g_hand
        block = g_block
        leg = g_leg
        kata = g_kata
    elif rank_select == rank[3]:
        stance = ob_stance
        hand = ob_hand
        block = ob_block
        leg = ob_leg
        kata = ob_kata
    elif rank_select == rank[4]:
        stance = tb_stance
        hand = tb_hand
        block = tb_block
        leg = tb_leg
        kata = tb_kata
    elif rank_select == rank[5]:
        stance = b_stance
        hand = b_hand
        block = b_block
        leg = b_leg
        kata = b_kata
    elif rank_select == rank[6]:
        stance = obl_stance
        hand = obl_hand
        block = obl_block
        leg = obl_leg
        kata = obl_kata
    elif rank_select == rank[7]:
        stance = tbl_stance
        hand = tbl_hand
        block = tbl_block
        leg = tbl_leg
        kata = tbl_kata
    elif rank_select == rank[8]:
        stance = bl_stance
        hand = bl_hand
        block = bl_block
        leg = bl_leg
        kata = bl_kata
    elif rank_select == rank[9]:
        stance = stance
        hand = hand
        block = block
        leg = leg
        kata = kata

# mixed training
if train_in == train[1]:
    if rank_select == rank[0]:
        stance = og_stance_mix
        hand = og_hand_mix
        block = og_block_mix
        leg = og_leg_mix
        kata = og_kata_mix
    elif rank_select == rank[1]:
        stance = tg_stance_mix
        hand = tg_hand_mix
        block = tg_block_mix
        leg = tg_leg_mix
        kata = tg_kata_mix
    elif rank_select == rank[2]:
        stance = g_stance_mix
        hand = g_hand_mix
        block = g_block_mix
        leg = g_leg_mix
        kata = g_kata_mix
    elif rank_select == rank[3]:
        stance = ob_stance_mix
        hand = ob_hand_mix
        block = ob_block_mix
        leg = ob_leg_mix
        kata = ob_kata_mix
    elif rank_select == rank[4]:
        stance = tb_stance_mix
        hand = tb_hand_mix
        block = tb_block_mix
        leg = tb_leg_mix
        kata = tb_kata_mix
    elif rank_select == rank[5]:
        stance = b_stance_mix
        hand = b_hand_mix
        block = b_block_mix
        leg = b_leg_mix
        kata = b_kata_mix
    elif rank_select == rank[6]:
        stance = obl_stance_mix
        hand = obl_hand_mix
        block = obl_block_mix
        leg = obl_leg_mix
        kata = obl_kata_mix
    elif rank_select == rank[7]:
        stance = tbl_stance_mix
        hand = tbl_hand_mix
        block = tbl_block_mix
        leg = tbl_leg_mix
        kata = tbl_kata_mix
    elif rank_select == rank[8]:
        stance = bl_stance_mix
        hand = bl_hand_mix
        block = bl_block_mix
        leg = bl_leg_mix
        kata = bl_kata_mix
    elif rank_select == rank[9]:
        stance = stance
        hand = hand
        block = block
        leg = leg
        kata = kata

combo_stance = random.choice(stance)
combo_move = random.choice([random.choice(hand), random.choice(block), random.choice(leg)])
range = ['3', '4', '5', '6', '7', '8', '9', '10']  # set numbers for random.choice(range)

# Daily Combo Prompt
print("\nGet into a " + random.choice(["left ", "right "]) + random.choice(stance)
      + ". \nPerform " + random.choice(hand) + " followed by a(n) " + random.choice(block) +
      " and a " + random.choice(leg) + ". " + "\nRepeat " + random.choice(range) + " times.""\nThen, finish with "
      + random.choice(kata) + "\n")

# Additional Practice
question = input("Would you like more practice? Y/N\n")

if question == "Y" or question == "y":
    print(random.choice(["\nAdvance, starting with left ", "Advance, starting with right ",
                     "Retreat, starting with left ", "Retreat, starting with right "])
    + random.choice(stance) + " and " + random.choice([random.choice(hand),random.choice(block),random.choice(leg)]))

    # I want to loop the print statement below to terminate after user decides to stop the generator
    while True:
        t_prompt = input("Continue? Y / N\n")
        if t_prompt == "N" or t_prompt == "n":
            print("Have a great day!")
            break
        else:
            print("Next, " + random.choice(stance) + " and " +
              random.choice([random.choice(hand), random.choice(block), random.choice(leg)]))
else:
    print("Have a great day!")
    quit()