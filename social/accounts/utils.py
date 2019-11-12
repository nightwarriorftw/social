
import string
import random
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six


def random_player_id_generator(size=10, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class TokenGenerator(PasswordResetTokenGenerator):

    def _make_hash_value(self, user, timestamp):
        return (six.text_type(user.pk) + 
            six.text_type(timestamp) + 
            six.text_type(user.is_active)
        )
account_activation_token = TokenGenerator()
