
import string
import random

def random_player_id_generator(size=10, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
