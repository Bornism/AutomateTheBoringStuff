import random


pets = ['Dog', 'Cat', 'Moose']
random_choice = random.choice(pets)
print(random_choice)

random.shuffle(pets)
print(pets)
