import random
import my_module

ran = random.randint(1,10)
print(ran)

print(my_module.my_favourite_num)

random_heads_or_tails = random.randint(0,1)
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")